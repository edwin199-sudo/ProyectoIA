from fastapi import FastAPI

from app.schemas import HealthResponse

app = FastAPI(
    title="ProyectoIA RAG Service",
    version="1.0.0"
)


@app.get("/", response_model=HealthResponse)
def health():
    return HealthResponse(
        success=True,
        message="RAG Service funcionando correctamente"
    )