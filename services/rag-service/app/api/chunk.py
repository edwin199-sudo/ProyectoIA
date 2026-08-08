from app.models.schemas import (
    ChunkRequest,
    ChunkResponse,
)
from app.services.chunker import split_text
from fastapi import APIRouter

router = APIRouter(tags=["Chunk"])


@router.post("/chunk", response_model=ChunkResponse)
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
