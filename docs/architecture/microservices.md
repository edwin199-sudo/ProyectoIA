# Microservicios

```mermaid
graph LR

subgraph Docker

N8N[n8n]

PDF[pdf-extractor]

RAG[rag-service]

Q[(Qdrant)]

O[Ollama]

P[(PostgreSQL)]

end

N8N --> PDF

N8N --> RAG

RAG --> O

RAG --> Q

N8N --> P
```
