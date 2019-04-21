FROM klarity/nginx:1.0

RUN apt-get clean && apt-get update --fix-missing && \
    apt-get install -y build-essential vim

RUN mkdir -p /etc/ssl/private

WORKDIR /nginx

COPY . /nginx

EXPOSE 80
EXPOSE 443

STOPSIGNAL SIGTERM

ENTRYPOINT bash /nginx/generate_nginx_config.sh