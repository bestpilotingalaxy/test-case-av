from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class AddRequestBody(BaseModel):
    """
    Request data model for "/add" route.
    """
    keyword: str
    location: str


class AddResponse(BaseModel):
    """
    Response models for "/add" route.
    """
    pair_id: str
    
    
class StatRequestBody(BaseModel):
    """
    Request data model for "/stat" route.
    """
    pair_id: str
    start: datetime
    end: datetime


class PairStat(BaseModel):
    """
    Single stat object in stats list.
    """
    count: int
    timestamp: datetime


class StatResponse(BaseModel):
    """
    Response models for "/stat" route.
    """
    stats: Optional[List[PairStat]] = None
    