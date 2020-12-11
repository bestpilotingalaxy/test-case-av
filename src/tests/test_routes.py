import time
from bson import ObjectId

from .conftest import create_timestamps


def test_ping(test_app):
    # "/" test ping for healthcheckers
    response = test_app.get("/")
    assert response.status_code == 200
    assert response.json() == "OK"


def test_config(test_app):
    # "/config" request to get app config
    response = test_app.get("/config")
    assert response.status_code == 200
    assert response.json()["service_name"] == "Avito API"


def test_add_pair(test_app):
    # "/add" request to add new pair
    response = test_app.post(
        "/add", json={"keyword": "Стекловата", "location": "Москва"}
    )
    assert response.status_code == 200
    assert "pair_id" in response.json()
    assert type(response.json()["pair_id"]) == str
    
    time.sleep(2)
    # "/stat" request body data
    pair_id = response.json()["pair_id"]
    timestamps = create_timestamps(1, 0)
    # "/stat" request to get stats for created pair
    response = test_app.post(
        "/stat",
        json={
            "pair_id": pair_id,
            "start": timestamps["start"],
            "end": timestamps["end"]
        }
    )
    assert response.status_code == 200
    assert len(response.json()["stats"]) >= 1


def test_add_already_existing_pair(test_app):
    # test "/add" route with already existing pair keyword+location
    response = test_app.post(
        "/add", json={"keyword": "Стекловата", "location": "Москва"}
    )
    assert response.status_code == 400
    

def test_add_pair_invalid_location(test_app):
    # test "/add" route with invalid location data
    response = test_app.post(
        "/add", json={"keyword": "Юнит тесты", "location": "Лапландия"}
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid region name."}


def test_get_stat_invalid_pair_id(test_app):
    # test "/stat" route with invalid pair_id string format
    timestamps = create_timestamps(1, 0)
    response = test_app.post(
        "/stat",
        json={
            "pair_id": "fwdffdasfvder",
            "start": timestamps["start"],
            "end": timestamps["end"]
        }
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid pair_id format."}
    

def test_get_stat_pair_not_exist(test_app):
    # test "/stat" route with not existing pair_id
    timestamps = create_timestamps(1, 0)
    response = test_app.post(
        "/stat",
        json={
            "pair_id": str(ObjectId()),
            "start": timestamps["start"],
            "end": timestamps["end"]
        }
    )
    assert response.status_code == 404
    assert response.json() == {"detail": "No such pair."}
    