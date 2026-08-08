from app.models.schemas import HealthResponse
from fastapi import APIRouter

router = APIRouter(tags=["Health"])


@router.get("/health", response_model=HealthResponse)
def health():
    return HealthResponse(
        success=True,
        message="RAG Service funcionando correctamente",
    )
