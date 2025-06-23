FROM mcr.microsoft.com/devcontainers/python:1-3.12-bullseye

# Install browsers and drivers from Debian packages
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
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY ../requirements.txt /workspace/requirements.txt
RUN pip install --no-cache-dir -r /workspace/requirements.txt

WORKDIR /workspace
ENV DISPLAY=:99

# Start Xvfb headless display
CMD ["sh", "-c", "Xvfb :99 -screen 0 1024x768x24 & exec bash"]
