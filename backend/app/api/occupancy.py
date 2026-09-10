from fastapi import APIRouter

router = APIRouter()


@router.get("/spaces/{space_id}/occupancy")
def get_occupancy(space_id: int):
    return {
        "space_id": space_id,
        "capacity": 5,
        "occupied": 3,
        "available": 2
    }