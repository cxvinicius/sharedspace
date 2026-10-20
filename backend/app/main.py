import asyncio
import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.check_in import router as check_in_router
from app.api.occupancy import router as occupancy_router
from app.api.sessions import router as sessions_router
from app.services.session_lifecycle import SessionLifecycleService


logger = logging.getLogger(__name__)


async def run_session_lifecycle() -> None:
    service = SessionLifecycleService()

    while True:
        try:
            await asyncio.to_thread(service.process_expirations)
        except Exception:
            logger.exception(
                "Failed to process session expirations."
            )

        await asyncio.sleep(15)


@asynccontextmanager
async def lifespan(app: FastAPI):
    lifecycle_task = asyncio.create_task(
        run_session_lifecycle()
    )
    app.state.lifecycle_task = lifecycle_task

    try:
        yield
    finally:
        lifecycle_task.cancel()

        try:
            await lifecycle_task
        except asyncio.CancelledError:
            pass


app = FastAPI(lifespan=lifespan)


@app.get("/")
def home() -> dict[str, str]:
    return {"message": "SharedSpace API funcionando!"}


app.include_router(occupancy_router)
app.include_router(check_in_router)
app.include_router(sessions_router)