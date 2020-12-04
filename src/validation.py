from fastapi import HTTPException
from bson import ObjectId
from bson.errors import InvalidId

from .db.actions import pairs_collection
from .parser import get_location_id


async def add_req_validator(body: object):
    """
    Request data validation for "/add" route.
    """    
    pair = await pairs_collection.find_one(
        {"keyword": body.keyword, "location": body.location}
    )
    if pair:
        raise HTTPException(status_code=400, detail="Pair already exist.")
    # check location_id existance for current location name
    location_id = await get_location_id(body.location)
    if location_id is None:
        raise HTTPException(status_code=400, detail="Invalid region name.")
    else:
        return location_id


async def stat_req_validator(body: object):
    """
    Request data validation for "/stat" route.
    """
    try:
        # check 'pair_id' string is ObjectId supported format
        pair_id = ObjectId(body.pair_id)
    except InvalidId:
        raise HTTPException(status_code=400, detail="Invalid pair_id string.")
    # check if such pair exist
    pair = await pairs_collection.find_one({"_id": pair_id})
    if pair is None:
        raise HTTPException(status_code=404, detail="No such pair.")