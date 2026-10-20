from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session as DatabaseSession

from app.models.space import Space
from app.persistence.models.space import SpaceModel


class SpaceRepository:
    def __init__(self, db: DatabaseSession) -> None:
        self.db = db

    def get_by_id(self, space_id: UUID) -> Space | None:
        statement = (
            select(SpaceModel)
            .where(SpaceModel.id == space_id)
            .with_for_update()
        )

        space_model = self.db.scalar(statement)

        if space_model is None:
            return None

        return Space(
            id=space_model.id,
            name=space_model.name,
            description=space_model.description,
            capacity=space_model.capacity,
        )
