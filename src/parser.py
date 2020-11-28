import json

from celery import Celery
from celery.utils.log import get_task_logger
import requests
from bs4 import BeautifulSoup

# Create the celery app and get the logger
app = Celery('tasks', broker='pyamqp://guest@rabbit//')
logger = get_task_logger(__name__)
# key for requests to avito api
key = 'af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir'


def get_location_id(location):
    """
    """
    url = f'http://m.avito.ru/api/1/slocations?key={key}&limit=2&q={location}'
    response = requests.get(url)
    data = json.loads(response.content)

    if location==data['result']['locations'][0]['names']['1']:
        location_id = data['result']['locations'][0]['id']
        return location_id
    else:
        raise ValueError("Invalid region name.")


@app.task
def parse_count(keyword, location):
    """
    """
    logger.info(f"Started parsing {keyword} + {location}")
    url = f'https://m.avito.ru/api/9/items?key={key}&locationId={location_id}&query={keyword}'
    response = requests.get(url)
    content = json.loads(response.content)
    count = content['result']['totalCount']
    return count
    
