#!/bin/bash

# This script provides a set of functions to clean up Docker resources.
# It supports cleaning up Docker containers, images, volumes, and networks
# individually or all at once. The script uses command-line options to 
# determine which resources to clean up.
#
# Usage:
#   ./clear_docker.sh [-a | -c | -i | -v | -n]
#
# Options:
#   -a    Clean up all Docker containers, images, volumes, and networks
#   -c    Clean up Docker containers
#   -i    Clean up Docker images
#   -v    Clean up Docker volumes
#   -n    Clean up Docker networks
#
# Functions:
#   show_help        Displays the usage information for the script.
#   clean_containers Stops and removes all Docker containers.
#   clean_images     Removes all Docker images.
#   clean_volumes    Removes all Docker volumes.
#   clean_networks   Removes all Docker networks.
#
# The script parses the command-line arguments and executes the appropriate
# cleanup functions based on the provided options. If no valid options are
# provided, it displays the help information.



# Function to display help
function show_help() {
    echo "Usage: $0 [-a | -c | -i | -v | -n]"
    echo "Options:"
    echo "  -a    Clean up all Docker containers, images, volumes, and networks"
    echo "  -c    Clean up Docker containers"
    echo "  -i    Clean up Docker images"
    echo "  -v    Clean up Docker volumes"
    echo "  -n    Clean up Docker networks"
    exit 1
}

# Function to clean up Docker containers
function clean_containers() {
    docker stop $(docker ps -q)
    docker rm $(docker ps -aq)
    echo "Docker containers cleaned up!"
}

# Function to clean up Docker images
function clean_images() {
    docker rmi $(docker images -q)
    echo "Docker images cleaned up!"
}

# Function to clean up Docker volumes
function clean_volumes() {
    docker volume rm $(docker volume ls -q)
    echo "Docker volumes cleaned up!"
}

# Function to clean up Docker networks
function clean_networks() {
    docker network rm $(docker network ls -q)
    echo "Docker networks cleaned up!"
}

# Parse arguments
while getopts "acivn" opt; do
    case "$opt" in
        a) clean_all=true ;;
        c) clean_containers=true ;;
        i) clean_images=true ;;
        v) clean_volumes=true ;;
        n) clean_networks=true ;;
        *) show_help ;;
    esac
done

# Execute cleanup based on arguments
if [ "$clean_all" = true ]; then
    clean_containers
    clean_images
    clean_volumes
    clean_networks
elif [ "$clean_containers" = true ]; then
    clean_containers
elif [ "$clean_images" = true ]; then
    clean_images
elif [ "$clean_volumes" = true ]; then
    clean_volumes
elif [ "$clean_networks" = true ]; then
    clean_networks
else
    show_help
fi

