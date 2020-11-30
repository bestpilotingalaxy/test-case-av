import json
from datetime import datetime

import requests

# key for requests to avito api
key = 'af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir'


async def get_location_id(location):
    """
    """
    url = f'http://m.avito.ru/api/1/slocations?key={key}&limit=2&q={location}'
    response = requests.get(url)
    data = json.loads(response.content)

    if location==data['result']['locations'][0]['names']['1']:
        location_id = data['result']['locations'][0]['id']
        return location_id
    else:
        return None


async def parse_count(pair_id, keyword, location_id):
    """
    """
    url = f'https://m.avito.ru/api/9/items?key={key}&locationId={location_id}&query={keyword}'
    response = requests.get(url)
    content = json.loads(response.content)
    count = content['result']['totalCount']
    stat = {
        'pair_id': pair_id,
        'count': count,
        'timestamp': datetime.now().isoformat()
    }
    return stat
