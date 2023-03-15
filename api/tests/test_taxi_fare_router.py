import json
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from api.main import app
from api.models.taxi_fare_model import TaxiFareModel
from api.models.schemas import TaxiFareCreate

client = TestClient(app)

def test_create_taxi_fare_success(mocked_session: Session, test_app_with_db: TestClient):
    taxi_fare_data = {"distance": 5.0, "duration": 15, "fare": 25.0}
    response = test_app_with_db.post("/taxi_fares", json=taxi_fare_data)

    assert response.status_code == 201
    assert response.json()["distance"] == taxi_fare_data["distance"]
    assert response.json()["duration"] == taxi_fare_data["duration"]
    assert response.json()["fare"] == taxi_fare_data["fare"]

def test_create_taxi_fare_failure(mocked_session: Session, test_app_with_db: TestClient):
    taxi_fare_data = {"distance": 5.0, "duration": 15, "fare": "invalid"}
    response = test_app_with_db.post("/taxi_fares", json=taxi_fare_data)

    assert response.status_code == 422

def test_read_taxi_fare_success(test_app_with_db: TestClient, mocked_taxi_fare: TaxiFareModel):
    response = test_app_with_db.get(f"/taxi_fares/{mocked_taxi_fare.id}")

    assert response.status_code == 200
    assert response.json()["id"] == mocked_taxi_fare.id
    assert response.json()["distance"] == mocked_taxi_fare.distance
    assert response.json()["duration"] == mocked_taxi_fare.duration
    assert response.json()["fare"] == mocked_taxi_fare.fare

def test_read_taxi_fare_failure(test_app_with_db: TestClient):
    response = test_app_with_db.get("/taxi_fares/99999")

    assert response.status_code == 404

def test_update_taxi_fare_success(mocked_session: Session, test_app_with_db: TestClient, mocked_taxi_fare: TaxiFareModel):
    taxi_fare_update_data = {"distance": 8.0, "duration": 20, "fare": 32.0}
    response = test_app_with_db.put(f"/taxi_fares/{mocked_taxi_fare.id}", json=taxi_fare_update_data)

    assert response.status_code == 200
    assert response.json()["id"] == mocked_taxi_fare.id
    assert response.json()["distance"] == taxi_fare_update_data["distance"]
    assert response.json()["duration"] == taxi_fare_update_data["duration"]
    assert response.json()["fare"] == taxi_fare_update_data["fare"]

def test_update_taxi_fare_failure(test_app_with_db: TestClient):
    taxi_fare_update_data = {"distance": 8.0, "duration": 20, "fare": 32.0}
    response = test_app_with_db.put("/taxi_fares/99999", json=taxi_fare_update_data)

    assert response.status_code == 404

def test_delete_taxi_fare_success(test_app_with_db: TestClient, mocked_taxi_fare: TaxiFareModel):
    response = test_app_with_db.delete(f"/taxi_fares/{mocked_taxi_fare.id}")

    assert response.status_code == 204

def test_delete_taxi_fare_failure(test_app_with_db: TestClient):
    response = test_app_with_db.delete("/taxi_fares/99999")

    assert response.status_code == 404

def test_read_all_taxi_fares(test_app_with_db: TestClient):
    response = test_app_with_db.get("/taxi_fares")

    assert response.status_code == 200
    assert isinstance(response.json(), list)
