from app.models.schemas import (
    EmbedRequest,
    EmbedResponse,
)
from app.services.embeddings import generate_embedding
from fastapi import APIRouter

router = APIRouter(tags=["Embedding"])


@router.post("/embed", response_model=EmbedResponse)
def embed(request: EmbedRequest):
    vectors = [generate_embedding(text) for text in request.texts]

    return EmbedResponse(
        success=True,
        embeddings=vectors,
    )
