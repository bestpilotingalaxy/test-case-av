from functools import lru_cache

from pydantic import BaseSettings, Field
from arq.connections import RedisSettings
from motor.motor_asyncio import AsyncIOMotorClient


class Settings(BaseSettings):
    """
    Service settings and enviroment variables.
    """
    service_name: str = "Avito API"
    
    REDIS_NAME: str = Field(env='REDIS_NAME')
    REDIS_PORT: int = Field(env='REDIS_PORT')
    
    MONGO_NAME: str = Field(env='MONGO_NAME')
    MONGO_PORT: int = Field(env='MONGO_PORT')
    
    UVICORN_PORT: int = Field(env='UVICORN_PORT')
    
    TIME_ZONE: str = Field(env='TZ')
    
    class Config:
        env_file = ".env"


@lru_cache
def get_settings() -> Settings:
    return Settings()


# MOTOR CLIENT CONNECTION 
MONGO_URL = f"mongodb://{get_settings().MONGO_NAME}:{get_settings().MONGO_PORT}"
mongo_client = AsyncIOMotorClient(MONGO_URL)

# REDIS SETTINGS FOR ARQ
redis_settings = RedisSettings(
    host=get_settings().REDIS_NAME,
    port=get_settings().REDIS_PORT
)

