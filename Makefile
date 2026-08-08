.PHONY: test lint format

test:
	cd services/pdf-extractor && pytest
	cd services/rag-service && pytest

lint:
	cd services/pdf-extractor && ruff check .
	cd services/rag-service && ruff check .

format:
	cd services/pdf-extractor && black .
	cd services/rag-service && black .s
