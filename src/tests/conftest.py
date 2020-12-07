import datetime

import pytest
from starlette.testclient import TestClient

from ..main import app


@pytest.fixture(scope="module")
def test_app():
    client = TestClient(app)
    yield client
    

def create_timestamps(days: int, minutes: int):
    """
    Create time interval for test.
    """
    now = datetime.datetime.now()
    start = now - datetime.timedelta(days=days, minutes=minutes)
    end = now + datetime.timedelta(days=days, minutes=minutes)

    return {"start": str(start), "end": str(end)}
