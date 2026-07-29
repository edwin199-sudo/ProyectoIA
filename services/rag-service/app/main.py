from fastapi import FastAPI

from app.chunker import split_text
from app.embeddings import generate_embedding
from app.qdrant_service import create_collection

from app.schemas import (
    ChunkRequest,
    ChunkResponse,
    EmbedRequest,
    EmbedResponse,
    HealthResponse,
    IndexRequest,
    IndexResponse,
)

app = FastAPI(
    title="ProyectoIA RAG Service",
    version="1.0.0",
)


@app.get("/", response_model=HealthResponse)
def health():
    return HealthResponse(
        success=True,
        message="RAG Service funcionando correctamente",
    )


@app.post("/chunk", response_model=ChunkResponse)
def chunk(request: ChunkRequest):

    chunks = split_text(
        request.text,
        chunk_size=request.chunk_size,
        chunk_overlap=request.chunk_overlap,
    )

    return ChunkResponse(
        success=True,
        total_chunks=len(chunks),
        chunks=chunks,
    )

@app.post("/embed", response_model=EmbedResponse)
def embed(request: EmbedRequest):

    vectors = [
        generate_embedding(text)
        for text in request.texts
    ]

    return EmbedResponse(
        success=True,
        embeddings=vectors,
    )

@app.post("/index", response_model=IndexResponse)
def index(request: IndexRequest):

    vectors = [
        generate_embedding(text)
        for text in request.texts
    ]

    create_collection(
        vector_size=len(vectors[0])
    )

    return IndexResponse(
        success=True,
        indexed_chunks=len(vectors),
    )

