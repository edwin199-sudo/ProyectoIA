#!/bin/bash

echo "Restarting ProyectoIA..."

cd "$(dirname "$0")/.."

docker compose down

docker compose up -d

docker ps

echo
echo "ProyectoIA restarted."
