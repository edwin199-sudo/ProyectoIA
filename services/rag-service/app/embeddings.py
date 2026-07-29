import ollama

MODEL = "nomic-embed-text"


def generate_embedding(text: str):

    response = ollama.embeddings(
        model=MODEL,
        prompt=text
    )

    return response["embedding"]