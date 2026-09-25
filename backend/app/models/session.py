from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from app.enums.session_status import SessionStatus


@dataclass
class Session:
    id: UUID
    space_id: UUID
    status: SessionStatus
    started_at: datetime
    expires_at: datetime
    confirmation_requested_at: datetime | None
    ended_at: datetime | None