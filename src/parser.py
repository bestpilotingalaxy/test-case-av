import json

import requests

# key for requests to avito api
key = 'af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir'


async def get_location_id(location: str):
    """
    Make request to avito api and parse response to get location id.
    """
    url = f'http://m.avito.ru/api/1/slocations?key={key}&limit=2&q={location}'
    response = requests.get(url)
    content = json.loads(response.content)
    # checks the location name match
    for region_data in content['result']['locations']:
        if location==region_data['names']['1']:
            return region_data['id']   
    

async def parse_count(keyword: str, location_id: int) -> int:
    """
    Parse averts count for current keyword and locationId.
    """
    url = f'https://m.avito.ru/api/9/items?key={key}&locationId={location_id}&query={keyword}'
    response = requests.get(url)
    content = json.loads(response.content)
    count = content['result']['totalCount']
    return count

