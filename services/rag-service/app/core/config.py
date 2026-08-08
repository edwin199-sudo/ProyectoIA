from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "ProyectoIA RAG Service"
    APP_VERSION: str = "1.0.0"

    OLLAMA_HOST: str = "http://ollama:11434"
    EMBEDDING_MODEL: str = "nomic-embed-text"
    CHAT_MODEL: str = "qwen2.5:7b"

    QDRANT_HOST: str = "qdrant"
    QDRANT_PORT: int = 6333
    QDRANT_COLLECTION: str = "documents"

    DEFAULT_TOP_K: int = 5

    CHUNK_SIZE: int = 500
    CHUNK_OVERLAP: int = 100

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()
