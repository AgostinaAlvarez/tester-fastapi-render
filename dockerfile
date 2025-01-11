# Usamos una imagen base con Python 3
FROM python:3.11-slim

# Instalamos dependencias del sistema necesarias (como Chromium y ChromeDriver)
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    unzip \
    chromium \
    chromium-driver

# Definir el directorio de trabajo
WORKDIR /app

# Copiar archivos del proyecto
COPY . /app

# Instalar las dependencias de Python desde requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto que utilizará FastAPI
EXPOSE 8000

# Configurar el comando de inicio para usar gunicorn y uvicorn
CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "app.main:app"]
