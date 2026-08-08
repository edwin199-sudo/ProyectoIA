from app.models.schemas import (
    SearchRequest,
    SearchResponse,
    SearchResult,
)
from app.services.embeddings import generate_embedding
from app.services.qdrant_service import search_vectors
from fastapi import APIRouter

router = APIRouter(tags=["Search"])


@router.post("/search", response_model=SearchResponse)
def search(request: SearchRequest):
    query_vector = generate_embedding(request.query)

    results = search_vectors(
        vector=query_vector,
        limit=request.top_k,
    )

    response = []

    for item in results:
        response.append(
            SearchResult(
                score=item.score,
                text=item.payload["text"],
                source=item.payload["source"],
                chunk_index=item.payload["chunk_index"],
            )
        )

    return SearchResponse(
        success=True,
        results=response,
    )
