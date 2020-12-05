from fastapi import FastAPI
from arq.connections import ArqRedis, create_pool

from .db.models import AddRequestBody, StatRequestBody
from .db.actions import get_stats, add_new_pair
from .config import redis_settings, get_settings
from .routes.validation import add_req_validator, stat_req_validator


app = FastAPI()


@app.post("/add")
async def add(body: AddRequestBody):
    """
    Register new pair.
    """
    location_id = await add_req_validator(body)
    pair_id = await add_new_pair(body.keyword, body.location, location_id)
    redis: ArqRedis = await create_pool(settings_=redis_settings)
    await redis.enqueue_job(
        'add_pair_stat', pair_id, body.keyword, location_id
    )
    return {'pair_id': pair_id}


@app.post("/stat")
async def stat(body: StatRequestBody):
    """
    Get all stats for current pair in the specified time interval.
    """
    await stat_req_validator(body)
    stats = await get_stats(body.pair_id, body.start, body.end)
    return {'stats': stats}


@app.get("/config")
async def get_config():
    """
    Service settings and env variables.
    """
    return get_settings().dict()


@app.get("/")
async def ping():
    """
    Simple ping for healthcheckers.
    """
    return "OK"
