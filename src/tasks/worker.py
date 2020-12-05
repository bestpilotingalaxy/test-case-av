from arq import cron

from .tasks import add_pair_stat, update_all_stats
from ..config import redis_settings


class WorkerSettings:
    """
    Settings for the ARQ worker.
    """
    redis_settings = redis_settings
    functions = [add_pair_stat]
    # TODO: поменять расписание на 1 раз в час
    cron_jobs = [cron(update_all_stats, minute={i for i in range(60)})]
