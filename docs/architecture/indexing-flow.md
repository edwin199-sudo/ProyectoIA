# Flujo de Indexación

```mermaid
flowchart TD

A[PDF]

B[PDF Extractor]

C[Chunk API]

D[Embedding API]

E[Index API]

F[(Qdrant)]

A --> B

B --> C

C --> D

D --> E

E --> F
```
