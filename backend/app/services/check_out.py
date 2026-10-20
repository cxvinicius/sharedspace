from datetime import datetime, timezone
from uuid import UUID, uuid4

from sqlalchemy.orm import Session as DatabaseSession

from app.database.connection import SessionLocal
from app.enums.event_type import EventType
from app.enums.session_status import SessionStatus
from app.models.event import Event
from app.models.session import Session
from app.repositories.event_repository import EventRepository
from app.repositories.session_repository import SessionRepository


class CheckOutService:
    def execute(self, session_id: UUID) -> Session:
        db: DatabaseSession = SessionLocal()

        try:
            session_repository = SessionRepository(db)
            event_repository = EventRepository(db)

            session = session_repository.get_by_id_for_update(session_id)

            if session is None:
                raise LookupError("Session not found.")

            allowed_statuses = {
                SessionStatus.ACTIVE,
                SessionStatus.CONFIRMATION_PENDING,
            }

            if session.status not in allowed_statuses:
                raise ValueError("Session has already ended.")

            now = datetime.now(timezone.utc)

            session.status = SessionStatus.COMPLETED
            session.ended_at = now

            session_repository.update(session)

            event_repository.create(
                Event(
                    id=uuid4(),
                    session_id=session.id,
                    type=EventType.CHECK_OUT,
                    occurred_at=now,
                )
            )

            db.commit()
            return session

        except Exception:
            db.rollback()
            raise

        finally:
            db.close()