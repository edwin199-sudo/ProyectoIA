def test_index(client):
    payload = {
        "texts": [
            "ProyectoIA utiliza FastAPI.",
            "ProyectoIA utiliza Ollama.",
            "ProyectoIA utiliza Qdrant.",
        ]
    }

    response = client.post("/index", json=payload)

    assert response.status_code == 200

    body = response.json()

    assert body["success"] is True
    assert body["indexed_chunks"] == len(payload["texts"])
