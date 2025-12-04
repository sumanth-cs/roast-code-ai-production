# # # # # Dockerfile (if you want single container)
# # # # FROM python:3.10-slim

# # # # WORKDIR /app

# # # # # Install system dependencies
# # # # RUN apt-get update && apt-get install -y \
# # # #     gcc \
# # # #     g++ \
# # # #     curl \
# # # #     redis-server \
# # # #     && rm -rf /var/lib/apt/lists/*

# # # # # Copy requirements
# # # # COPY requirements.txt .
# # # # RUN pip install --no-cache-dir -r requirements.txt

# # # # # Copy all code
# # # # COPY . .

# # # # # Create non-root user
# # # # RUN useradd -m -u 1000 appuser
# # # # USER appuser

# # # # # Expose ports
# # # # EXPOSE 5001
# # # # EXPOSE 8501

# # # # # Start script
# # # # COPY start.sh .
# # # # RUN chmod +x start.sh

# # # # CMD ["./start.sh"]
# # # FROM python:3.10-slim

# # # WORKDIR /app

# # # RUN apt-get update && apt-get install -y \
# # #     curl \
# # #     && rm -rf /var/lib/apt/lists/*

# # # COPY requirements.txt .
# # # RUN pip install --no-cache-dir -r requirements.txt

# # # COPY . .

# # # # Simple start command - Render will set PORT=10000
# # # CMD ["sh", "-c", "if [ -d 'backend' ]; then cd backend && gunicorn --bind 0.0.0.0:10000 --workers 2 app:app & fi; if [ -d 'frontend' ]; then cd frontend && streamlit run app.py --server.port 8501 --server.address 0.0.0.0 & fi; wait"]

# # FROM python:3.10-slim

# # WORKDIR /app

# # RUN apt-get update && apt-get install -y \
# #     curl \
# #     && rm -rf /var/lib/apt/lists/*

# # COPY requirements.txt .
# # RUN pip install --no-cache-dir -r requirements.txt

# # COPY . .

# # CMD ["sh", "-c", "cd backend && gunicorn --bind 0.0.0.0:$PORT --workers 2 app:app & cd frontend && streamlit run app.py --server.port 8501 --server.address 0.0.0.0 && wait"]

# FROM python:3.10-slim

# WORKDIR /app

# # Install minimal dependencies
# RUN apt-get update && apt-get install -y \
#     curl \
#     && rm -rf /var/lib/apt/lists/*

# # Copy requirements first
# COPY requirements.txt .

# # Install Python packages
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy all code
# COPY . .

# # Create startup script
# RUN echo '#!/bin/bash\n\
# \n\
# echo "Starting services on port: $PORT"\n\
# \n\
# # Start backend\n\
# cd backend && gunicorn --bind 0.0.0.0:$PORT --workers 1 app:app &\n\
# \n\
# # Start frontend\n\
# cd frontend && streamlit run app.py --server.port 8501 --server.address 0.0.0.0 &\n\
# \n\
# # Keep container running\n\
# wait\n' > /app/start.sh && chmod +x /app/start.sh

# EXPOSE 10000

# CMD ["/app/start.sh"]

# Dockerfile - FIXED FOR RAILWAY
FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    nginx \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements FIRST for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy all code
COPY . .

# Configure nginx as reverse proxy
RUN echo 'events {}\n\
http {\n\
    server {\n\
        listen $PORT;\n\
        \n\
        # Backend API\n\
        location /api/ {\n\
            proxy_pass http://localhost:5001/;\n\
            proxy_set_header Host $host;\n\
            proxy_set_header X-Real-IP $remote_addr;\n\
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;\n\
        }\n\
        \n\
        # Streamlit frontend\n\
        location / {\n\
            proxy_pass http://localhost:8501/;\n\
            proxy_set_header Host $host;\n\
            proxy_set_header X-Real-IP $remote_addr;\n\
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;\n\
            proxy_http_version 1.1;\n\
            proxy_set_header Upgrade $http_upgrade;\n\
            proxy_set_header Connection "upgrade";\n\
        }\n\
    }\n\
}' > /etc/nginx/nginx.conf

# Create startup script
RUN echo '#!/bin/bash\n\
set -e\n\
\n\
echo "Starting Roast Code AI..."\n\
echo "PORT: $PORT"\n\
\n\
# Export PORT for nginx config\n\
export PORT=${PORT:-10000}\n\
\n\
# Start Flask backend\n\
cd /app/backend && gunicorn --bind 0.0.0.0:5001 --workers 1 --timeout 120 app:app &\n\
\n\
# Start Streamlit frontend\n\
cd /app/frontend && streamlit run app.py \\\n\
    --server.port=8501 \\\n\
    --server.address=0.0.0.0 \\\n\
    --server.headless=true \\\n\
    --browser.gatherUsageStats=false \\\n\
    --server.enableCORS=false \\\n\
    --server.enableXsrfProtection=false &\n\
\n\
# Start nginx with the right port\n\
envsubst < /etc/nginx/nginx.conf > /etc/nginx/nginx.conf.tmp && mv /etc/nginx/nginx.conf.tmp /etc/nginx/nginx.conf\n\
nginx -g "daemon off;" &\n\
\n\
# Keep container running\n\
wait\n' > /app/start.sh && chmod +x /app/start.sh

# Install envsubst
RUN apt-get update && apt-get install -y gettext-base && rm -rf /var/lib/apt/lists/*

EXPOSE 10000

CMD ["/app/start.sh"]