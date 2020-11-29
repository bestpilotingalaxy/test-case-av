from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from celery import uuid

from .parser import get_location_id, parse_count
from .db.models import AddRequestBody, Pair
from .db.actions import database as mongo

app = FastAPI()


@app.post("/add")
def parse(item: AddRequestBody):
    try:
        location_id = get_location_id(item.location)
    except ValueError:
        raise HTTPException(status_code=400,
                            detail="Invalid region name.")
    pair_id = uuid()
    mongo.pairs.insert({
        '_id': pair_id,
        'keyword': item.keyword,
        'location_id': location_id
    })
    parse_count.delay(item.keyword, location_id)
    return {"pair_id": pair_id}
