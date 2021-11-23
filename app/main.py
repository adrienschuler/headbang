from typing import List
from fastapi import (
    BackgroundTasks,
    FastAPI,
    HTTPException
)
from elasticsearch.exceptions import ConnectionError

from app import logger

from app.backends.elasticsearch import ES
from app.backends.luigi import Luigi
from app.clients.spotify import Spotify
from app.core.models import Artist


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/artist/{artist_id}", response_model=Artist)
async def get_artist(artist_id: str = None) -> Artist:
    return Spotify.get_artist(artist_id)


@app.post("/me/following")
async def fetch_followed_artists(background_tasks: BackgroundTasks):
    background_tasks.add_task(Luigi.trigger)
    return {"message": "Triggered task in the background"}


@app.get("/search/{query}", response_model=List[Artist])
async def search(query: str = None):
    try:
        logger.debug(query)
        return ES.search(query)
    except (AttributeError, ConnectionError):
        raise HTTPException(status_code=500, detail="Search backend exception")


@app.post("/callback")
async def post_callback():
    return {"message": "Received callback!"}
