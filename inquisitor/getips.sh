#!/bin/bash

# Function to get the primary IP address of the host
get_ip() {
    ip addr show | grep 'inet ' | grep -v '127.0.0.1' | awk '{print $2}' | cut -d/ -f1 | head -n 1
}

# Function to get the primary MAC address of the host
get_mac() {
    ip link show | grep 'link/ether' | awk '{print $2}' | head -n 1
}

# Function to get the MAC address of a given IP
get_target_mac() {
    local container_name=$1
    docker exec $container_name cat /sys/class/net/eth0/address
}

# Get the source IP and MAC address
IP_SRC=$(get_ip)
MAC_SRC=$(get_mac)

# Simulate target IP and MAC address (you can replace these with actual values)
IP_TARGET="192.168.1.10"
CONTAINER_NAME="victim"

# Get the MAC address of the target container
MAC_TARGET=$(get_target_mac $CONTAINER_NAME)

# Print the gathered information
echo "Source IP: $IP_SRC"
echo "Source MAC: $MAC_SRC"
echo "Target IP: $IP_TARGET"
echo "Target MAC: $MAC_TARGET"

# Check if the target MAC address was found
if [ -z "$MAC_TARGET" ]; then
    echo "Failed to retrieve the MAC address for the target container $CONTAINER_NAME."
    echo "Please ensure the container is running and try again."
else
    echo "Successfully retrieved the MAC address for the target container $CONTAINER_NAME."
fi