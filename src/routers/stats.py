from fastapi import APIRouter, Depends

from .dependencies import verify_pair_no_exist, verify_id_format
from ..db.actions import  get_stats
from ..db.models import StatRequestBody, StatResponse


router = APIRouter()


@router.post(
    "/stat",
    response_model=StatResponse,
    dependencies=[Depends(verify_id_format), Depends(verify_pair_no_exist)]
)
async def stat(body: StatRequestBody) -> dict:
    """
    Get all stats for current pair in the specified time interval.
    """
    stats = await get_stats(body.pair_id, body.start, body.end)
    return {'stats': stats}

