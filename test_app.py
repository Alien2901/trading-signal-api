from fastapi.testclient import TestClient
from app_final import app

client = TestClient(app)

def test_read_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "OK", "message": "Trading API is running smoothly"}

def test_read_version():
    response = client.get("/version")
    assert response.status_code == 200
    assert "version" in response.json()

def test_read_signal():
    response = client.get("/signal/btc")
    assert response.status_code == 200
    data = response.json()
    assert data["ticker"] == "BTC"
    assert data["recommendation"] in ["BUY", "SELL", "HOLD"]
