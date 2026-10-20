from uuid import UUID

from fastapi import APIRouter, HTTPException, status

from app.services.check_in import CheckInService


router = APIRouter()


@router.post(
    "/spaces/{space_id}/sessions",
    status_code=status.HTTP_201_CREATED,
)
def check_in(space_id: UUID) -> dict:
    try:
        session = CheckInService().execute(space_id)

    except LookupError as error:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(error),
        ) from error

    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(error),
        ) from error

    return {
        "id": str(session.id),
        "space_id": str(session.space_id),
        "status": session.status.value,
        "started_at": session.started_at,
        "expires_at": session.expires_at,
    }