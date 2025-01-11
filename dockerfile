# Usar una imagen base con Python
FROM python:3.11-slim

# Instalar dependencias del sistema necesarias (como Chromium y ChromeDriver)
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    unzip \
    chromium \
    chromium-driver \
    libx11-xcb1 \
    libglib2.0-0 \
    libnss3 \
    libgdk-pixbuf2.0-0 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libgdk-x11-2.0-0 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    && apt-get clean

# Instalar las dependencias de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar los archivos del proyecto
COPY . /app
WORKDIR /app

# Establecer las variables de entorno para Chromium
ENV CHROME_BIN=/usr/bin/chromium
ENV CHROME_DRIVER=/usr/lib/chromium-driver/chromium-driver

# Exponer el puerto
EXPOSE 3000

# Comando para ejecutar la aplicación FastAPI con Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3000"]
