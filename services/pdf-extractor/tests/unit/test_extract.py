from pathlib import Path

from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

FIXTURES = Path(__file__).resolve().parent.parent / "fixtures"
PDF_FILE = FIXTURES / "sample.pdf"


def test_extract_pdf():
    with open(PDF_FILE, "rb") as pdf:
        response = client.post(
            "/extract",
            files={
                "file": (
                    "sample.pdf",
                    pdf,
                    "application/pdf",
                )
            },
        )

    assert response.status_code == 200

    body = response.json()

    assert body["success"] is True
    assert body["pages"] >= 1
    assert body["characters"] > 0
    assert len(body["text"]) > 0

    # Validación del contenido esperado
    assert len(body["text"]) > 100
    assert "FastAPI" in body["text"]
