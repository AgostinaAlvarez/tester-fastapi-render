# Usar una imagen base con Python
FROM python:3.11-slim

# Instalar dependencias del sistema necesarias (como Chromium y ChromeDriver)
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    unzip \
    chromium \
    chromium-driver

# Instalar las dependencias de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar los archivos del proyecto
COPY . /app
WORKDIR /app

# Exponer el puerto
EXPOSE 3000

# Comando para ejecutar la aplicación FastAPI con Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3000"]
