FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    tor \
    nginx \
    && apt-get clean

# Create hidden service directory and configure tor
RUN mkdir -p /var/lib/tor/hidden_service \
    && chown -R debian-tor:debian-tor /var/lib/tor/hidden_service \
    && chmod 700 /var/lib/tor/hidden_service
COPY ./src/torrc /etc/tor/torrc

# Configure nginx
COPY ./src/default.conf /etc/nginx/sites-available/default
COPY ./src/index.html /var/www/html/index.html

EXPOSE 80

CMD service tor start && nginx -g 'daemon off;'