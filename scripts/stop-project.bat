@echo off
echo =====================================
echo Stopping ProyectoIA...
echo =====================================

cd /d %~dp0..
docker compose down

echo.
echo ProyectoIA stopped.
pause
