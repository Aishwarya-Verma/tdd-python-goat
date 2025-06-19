FROM mcr.microsoft.com/devcontainers/python:1-3.12-bullseye

# Install Firefox (no manual geckodriver)
RUN echo "===> Installing firefox..." && \
    apt-get update && \
    apt-get install -y firefox-esr wget unzip
