from datetime import datetime

from arq.connections import ArqRedis, create_pool

from .db.actions import get_all_pairs, stats_collection, pairs_collection
from .parser import parse_count
from .main import redis_settings


async def add_pair_stat(ctx: dict, pair_id, keyword, location_id):
    """
    """
    count = await parse_count(pair_id, keyword, location_id)
    stat = {
        'pair_id': pair_id,
        'count': count,
        'timestamp': datetime.now().isoformat()
    }
    await stats_collection.insert_one(stat)


async def update_all_stats(ctx: dict):

    all_pairs = await get_all_pairs()
    redis: ArqRedis = await create_pool(settings_=redis_settings)
    for pair in all_pairs:
        await redis.enqueue_job(
            'add_pair_stat',
            pair['pair_id'],
            pair['keyword'],
            pair['location_id']
        )
