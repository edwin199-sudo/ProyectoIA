@echo off
echo =====================================
echo Starting ProyectoIA...
echo =====================================

cd /d %~dp0..
docker compose up -d

echo.
docker ps

echo.
echo ProyectoIA is running!
pause
