# Imagen base oficial de Python
FROM python:3.12-slim

# Evita generar archivos .pyc
ENV PYTHONDONTWRITEBYTECODE=1

# Muestra los logs inmediatamente
ENV PYTHONUNBUFFERED=1

# Carpeta de trabajo dentro del contenedor
WORKDIR /app

# Copiamos primero las dependencias
COPY requirements.txt .

# Instalamos dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el código de la aplicación
COPY app ./app

# Puerto que utilizará FastAPI
EXPOSE 8000

# Comando para iniciar el servidor
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
