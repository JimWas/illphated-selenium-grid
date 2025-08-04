FROM python:3.11-slim

# Install netcat so we can wait for Selenium Hub
RUN apt-get update && apt-get install -y netcat-openbsd && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /tests

# Install Selenium
RUN pip install --no-cache-dir selenium

# Copy project files
COPY . /tests

# Default command (will be overridden in docker-compose)
CMD ["python", "test_script.py"]
