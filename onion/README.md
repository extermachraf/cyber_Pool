# Dockerized Tor Hidden Service with Nginx

This project sets up an anonymous website on the Tor network using Docker. It includes a Tor hidden service and an Nginx web server to serve a static webpage.

## Prerequisites

- Docker installed on your system.

# How to Run Dockerized Tor Hidden Service with Nginx

## Prerequisites

- Docker installed on your system.

## Building and Running the Docker Container

1. **Build the Docker Image:**

    ```bash
    docker build -t tor-nginx .
    ```

2. **Run the Docker Container:**

    ```bash
    docker run -d -p 80:80 --name tor-nginx-container tor-nginx
    ```

3. **Retrieve Your .onion Address:**

    To get the .onion address, access the `hostname` file inside the running container:

    ```bash
    docker exec tor-nginx-container cat /var/lib/tor/hidden_service/hostname
    ```

4. **Access Your Website via Tor Browser:**

    Use the .onion address retrieved in the previous step to access your website via the Tor Browser.