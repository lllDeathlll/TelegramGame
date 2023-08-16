# Use Ubuntu as the base image for the container
FROM ubuntu:latest

# Install python and packages
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    pip install aiogram

# Set the working directory inside the container
WORKDIR /app

# Copy the project files into the container
COPY . /app

# Start the bot
CMD ["python3", "main.py"]