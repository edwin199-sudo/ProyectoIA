#!/usr/bin/env bash

set -e

case "$1" in
  test)
    echo "==> Running PDF Extractor tests..."
    (
      cd services/pdf-extractor
      pytest
    )

    echo "==> Running RAG Service tests..."
    (
      cd services/rag-service
      pytest
    )
    ;;

  lint)
    echo "==> Running Ruff..."

    (
      cd services/pdf-extractor
      ruff check .
    )

    (
      cd services/rag-service
      ruff check .
    )
    ;;

  format)
    echo "==> Formatting with Black..."

    (
      cd services/pdf-extractor
      black .
    )

    (
      cd services/rag-service
      black .
    )
    ;;

  *)
    echo "Usage:"
    echo "./scripts/dev.sh test"
    echo "./scripts/dev.sh lint"
    echo "./scripts/dev.sh format"
    ;;
esac
