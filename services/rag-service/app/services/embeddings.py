from app.core.config import settings
from ollama import Client

client = Client(
    host=settings.OLLAMA_HOST,
)

MODEL = settings.EMBEDDING_MODEL


def generate_embedding(text: str) -> list[float]:
    response = client.embed(
        model=MODEL,
        input=text,
    )

    return response["embeddings"][0]
