# Imagen base con soporte para FastAPI y Python
FROM python:3.10-slim

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    unzip \
    chromium \
    chromium-driver

# Crear directorio de la aplicación
WORKDIR /app

# Copiar archivos del proyecto
COPY . /app

# Instalar dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Comando de inicio
CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "app.main:app"]
