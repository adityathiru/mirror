ARG ELK_VERSION

# https://github.com/elastic/elasticsearch-docker
FROM docker.elastic.co/elasticsearch/elasticsearch-oss:${ELK_VERSION}

USER root
RUN chown root:root /usr/share/elasticsearch/data

USER root

# Add your elasticsearch plugins setup here
# Example: RUN elasticsearch-plugin install analysis-icu
