from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from app.enums.event_type import EventType


@dataclass
class Event:
    id: UUID
    session_id: UUID
    type: EventType
    occurred_at: datetime