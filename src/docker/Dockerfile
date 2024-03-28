FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

# Update and install all required packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential cmake git pkg-config wget unzip curl \
    libgtk-3-dev libavcodec-dev libavformat-dev libswscale-dev libv4l-dev \
    libxvidcore-dev libx264-dev \
    libjpeg-dev libpng-dev libtiff-dev \
    libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev \
    gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly gstreamer1.0-libav \
    libatlas-base-dev liblapacke-dev \
    python3-dev python3-numpy python3-pip \
    libgstreamer1.0-0 gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly

# Clean apt cache to reduce image size
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Install code-server
RUN curl -fsSL https://code-server.dev/install.sh | sh

# Set environment variables for GUI applications (if needed)
ENV DISPLAY=host.docker.internal:0.0
ENV LD_LIBRARY_PATH=/usr/local/lib

WORKDIR /usr/src/app

EXPOSE 8080

# Ensure code-server is installed and check its version
RUN code-server --version

CMD ["code-server", "--auth", "none", "--bind-addr", "0.0.0.0:8080"]
