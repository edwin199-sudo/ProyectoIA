@echo off
echo =====================================
echo Restarting ProyectoIA...
echo =====================================

cd /d %~dp0..
docker compose down
docker compose up -d

echo.
docker ps

echo.
echo ProyectoIA restarted.
pause
