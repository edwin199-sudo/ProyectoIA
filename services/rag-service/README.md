# RAG Service

Microservicio desarrollado con **FastAPI** encargado de implementar el núcleo de la plataforma **ProyectoIA**.

Este servicio procesa documentos mediante un pipeline **Retrieval-Augmented Generation (RAG)** que permite:

- Dividir documentos en fragmentos (Chunking).
- Generar embeddings utilizando Ollama.
- Indexar información en Qdrant.
- Realizar búsquedas semánticas.
- Recuperar el contexto más relevante para modelos LLM.

---

# Arquitectura

```text
Documento

↓

Chunking

↓

Embeddings (Ollama)

↓

Qdrant

↓

Semantic Search

↓

Context Retrieval

↓

LLM
```

---

# Características

- API REST con FastAPI
- Documentación automática (Swagger/OpenAPI)
- Chunking configurable
- Embeddings locales mediante Ollama
- Base de datos vectorial Qdrant
- Indexación de documentos
- Búsqueda semántica
- Preparado para integrarse con n8n
- Arquitectura basada en microservicios

---

# Tecnologías

- Python 3.12
- FastAPI
- Ollama
- Qdrant
- Docker
- Pydantic
- Uvicorn

---

# API

## GET /health

Verifica el estado del servicio.

### Respuesta

```json
{
    "success": true,
    "message": "RAG Service funcionando correctamente"
}
```

---

## POST /chunk

Divide un texto en fragmentos.

### Request

```json
{
    "text": "Contenido del documento...",
    "chunk_size": 500,
    "chunk_overlap": 100
}
```

### Response

```json
{
    "success": true,
    "total_chunks": 8,
    "chunks": [
        "...",
        "..."
    ]
}
```

---

## POST /embed

Genera embeddings utilizando Ollama.

### Request

```json
{
    "texts": [
        "Texto 1",
        "Texto 2"
    ]
}
```

### Response

```json
{
    "success": true,
    "embeddings": [
        [...],
        [...]
    ]
}
```

---

## POST /index

Indexa documentos dentro de Qdrant.

### Request

```json
{
    "texts": [
        "...",
        "..."
    ]
}
```

### Response

```json
{
    "success": true,
    "indexed_chunks": 8
}
```

---

## POST /search

Realiza una búsqueda semántica utilizando embeddings.

### Request

```json
{
    "query": "¿Qué experiencia tiene Edwin en Python?",
    "top_k": 5
}
```

### Response

```json
{
    "success": true,
    "results": [
        {
            "score": 0.71,
            "text": "...",
            "source": "Edwin_CV.pdf",
            "chunk_index": 2
        }
    ]
}
```

---

# Flujo RAG

```text
Documento PDF

↓

Texto

↓

Chunking

↓

Embeddings

↓

Qdrant

↓

Semantic Search

↓

Contexto

↓

LLM
```

---

# Integración con Ollama

Este servicio utiliza un modelo de embeddings ejecutándose localmente mediante Ollama.

Ejemplo:

```
nomic-embed-text
```

Los modelos conversacionales (por ejemplo `qwen2.5:7b`) son utilizados posteriormente por el AI Agent de n8n para generar la respuesta final.

---

# Integración con Qdrant

El servicio almacena cada fragmento del documento como un vector de alta dimensión junto con sus metadatos.

Cada punto contiene:

- embedding
- texto
- documento origen
- índice del fragmento

Esto permite realizar búsquedas semánticas extremadamente rápidas.

---

# Integración con n8n

Este microservicio es utilizado por los siguientes workflows:

- 03 – Indexador RAG
- 04 – Chat RAG

---

# Variables de entorno

| Variable | Descripción |
|----------|-------------|
| OLLAMA_BASE_URL | URL del servidor Ollama |
| QDRANT_URL | URL del servidor Qdrant |

---

# Ejecución local

```bash
uvicorn app.main:app --reload
```

Swagger

```
http://localhost:8001/docs
```

---

# Docker

Construcción

```bash
docker compose build rag-service
```

Inicio

```bash
docker compose up -d rag-service
```

---

# Próximas mejoras

- Batch Embeddings
- Metadata Filtering
- Hybrid Search
- Re-ranking
- Streaming Responses
- Multi-document Retrieval
- Evaluación automática del RAG
- Observabilidad y métricas

---

# Autor

Edwin Andrés Cataño Vanegas

ProyectoIA
