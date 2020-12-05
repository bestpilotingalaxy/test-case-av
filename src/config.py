import os

from arq.connections import RedisSettings
import motor.motor_asyncio as m

# mongo client instance
MONGO_DETAILS = "mongodb://mongo:27017"
mongo_client = m.AsyncIOMotorClient(MONGO_DETAILS)

# redis settings object
REDIS_SETTINGS = RedisSettings(host='redis', port=6379)