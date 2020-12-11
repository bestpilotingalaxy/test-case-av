from fastapi import APIRouter, Depends
from arq.connections import ArqRedis, create_pool

from .dependencies import verify_pair_exist, verify_region_name
from ..db.actions import  add_new_pair
from ..config import redis_settings
from ..db.models import AddRequestBody, AddResponse


router = APIRouter()


@router.post(
    "/add",
    response_model=AddResponse,
    dependencies=[Depends(verify_pair_exist), Depends(verify_region_name)]
)
async def add(
    body: AddRequestBody,
    location_id: int = Depends(verify_region_name)
) -> dict:
    """
    Register new pair.
    """
    pair_id = await add_new_pair(body.keyword, body.location, location_id)
    redis: ArqRedis = await create_pool(settings_=redis_settings)
    await redis.enqueue_job(
        'add_pair_stat', pair_id, body.keyword, location_id
    )
    return {'pair_id': pair_id}
