from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from arq.connections import ArqRedis, create_pool

from .parser import get_location_id
from .db.models import AddRequestBody, StatRequestBody, Pair
from .db.actions import pairs_collection, get_stats, add_new_pair
from .worker import settings as redis_settings

app = FastAPI()


@app.post("/add")
async def add(body: AddRequestBody):
# Добавить проверку на наличие пары !!!
    location_id = await get_location_id(body.location)
    if location_id is None:
        raise HTTPException(status_code=400,
                            detail="Invalid region name.")
    # сделать uuid уникальным для пары ключ+значение
    pair_id = await add_new_pair(body.keyword, body.location, location_id)
    redis: ArqRedis = await create_pool(settings_=redis_settings)
    await redis.enqueue_job(
        'add_pair_stat',
        pair_id,
        body.keyword,
        location_id
    )
    return {'pair_id': pair_id}


@app.post("/stat")
async def stat(body: StatRequestBody):
# Обработать некорретные запросы
    stats = await get_stats(body.pair_id, body.start, body.end)
    return {'stats': stats}
