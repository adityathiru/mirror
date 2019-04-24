#!/usr/bin/env bash
curl -fsSL https://get.docker.com -o get-docker.sh
./get-docker.sh
sudo usermod -aG docker $USER