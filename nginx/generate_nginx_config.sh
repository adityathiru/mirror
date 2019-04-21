#!/usr/bin/env bash

# TODO: Need to move this to environment settings.
FILE="/etc/nginx/conf.d/default.conf"

DEFAULT_ADDRESS="localhost"
DEFAULT_PORT=8000

cat > $FILE << EOF
server {
  listen 443;
  listen [::]:443;

  server_name localhost;
  return 301 http://\$host\$request_uri;
}

server {
    listen       80;
    listen [::]:80;

    server_name  localhost;
    rewrite ^/backend/(.*)$ /\$1;
    proxy_read_timeout 600s;
    client_max_body_size 10m;

    location / {
        proxy_pass http://$DEFAULT_ADDRESS:$DEFAULT_PORT;
    }

    error_page   500 502 503 504  /50x.html;
    location = /50x.html {
        root   /usr/share/nginx/html;
    }
}
EOF

# Stopping nginx daemon
nginx -g "daemon off;"
