# Deployment Configuration for HTTPS

This document provides a sample configuration for deploying the Django application with Nginx and serving it over HTTPS.

## Prerequisites

1.  A server with Nginx and Gunicorn installed.
2.  A registered domain name pointing to the server's IP address.
3.  SSL/TLS certificates obtained from a Certificate Authority like Let's Encrypt. The certificate files (`fullchain.pem` and `privkey.pem`) are assumed to be in `/etc/letsencrypt/live/your.domain.com/`.

## Sample Nginx Configuration

Create a new Nginx server block configuration file at `/etc/nginx/sites-available/libraryproject`.

```nginx
# Server block to redirect all HTTP traffic to HTTPS
server {
    listen 80;
    server_name your.domain.com;
    return 301 https://$server_name$request_uri;
}

# Server block for handling HTTPS traffic
server {
    listen 443 ssl;
    server_name your.domain.com;

    # SSL Certificate Configuration
    ssl_certificate /etc/letsencrypt/live/your.domain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/your.domain.com/privkey.pem;

    # Improve SSL Security
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers HIGH:!aNULL:!MD5;

    # Static and Media files handling
    location /static/ {
        alias /path/to/your/project/staticfiles/;
    }

    location /media/ {
        alias /path/to/your/project/media/;
    }

    # Proxy requests to the Gunicorn/Django application
    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
}
```
