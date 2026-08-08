def test_embed(client):
    payload = {
        "texts": [
            "ProyectoIA es una plataforma RAG.",
            "FastAPI funciona con Ollama.",
        ]
    }

    response = client.post("/embed", json=payload)

    assert response.status_code == 200

    body = response.json()

    assert body["success"] is True

    assert len(body["embeddings"]) == 2

    for embedding in body["embeddings"]:
        assert isinstance(embedding, list)

        assert len(embedding) > 0

        assert all(isinstance(value, float | int) for value in embedding)
