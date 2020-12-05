from datetime import datetime

from arq.connections import ArqRedis, create_pool

from ..db.actions import get_all_pairs, stats_collection
from ..parsing.parser import parse_count
from ..config import REDIS_SETTINGS


async def add_pair_stat(ctx: dict, pair_id, keyword, location_id):
    """
    ARQ task to parse advert count and save to DB.
    """
    count = await parse_count(keyword, location_id)
    stat = {
        'pair_id': pair_id,
        'count': count,
        'timestamp': datetime.now().isoformat()
    }
    await stats_collection.insert_one(stat)


async def update_all_stats(ctx: dict):
    """
    ARQ cron regular task. Runs every hour.
    Enqueue add_pair_stat() task for every pair in DB.
    """
    all_pairs = await get_all_pairs()
    redis: ArqRedis = await create_pool(settings_=REDIS_SETTINGS)
    for pair in all_pairs:
        await redis.enqueue_job(
            'add_pair_stat',
            str(pair['_id']),
            pair['keyword'],
            pair['location_id']
        )
