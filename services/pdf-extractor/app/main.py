from fastapi import FastAPI

app = FastAPI(
    title="ProyectoIA - PDF Extractor",
    description="Microservicio para extraer texto de archivos PDF",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "status": "ok",
        "service": "pdf-extractor",
        "version": "1.0.0"
    }


@app.get("/health")
def health():
    return {
        "healthy": True
    }