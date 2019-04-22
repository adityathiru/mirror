ARG ELK_VERSION

# https://github.com/elastic/elasticsearch-docker
FROM docker.elastic.co/elasticsearch/elasticsearch-oss:${ELK_VERSION}

USER root
RUN chown elasticsearch:elasticsearch /usr/share/elasticsearch/data

USER elasticsearch

# Add your elasticsearch plugins setup here
# Example: RUN elasticsearch-plugin install analysis-icu
