from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_create_event(client):
    payload = {
        "event_type": "auth_failed",
        "source_ip": "1.1.1.1",
        "user_id": "u-test",
        "details": "invalid password",
    }

    response = client.post("/events", json=payload)
    assert response.status_code == 200
    assert response.json()["event_type"] == "auth_failed"
    assert "id" in response.json()


def test_list_events(client):
    # önce bir event ekle
    payload = {
        "event_type": "auth_failed",
        "source_ip": "2.2.2.2",
        "user_id": "u-test-2",
        "details": "wrong otp",
    }
    client.post("/events", json=payload)

    response = client.get("/events")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) >= 1

