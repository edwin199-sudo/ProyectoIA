# PDF Extractor Service

Microservicio desarrollado con **FastAPI** encargado de extraer texto desde documentos PDF.

Este servicio forma parte de la plataforma **ProyectoIA** y constituye el primer paso del pipeline RAG.

---

# Funcionalidades

- Extracción de texto desde archivos PDF.
- Conteo de páginas.
- Conteo de caracteres.
- API REST basada en FastAPI.
- Documentación automática con Swagger.
- Preparado para ejecutarse mediante Docker.

---

# Arquitectura

PDF

↓

FastAPI

↓

PyMuPDF (fitz)

↓

Texto plano

---

# Tecnologías

- Python 3.12
- FastAPI
- PyMuPDF
- Uvicorn
- Docker

---

# Endpoints

## GET /health

Verifica el estado del servicio.

Respuesta

```json
{
    "success": true,
    "message": "PDF Extractor funcionando correctamente"
}
```

---

## POST /extract

Recibe un archivo PDF y devuelve:

- número de páginas
- número de caracteres
- texto extraído

Ejemplo de respuesta

```json
{
    "success": true,
    "pages": 12,
    "characters": 5487,
    "text": "Contenido del documento..."
}
```

---

# Ejecución local

```bash
uvicorn app.main:app --reload
```

Swagger

```
http://localhost:8000/docs
```

---

# Docker

Construcción

```bash
docker compose build pdf-extractor
```

Inicio

```bash
docker compose up -d pdf-extractor
```

---

# Rol dentro de ProyectoIA

Este servicio corresponde a la primera etapa del pipeline RAG:

PDF

↓

Extracción de texto

↓

Chunking

↓

Embeddings

↓

Base vectorial

↓

Búsqueda semántica

---

# Autor

Edwin Andrés Cataño Vanegas

ProyectoIA
