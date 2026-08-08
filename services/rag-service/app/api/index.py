from app.models.schemas import (
    IndexRequest,
    IndexResponse,
)
from app.services.embeddings import generate_embedding
from app.services.qdrant_service import (
    create_collection,
    index_vectors,
)
from fastapi import APIRouter

router = APIRouter(tags=["Index"])


@router.post("/index", response_model=IndexResponse)
def index(request: IndexRequest):
    vectors = [generate_embedding(text) for text in request.texts]

    create_collection(vector_size=len(vectors[0]))

    index_vectors(
        texts=request.texts,
        vectors=vectors,
    )

    return IndexResponse(
        success=True,
        indexed_chunks=len(vectors),
    )
