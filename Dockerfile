FROM python:3.11-slim

# Install dependencies for Chrome
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    fonts-liberation \
    libx11-xcb1 \
    libxcomposite1 \
    libxcursor1 \
    libxdamage1 \
    libxi6 \
    libxtst6 \
    libnss3 \
    libxrandr2 \
    libasound2 \
    libatk1.0-0 \
    libcups2 \
    libdbus-1-3 \
    libdrm2 \
    libgbm1 \
    libgtk-3-0 \
    libxss1 \
    xdg-utils \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

# Install Chrome
RUN wget -q -O /tmp/chrome.deb https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt-get install -y /tmp/chrome.deb && \
    rm /tmp/chrome.deb

# Install Selenium
RUN pip install --no-cache-dir selenium

# Set working directory
WORKDIR /app

# Copy our script
COPY load_illphated.py /app/

# Run script when container starts
CMD ["python", "load_illphated.py"]
