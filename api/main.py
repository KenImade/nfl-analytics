"""Defines routes and controls for API"""

from fastapi import FastAPI

from api.settings import API_VERSION, API_DESCRIPTION, API_TITLE
from api.routes import router


app = FastAPI(description=API_DESCRIPTION, title=API_TITLE, version=API_VERSION)


@app.get("/", tags=["analytics"])
async def root():
    return {"message": "API health check successful"}


app.include_router(router)
