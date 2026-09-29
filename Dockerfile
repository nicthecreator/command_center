FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements
COPY requirements/ /app/requirements/

# Instalar dependências Python
RUN pip install --upgrade pip
RUN pip install -r requirements/local.txt

# O código fonte será mapeado via volume no docker-compose para desenvolvimento local
# COPY . /app/
