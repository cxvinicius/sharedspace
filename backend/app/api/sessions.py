from uuid import UUID

from fastapi import APIRouter, HTTPException, status

from app.services.check_out import CheckOutService
from app.services.confirm_session import ConfirmSessionService


router = APIRouter()


def session_response(session) -> dict:
    return {
        "id": str(session.id),
        "space_id": str(session.space_id),
        "status": session.status.value,
        "started_at": session.started_at,
        "expires_at": session.expires_at,
        "ended_at": session.ended_at,
    }


@router.post("/sessions/{session_id}/checkout")
def check_out(session_id: UUID) -> dict:
    try:
        session = CheckOutService().execute(session_id)
        return session_response(session)

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


@router.post("/sessions/{session_id}/confirm")
def confirm_session(session_id: UUID) -> dict:
    try:
        session = ConfirmSessionService().execute(session_id)
        return session_response(session)

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