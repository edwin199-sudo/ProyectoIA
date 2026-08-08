from app.api.chunk import router as chunk_router
from app.api.embed import router as embed_router
from app.api.health import router as health_router
from app.api.index import router as index_router
from app.api.search import router as search_router
from app.core.config import settings
from fastapi import FastAPI

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)

app.include_router(health_router)
app.include_router(chunk_router)
app.include_router(embed_router)
app.include_router(index_router)
app.include_router(search_router)
