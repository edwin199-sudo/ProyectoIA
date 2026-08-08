from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_search():
    payload = {"query": "Documento", "top_k": 3}

    response = client.post("/search", json=payload)

    assert response.status_code == 200

    body = response.json()

    assert body["success"] is True

    assert isinstance(body["results"], list)
