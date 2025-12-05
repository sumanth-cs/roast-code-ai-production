# FROM python:3.10-slim

# WORKDIR /app

# COPY requirements.txt .
# RUN pip install -r requirements.txt

# COPY backend ./backend

# EXPOSE 5001

# CMD ["python", "backend/app.py"]

# Dockerfile.backend - LIGHTWEIGHT
FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY backend ./backend

# Create non-root user
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

EXPOSE 5001

CMD ["python", "backend/app.py"]