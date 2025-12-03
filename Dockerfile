# # # Dockerfile (if you want single container)
# # FROM python:3.10-slim

# # WORKDIR /app

# # # Install system dependencies
# # RUN apt-get update && apt-get install -y \
# #     gcc \
# #     g++ \
# #     curl \
# #     redis-server \
# #     && rm -rf /var/lib/apt/lists/*

# # # Copy requirements
# # COPY requirements.txt .
# # RUN pip install --no-cache-dir -r requirements.txt

# # # Copy all code
# # COPY . .

# # # Create non-root user
# # RUN useradd -m -u 1000 appuser
# # USER appuser

# # # Expose ports
# # EXPOSE 5001
# # EXPOSE 8501

# # # Start script
# # COPY start.sh .
# # RUN chmod +x start.sh

# # CMD ["./start.sh"]
# FROM python:3.10-slim

# WORKDIR /app

# RUN apt-get update && apt-get install -y \
#     curl \
#     && rm -rf /var/lib/apt/lists/*

# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# COPY . .

# # Simple start command - Render will set PORT=10000
# CMD ["sh", "-c", "if [ -d 'backend' ]; then cd backend && gunicorn --bind 0.0.0.0:10000 --workers 2 app:app & fi; if [ -d 'frontend' ]; then cd frontend && streamlit run app.py --server.port 8501 --server.address 0.0.0.0 & fi; wait"]

FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["sh", "-c", "cd backend && gunicorn --bind 0.0.0.0:$PORT --workers 2 app:app & cd frontend && streamlit run app.py --server.port 8501 --server.address 0.0.0.0 && wait"]