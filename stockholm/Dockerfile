# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app
RUN apt-get update && apt-get install -y make

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Create a directory for testing
RUN mkdir -p /root/infection

# Start a shell when the container launches
CMD ["bash"]