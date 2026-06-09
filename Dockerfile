# Use a more recent, stable slim image
FROM python:3.11-slim-bookworm

# Install system dependencies and clean up in the same layer
RUN apt-get update -y && \
    apt-get install -y --no-install-recommends awscli && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . .

# Copy only requirements first to leverage Docker layer caching
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY . .

# Run your application
CMD ["python3", "app.py"]