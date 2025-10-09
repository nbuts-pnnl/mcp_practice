# Use Python 3.11 slim image as base
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better Docker layer caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Create logs directory
RUN mkdir -p logs

# Copy source code
COPY src/ ./src/

# Copy environment file
COPY .env.local .env

# Expose port (if needed for future HTTP transport)
EXPOSE 8000

# Run the MCP service
CMD ["fastapi", "dev", "src/mcp_service.py"]