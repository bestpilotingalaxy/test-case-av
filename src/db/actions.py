from datetime import datetime

import motor.motor_asyncio

# connection instance
MONGO_DETAILS = "mongodb://mongo:27017"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

# database instance
database = client.avito

pairs_collection = database.get_collection("pairs")
stats_collection = database.get_collection("counts")


async def get_all_pairs():
    pairs = []
    async for pair in pairs_collection.find():
        pairs.append(pair)
    return pairs


async def get_stats(pair_id, start, end):
    stats = []
    async for stat in stats_collection.find({
        "pair_id": pair_id,
        "timestamp":{"$gte": datetime.isoformat(start),
                     "$lt": datetime.isoformat(end)}}):
        stats.append({'count': stat['count'], 'timestamp': stat['timestamp']})
    return stats


async def add_new_pair(keyword, location, location_id):
    pair_data = {
        "keyword": keyword,
        "location": location,
        "location_id": location_id
    }
    pair = await pairs_collection.insert_one(pair_data)
    return pair.inserted_id
