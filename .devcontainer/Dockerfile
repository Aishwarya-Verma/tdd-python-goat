FROM mcr.microsoft.com/devcontainers/python:1-3.12-bullseye

# Install Firefox and Geckodriver
RUN echo "===> Installing geckodriver and firefox..." && \
    apt-get update && \
    apt-get install -y firefox-esr wget unzip && \
    wget https://github.com/mozilla/geckodriver/releases/latest/download/geckodriver-linux64.tar.gz && \
    tar -xzf geckodriver-linux64.tar.gz -C /usr/local/bin && \
    chmod +x /usr/local/bin/geckodriver && \
    rm geckodriver-linux64.tar.gz
