from datetime import datetime

from celery import Celery
from celery.utils.log import get_task_logger
from celery.schedules import crontab

from .db.actions import get_all_pairs, stats_collection, pairs_collection
from .parser import parse_count

# Create the celery app and get the logger
app = Celery('tasks', broker='pyamqp://guest@rabbit//')
logger = get_task_logger(__name__)


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    #
    sender.add_periodic_task(
        crontab(minute='*/1'),
        collect_pairs_stats.s(),
        name='Stats update'
    )


@app.task
def collect_pairs_stats():
    """
    """
    pairs = get_all_pairs()
    for pair in pairs:
        stat = parse_count(
            pair['pair_id'], pair['keyword'], pair['location_id']
        )
        stats_collection.insert_one(stat)


@app.task
def add_new_pair(pair_id, keyword, location, location_id):
    """
    """
    pairs_collection.insert_one({
        '_id': pair_id,
        'keyword': keyword,
        'location': location,
        'location_id': location_id
    })

    stat = parse_count(pair_id, keyword, location_id)

    stats_collection.insert_one(stat
    # {
    #     'pair_id': pair_id,
    #     'count': stat,
    #     'timestamp': datetime.now().isoformat()
    # }
    )
