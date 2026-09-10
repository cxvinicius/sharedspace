from fastapi import FastAPI

from app.api.occupancy import router as occupancy_router


app = FastAPI()


@app.get("/")
def home():
    return {"message": "SharedSpace API funcionando!"}


app.include_router(occupancy_router)