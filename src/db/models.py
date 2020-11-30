from datetime import datetime

from pydantic import BaseModel, Field



#TODO find better name for dat classes !!!
class Pair(BaseModel):
    """
    """
    id: str = Field(alias='_id')
    keyword: str
    location: str
    location_id: int


class Stat(BaseModel):
    """
    """
    pair_id: str
    count: int
    timestamp: datetime


class AddRequestBody(BaseModel):
    """
    """
    keyword: str
    location: str


class StatRequestBody(BaseModel):
    """
    """
    pair_id: str
    start: datetime
    end: datetime
