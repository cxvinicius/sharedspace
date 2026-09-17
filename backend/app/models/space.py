from dataclasses import dataclass
from uuid import UUID


@dataclass
class Space:
    id: UUID
    name: str
    description: str | None
    capacity: int