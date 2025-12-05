# FROM python:3.10-slim

# WORKDIR /app

# COPY requirements.txt .
# RUN pip install -r requirements.txt

# COPY backend ./backend

# EXPOSE 5001

# CMD ["python", "backend/app.py"]

# Dockerfile (for backend)
FROM python:3.10-slim

WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend code
COPY backend ./backend

# Create a simple wsgi.py if it doesn't exist
RUN echo "from app import app\n\nif __name__ == '__main__':\n    app.run(host='0.0.0.0', port=5001)" > /app/backend/wsgi.py

EXPOSE 5001

CMD ["python", "backend/app.py"]