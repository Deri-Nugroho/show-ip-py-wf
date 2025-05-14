# Dockerfile.dev - Untuk development dengan hot-reload
FROM python:3.9-slim

WORKDIR /app

# Clone repo GitHub
RUN apt-get update && apt-get install -y git \
    && git clone https://github.com/dihkaw/showipserverwithpython.git /app \
    && rm -rf /var/lib/apt/lists/*

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt \
    && pip install watchdog

# Expose port
EXPOSE 5000

# Jalankan dengan hot-reload
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000", "--reload"]
