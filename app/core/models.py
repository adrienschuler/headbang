from datetime import datetime

from typing import List
from pydantic import BaseModel


class Image(BaseModel):
    url: str
    width: int
    height: int


class Artist(BaseModel):
    id: str
    name: str
    genres: List[str] = []
    images: List[Image] = []
    updated_at: datetime = datetime.now()


class Venue(BaseModel):
    id: str
    name: str
    address: str
    updated_at: datetime = datetime.now()


class Concert(BaseModel):
    id: str
    name: str
    date: datetime = None
    artists: List[Artist] = []
    venue: Venue = None
    updated_at: datetime = datetime.now()


class Chord(BaseModel):
    short_name: str
    long_name: str
    function: str


class Progression(BaseModel):
    id: str
    key: str
    bpm: int
    sections: List[Section] = []
