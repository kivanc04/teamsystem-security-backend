from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_and_list_events():
    payload = {
        "event_type": "auth_failed",
        "source_ip": "203.0.113.10",
        "user_id": "user_123",
        "details": "invalid password"
    }

    r1 = client.post("/events", json=payload)
    assert r1.status_code == 200
    body = r1.json()
    assert body["id"] >= 1
    assert body["event_type"] == "auth_failed"

    r2 = client.get("/events")
    assert r2.status_code == 200
    events = r2.json()
    assert len(events) >= 1
