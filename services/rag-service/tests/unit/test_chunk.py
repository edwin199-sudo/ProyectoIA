def test_chunk(client):
    payload = {
        "text": (
            "ProyectoIA es una plataforma RAG desarrollada con FastAPI, "
            "Docker, Ollama y Qdrant para procesamiento de documentos."
        ),
        "chunk_size": 50,
        "chunk_overlap": 10,
    }

    response = client.post("/chunk", json=payload)

    assert response.status_code == 200

    body = response.json()

    assert body["success"] is True
    assert body["total_chunks"] > 0
    assert isinstance(body["chunks"], list)
    assert len(body["chunks"]) == body["total_chunks"]

    for chunk in body["chunks"]:
        assert isinstance(chunk, str)
        assert len(chunk) > 0
