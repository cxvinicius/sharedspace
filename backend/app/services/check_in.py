from datetime import datetime, timedelta, timezone
from uuid import UUID, uuid4

from sqlalchemy.orm import Session as DatabaseSession

from app.database.connection import SessionLocal
from app.enums.event_type import EventType
from app.enums.session_status import SessionStatus
from app.models.event import Event
from app.models.session import Session
from app.repositories.event_repository import EventRepository
from app.repositories.session_repository import SessionRepository
from app.repositories.space_repository import SpaceRepository


SESSION_DURATION = timedelta(minutes=30)


class CheckInService:
    def execute(self, space_id: UUID) -> Session:
        db: DatabaseSession = SessionLocal()

        try:
            space_repository = SpaceRepository(db)
            session_repository = SessionRepository(db)
            event_repository = EventRepository(db)

            space = space_repository.get_by_id(space_id)

            if space is None:
                raise LookupError("Space not found.")

            occupying_sessions = (
                session_repository.count_occupying_by_space(space_id)
            )

            if occupying_sessions >= space.capacity:
                raise ValueError("Space capacity has been reached.")

            now = datetime.now(timezone.utc)

            new_session = Session(
                id=uuid4(),
                space_id=space.id,
                status=SessionStatus.ACTIVE,
                started_at=now,
                expires_at=now + SESSION_DURATION,
                confirmation_requested_at=None,
                ended_at=None,
            )

            check_in_event = Event(
                id=uuid4(),
                session_id=new_session.id,
                type=EventType.CHECK_IN,
                occurred_at=now,
            )

            session_repository.create(new_session)
            event_repository.create(check_in_event)

            db.commit()

            return new_session

        except Exception:
            db.rollback()
            raise

        finally:
            db.close()