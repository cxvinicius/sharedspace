from sqlalchemy.orm import Session as DatabaseSession

from app.models.event import Event
from app.persistence.models.event import EventModel


class EventRepository:
    def __init__(self, db: DatabaseSession) -> None:
        self.db = db

    def create(self, event: Event) -> None:
        event_model = EventModel(
            id=event.id,
            session_id=event.session_id,
            type=event.type.value,
            occurred_at=event.occurred_at,
        )

        self.db.add(event_model)
        self.db.flush()