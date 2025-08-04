# Use slim Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /tests

# Install Selenium
RUN pip install --no-cache-dir selenium

# Copy all project files into container
COPY . /tests

# Default command (can be overridden in docker-compose.yml)
CMD ["python", "test_script.py"]
