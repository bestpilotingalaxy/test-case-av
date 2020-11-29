import motor.motor_asyncio

# connection instance
MONGO_DETAILS = "mongodb://localhost:27017"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

# database instance
database = client.avito
