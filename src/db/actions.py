from datetime import datetime

import motor.motor_asyncio

# connection instance
MONGO_DETAILS = "mongodb://mongo:27017"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

# database instance
database = client.avito

pairs_collection = database.get_collection("pairs")
stats_collection = database.get_collection("stats")

# Всетаки надо написать конвертер JSON обьектов в словарик

# TODO: add async CRUD actions
# def pair_deserialize(pair) -> dict:
#     pair{
#         "pair_id": pair["_id"],
#         "keyword": pair["keyword"],
#         "location": pair["location"]
#         "location_id": pair["location_id"],
#     }
#     return pair
#
async def get_all_pairs():
    pairs = []
    async for pair in pairs_collection.find():
        pairs.append(pair.to_dict())
    return pairs

async def get_stats(pair_id, start, end):
    stats = []
    async for stat in stats_collection.find({"timestamp":{
                        "$gte": datetime.isoformat(start),
                        "$lt": datetime.isoformat(end)}}):
        stats.append(stat.to_dict())
    return stats
