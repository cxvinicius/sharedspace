from datetime import datetime, timedelta, timezone
from uuid import uuid4

from sqlalchemy.orm import Session as DatabaseSession

from app.database.connection import SessionLocal
from app.enums.event_type import EventType
from app.enums.session_status import SessionStatus
from app.models.event import Event
from app.repositories.event_repository import EventRepository
from app.repositories.session_repository import SessionRepository


CONFIRMATION_WINDOW = timedelta(minutes=5)


class SessionLifecycleService:
    def process_expirations(self) -> None:
        db: DatabaseSession = SessionLocal()

        try:
            session_repository = SessionRepository(db)
            event_repository = EventRepository(db)

            now = datetime.now(timezone.utc)

            # Expired ACTIVE sessions enter the confirmation window.
            expired_active = session_repository.get_expired_by_status(
                SessionStatus.ACTIVE,
                now,
            )

            for session in expired_active:
                session.status = SessionStatus.CONFIRMATION_PENDING
                session.confirmation_requested_at = now
                session.expires_at = now + CONFIRMATION_WINDOW

                session_repository.update(session)

            # Expired confirmation windows terminate the session.
            expired_pending = session_repository.get_expired_by_status(
                SessionStatus.CONFIRMATION_PENDING,
                now,
            )

            for session in expired_pending:
                session.status = SessionStatus.AUTO_TERMINATED
                session.ended_at = now

                session_repository.update(session)

                event_repository.create(
                    Event(
                        id=uuid4(),
                        session_id=session.id,
                        type=EventType.AUTO_TERMINATION,
                        occurred_at=now,
                    )
                )

            db.commit()

        except Exception:
            db.rollback()
            raise

        finally:
            db.close()