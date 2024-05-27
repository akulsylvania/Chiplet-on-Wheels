# Use the official Ubuntu 16.04 image as the base image
FROM ubuntu:16.04

# Update the package list and install necessary packages
RUN apt-get update && \
    apt-get install -y \
    build-essential \
    git \
    m4 \
    scons \
    zlib1g \
    zlib1g-dev \
    libprotobuf-dev \
    protobuf-compiler \
    libprotoc-dev \
    libgoogle-perftools-dev \
    python-dev \
    python

# Clean up unnecessary files to reduce the image size
RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory to /pwd
WORKDIR /pwd

# Entry point (optional)
CMD ["/bin/bash"]
