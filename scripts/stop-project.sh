#!/bin/bash

echo "Stopping ProyectoIA..."

cd "$(dirname "$0")/.."

docker compose down

echo "ProyectoIA stopped."
