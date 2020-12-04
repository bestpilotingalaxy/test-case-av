from datetime import datetime

import motor.motor_asyncio

# connection instance
MONGO_DETAILS = "mongodb://mongo:27017"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

# database instance
database = client.avito

# async collections shortcuts
pairs_collection = database.get_collection("pairs")
stats_collection = database.get_collection("counts")


async def get_all_pairs() -> list:
    """
    Returns all pair objects from db as a list.
    """
    pairs = []
    async for pair in pairs_collection.find():
        pairs.append(pair)
    return pairs


async def get_stats(pair_id: str, start, end) -> list:
    """
    Filter all stats from *start* to *end* timestamps for current pair_id.
    """
    stats = []
    async for stat in stats_collection.find({
        "pair_id": pair_id,
        "timestamp":{"$gte": datetime.isoformat(start),
                     "$lt": datetime.isoformat(end)}}):
        stats.append({'count': stat['count'], 'timestamp': stat['timestamp']})
    return stats


async def add_new_pair(keyword: str, location: str, location_id: int) -> str:
    """
    Add new pair object to database.
    """
    pair_data = {
        "keyword": keyword,
        "location": location,
        "location_id": location_id
    }
    pair = await pairs_collection.insert_one(pair_data)
    return str(pair.inserted_id)
