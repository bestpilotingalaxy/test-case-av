from fastapi import FastAPI

from .config import  get_settings
from .routers import pairs, stats


app = FastAPI()


app.include_router(pairs.router)
app.include_router(stats.router)


@app.get("/config")
async def get_config():
    """
    Service settings and env variables.
    """
    return get_settings().dict()


@app.get("/")
async def ping():
    """
    Simple ping for healthcheckers.
    """
    return "OK"
