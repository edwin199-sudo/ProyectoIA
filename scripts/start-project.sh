#!/bin/bash

echo "==========================="
echo "Starting ProyectoIA..."
echo "==========================="

cd "$(dirname "$0")/.."

docker compose up -d

docker ps

echo
echo "ProyectoIA started."
