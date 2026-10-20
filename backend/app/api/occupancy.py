
from uuid import UUID

from fastapi import APIRouter, HTTPException, status

from app.services.occupancy import OccupancyService


router = APIRouter()


@router.get("/spaces/{space_id}/occupancy")
def get_occupancy(space_id: UUID) -> dict:
    try:
        return OccupancyService().execute(space_id)

    except LookupError as error:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(error),
        ) from error