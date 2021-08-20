from pydantic import BaseModel
from datetime import date
from typing import List


class AnnounceBase(BaseModel):
    title: str
    category: str
    date: date
    description: str
    connect: str


class AnnounceCreate(AnnounceBase):
    pass


class AnnounceUpdate(AnnounceBase):
    pass


class Announce(AnnounceBase):
    id: int

    class Config:
        orm_mode = True
