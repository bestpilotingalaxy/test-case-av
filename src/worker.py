from arq import cron
from arq.connections import RedisSettings

from .tasks import add_pair_stat, update_all_stats

settings = RedisSettings(host='redis', port=6379)

class WorkerSettings:
    """
    Settings for the ARQ worker.
    """
    redis_settings = settings
    functions = [add_pair_stat]
    cron_jobs = [cron(update_all_stats, minute='*/1')]
