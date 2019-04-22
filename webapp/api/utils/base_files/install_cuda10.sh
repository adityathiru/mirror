#!/bin/bash
echo "Checking for CUDA10 and installing."
# Check for CUDA10 and try to install.
if ! dpkg-query -W cuda-10-0; then
  # The 16.04 installer works with 16.10.
  curl -O http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/cuda-repo-ubuntu1604_10.0.130-1_amd64.deb
  dpkg -i ./cuda-repo-ubuntu1604_10.0.130-1_amd64.deb
  apt-key adv --fetch-keys http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/7fa2af80.pub
  apt-get update
  apt-get install cuda-10-0 -y
fi

# Enable persistence mode
nvidia-smi -pm 1
