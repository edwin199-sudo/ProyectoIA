from pydantic import BaseModel


class HealthResponse(BaseModel):
    success: bool
    message: str


class ChunkRequest(BaseModel):
    text: str
    chunk_size: int = 500
    chunk_overlap: int = 100


class ChunkResponse(BaseModel):
    success: bool
    total_chunks: int
    chunks: list[str]

class EmbedRequest(BaseModel):
    texts: list[str]


class EmbedResponse(BaseModel):
    success: bool
    embeddings: list[list[float]]

class IndexRequest(BaseModel):
    texts: list[str]


class IndexResponse(BaseModel):
    success: bool
    indexed_chunks: int

