# Start from the official GitHub dev container image for Python
FROM mcr.microsoft.com/devcontainers/python:3.12

# Install browsers and drivers
RUN apt-get update && apt-get install -y \
    firefox-esr \
    chromium \
    chromium-driver \
    xvfb \
    libgtk-3-0 \
    libdbus-glib-1-2 \
    libnss3 \
    libxss1 \
    libasound2 \
    libxss1 \
    && rm -rf /var/lib/apt/lists/*

# Set environment variable for headless display
ENV DISPLAY=:99

# Set working directory
WORKDIR /workspace

# Copy and install Python dependencies
COPY ../requirements.txt /workspace/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Start Xvfb and bash when container starts
CMD ["sh", "-c", "Xvfb :99 -screen 0 1024x768x24 & exec bash"]
