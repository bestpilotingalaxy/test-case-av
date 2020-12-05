from datetime import datetime

from pydantic import BaseModel


class AddRequestBody(BaseModel):
    """
    Request data model for "/add" route.
    """
    keyword: str
    location: str


class StatRequestBody(BaseModel):
    """
    Request data model for "/stat" route.
    """
    pair_id: str
    start: datetime
    end: datetime
