
from uuid import UUID

from sqlalchemy.orm import Session as DatabaseSession

from app.database.connection import SessionLocal
from app.repositories.session_repository import SessionRepository
from app.repositories.space_repository import SpaceRepository


class OccupancyService:
    def execute(self, space_id: UUID) -> dict:
        db: DatabaseSession = SessionLocal()

        try:
            space_repository = SpaceRepository(db)
            session_repository = SessionRepository(db)

            space = space_repository.get_by_id(space_id)

            if space is None:
                raise LookupError("Space not found.")

            occupied = (
                session_repository.count_occupying_by_space(space_id)
            )

            return {
                "space_id": str(space.id),
                "capacity": space.capacity,
                "occupied": occupied,
                "available": max(space.capacity - occupied, 0),
            }

        finally:
            db.close()