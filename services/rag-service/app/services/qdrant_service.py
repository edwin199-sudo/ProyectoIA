from uuid import uuid4

from app.core.config import settings
from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    PointStruct,
    VectorParams,
)

client = QdrantClient(
    host=settings.QDRANT_HOST,
    port=settings.QDRANT_PORT,
)

COLLECTION_NAME = settings.QDRANT_COLLECTION


def create_collection(vector_size: int):
    collections = client.get_collections().collections

    names = [c.name for c in collections]

    if COLLECTION_NAME not in names:
        client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(
                size=vector_size,
                distance=Distance.COSINE,
            ),
        )


def index_vectors(
    texts: list[str],
    vectors: list[list[float]],
):
    points = []

    for i, (text, vector) in enumerate(zip(texts, vectors, strict=False)):
        points.append(
            PointStruct(
                id=str(uuid4()),
                vector=vector,
                payload={
                    "text": text,
                    "source": "manual",
                    "chunk_index": i,
                },
            )
        )

    client.upsert(
        collection_name=COLLECTION_NAME,
        points=points,
    )


def search_vectors(
    vector: list[float],
    limit: int = settings.DEFAULT_TOP_K,
):
    response = client.query_points(
        collection_name=COLLECTION_NAME,
        query=vector,
        limit=limit,
    )

    return response.points
