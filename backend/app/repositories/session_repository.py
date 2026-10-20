from datetime import datetime
from uuid import UUID

from sqlalchemy import func, select, update
from sqlalchemy.orm import Session as DatabaseSession

from app.enums.session_status import SessionStatus
from app.models.session import Session
from app.persistence.models.session import SessionModel


class SessionRepository:
    def __init__(self, db: DatabaseSession) -> None:
        self.db = db

    def count_occupying_by_space(self, space_id: UUID) -> int:
        statement = (
            select(func.count())
            .select_from(SessionModel)
            .where(
                SessionModel.space_id == space_id,
                SessionModel.status.in_(
                    [
                        SessionStatus.ACTIVE.value,
                        SessionStatus.CONFIRMATION_PENDING.value,
                    ]
                ),
            )
        )

        return self.db.scalar(statement) or 0

    def create(self, session: Session) -> None:
        session_model = SessionModel(
            id=session.id,
            space_id=session.space_id,
            status=session.status.value,
            started_at=session.started_at,
            expires_at=session.expires_at,
            confirmation_requested_at=session.confirmation_requested_at,
            ended_at=session.ended_at,
        )

        self.db.add(session_model)
        self.db.flush()

    def get_by_id_for_update(
        self,
        session_id: UUID,
    ) -> Session | None:
        statement = (
            select(SessionModel)
            .where(SessionModel.id == session_id)
            .with_for_update()
        )

        model = self.db.scalar(statement)

        if model is None:
            return None

        return Session(
            id=model.id,
            space_id=model.space_id,
            status=SessionStatus(model.status),
            started_at=model.started_at,
            expires_at=model.expires_at,
            confirmation_requested_at=model.confirmation_requested_at,
            ended_at=model.ended_at,
        )

    def update(self, session: Session) -> None:
        statement = (
            update(SessionModel)
            .where(SessionModel.id == session.id)
            .values(
                status=session.status.value,
                expires_at=session.expires_at,
                confirmation_requested_at=session.confirmation_requested_at,
                ended_at=session.ended_at,
            )
        )

        self.db.execute(statement)
        self.db.flush()

    def get_expired_by_status(
        self,
        session_status: SessionStatus,
        now: datetime,
    ) -> list[Session]:
        statement = (
            select(SessionModel)
            .where(
                SessionModel.status == session_status.value,
                SessionModel.expires_at <= now,
            )
            .with_for_update(skip_locked=True)
        )

        models = self.db.scalars(statement).all()

        return [
            Session(
                id=model.id,
                space_id=model.space_id,
                status=SessionStatus(model.status),
                started_at=model.started_at,
                expires_at=model.expires_at,
                confirmation_requested_at=model.confirmation_requested_at,
                ended_at=model.ended_at,
            )
            for model in models
        ]