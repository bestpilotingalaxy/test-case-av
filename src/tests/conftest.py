import datetime
import asyncio

import pytest
from starlette.testclient import TestClient

from ..main import app


@pytest.fixture(scope="module")
def test_app():
    client = TestClient(app)
    yield client


# @pytest.yield_fixture(scope='session')
# def event_loop(request):
#     """Create an instance of the default event loop for each test case."""
#     loop = asyncio.get_event_loop_policy().new_event_loop()
#     yield loop
#     loop.close()
    

def create_timestamps(days: int, minutes: int):
    """
    Create time interval for test.
    """
    now = datetime.datetime.now()
    start = now - datetime.timedelta(days=days, minutes=minutes)
    end = now + datetime.timedelta(days=days, minutes=minutes)

    return {"start": str(start), "end": str(end)}
