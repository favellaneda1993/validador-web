FROM python:3.9-slim

# Evitar buffering de logs y asegurar UTF-8
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONIOENCODING=UTF-8

WORKDIR /app

# Instalar dependencias del sistema necesarias
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copiar dependencias e instalarlas
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código
COPY . .

# Puerto de Flask
ENV PORT=5000
EXPOSE 5000

# Comando de inicio con gunicorn (mejor para producción)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]

