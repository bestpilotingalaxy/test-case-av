from pydantic import BaseModel, Field


#TODO find better name for dat classes !!!
class Pair(BaseModel):
    """
    """
    id: str = Field(alias='_id')
    keyword: str
    location_id: int

class Stats(BaseModel):
    """
    """
    pair_id: str
    count: int
    datetime: datetime


class AddRequestBody(BaseModel):
    """
    """
    keyword: str
    location: str
