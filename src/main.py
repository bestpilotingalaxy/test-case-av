from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from .parser import get_location_id, parse_count
from .parser import app as celery_app

app = FastAPI()


class Item(BaseModel):
    keyword: str
    location: str


@app.post("/add")
def parse(item: Item):
    try:
        location = get_location_id(item.location)
    except ValueError:
        raise HTTPException(
            status_code=400,
            detail="Invalid region name."
        )
    parse_count.delay(item.keyword, location)
    return {"pair_id": }   
