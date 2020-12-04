from datetime import datetime
from bson.objectid import ObjectId

from pydantic import BaseModel, Field


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
