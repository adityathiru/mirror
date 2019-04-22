#!/usr/bin/env bash

docker-compose -f docker-compose-dev.yml down
docker build -t projectmirror/baseimage:1.0 baseimage/
docker-compose -f docker-compose-dev.yml build
docker-compose -f docker-compose-dev.yml up
