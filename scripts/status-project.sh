#!/bin/bash

cd "$(dirname "$0")/.."

echo
echo "==========================="
echo "ProyectoIA Status"
echo "==========================="

docker compose ps
