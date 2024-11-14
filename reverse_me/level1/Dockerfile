FROM ubuntu:latest

# Enable multi-architecture support
RUN dpkg --add-architecture i386

# Update package lists and install required packages
RUN apt-get update && apt-get install -y gdb libc6:i386

# Copy the binary into the container
COPY level1 /level1

# Set the command to run gdb with the binary
# CMD ["gdb", "./level1"]