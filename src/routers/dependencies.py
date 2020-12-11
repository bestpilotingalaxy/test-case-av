from fastapi import HTTPException
from bson import ObjectId
from bson.errors import InvalidId

from ..db.models import AddRequestBody, StatRequestBody
from ..db.actions import pairs_collection
from ..parsing.parsing import get_location_id


async def verify_pair_exist(body: AddRequestBody):
    """
    Verify if such keyword + location pair already exist in database. 
    """    
    pair = await pairs_collection.find_one(
        {"keyword": body.keyword, "location": body.location}
    )
    if pair:
        raise HTTPException(
            status_code=400,
            detail=f"Pair already exist. id: {pair['_id']}"
        )


async def verify_region_name(body: AddRequestBody):
    """
    Verify if avito.ru contains region with such name.
    """
    location_id = await get_location_id(body.location)
    if location_id is None:
        raise HTTPException(status_code=400, detail="Invalid region name.")
    else:
        return location_id


async def verify_id_format(body: StatRequestBody):
    """
    Checks 'pair_id' string is ObjectId supported format.
    """
    try:
        ObjectId(body.pair_id)
    except InvalidId:
        raise HTTPException(status_code=400, detail="Invalid pair_id format.")
    
 
async def verify_pair_no_exist(body: StatRequestBody):
    """
    Verify if no such pair_id saved in database.
    """
    pair = await pairs_collection.find_one({"_id": ObjectId(body.pair_id)})
    if pair is None:
        raise HTTPException(status_code=404, detail="No such pair.")