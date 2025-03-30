# Use Ubuntu 20.04 as base image
FROM ubuntu:20.04  

# Install Python 3.9 and clean up cache
RUN apt-get update && apt-get install -y \
    python3.9 python3.9-venv python3.9-dev \
    && rm -rf /var/lib/apt/lists/*  

# Set default command
CMD ["python3"]
