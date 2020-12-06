import json
import pytest
from requests.api import post
from starlette import responses


def test_ping(test_app):
    response = test_app.get("/")
    assert response.status_code == 200
    assert response.json() == "OK"


def test_config(test_app):
    response = test_app.get("/config")
    assert response.status_code == 200
    assert response.json()["service_name"] == "Avito API"


def test_add_pair(test_app):
    response = test_app.post(
        "/add", json={"keyword": "Стекловата", "location": "Москва"}
    )
    assert response.status_code == 200
    assert ("pair_id" in response.json()) == True
    assert type(response.json()["pair_id"]) == str


def test_add_already_existing_pair(test_app):
    response = test_app.post(
        "/add", json={"keyword": "Стекловата", "location": "Москва"}
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "Pair already exist."}
    

def test_add_pair_invalid_location(test_app):
    response = test_app.post(
        "/add", json={"keyword": "Юнит тесты", "location": "Лапландия"}
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid region name."}
