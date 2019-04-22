SUPPORTED_CONFIGURATIONS = {
    'SUPPORTED_PYTHON_VERSIONS': {
        'python2': 'python2.7',
        'python3': 'python3.6'
    },
    'SUPPORTED_BACKEND': ['cpu', 'cuda8', 'cuda9', 'cuda10'],
    'SUPPORTED_GPU': ['cuda8', 'cuda9', 'cuda10'],
    'DEEP_LEARNING_FRAMEWORKS': {
        'pytorch': {
            'python2.7': {
                'cpu': {
                    'installation': 'torch'
                },
                'cuda8': {
                    'installation': 'https://download.pytorch.org/whl/cu80/torch-1.0.1.post2-cp27-cp27mu-linux_x86_64.whl'
                },
                'cuda9': {
                    'installation': 'torch'
                },
                'cuda10': {
                    'installation': 'https://download.pytorch.org/whl/cu100/torch-1.0.1.post2-cp27-cp27mu-linux_x86_64.whl'
                },
                'other_packages': ['torchvision', 'torchtext']
            },
            'python3.6': {
                'cpu': {
                    'installation': 'torch'
                },
                'cuda8': {
                    'installation': 'https://download.pytorch.org/whl/cu80/torch-1.0.1.post2-cp36-cp36m-linux_x86_64.whl'
                },
                'cuda9': {
                    'installation': 'torch'
                },
                'cuda10': {
                    'installation': 'https://download.pytorch.org/whl/cu100/torch-1.0.1.post2-cp36-cp36m-linux_x86_64.whl'
                },
                'other_packages': ['torchvision', 'torchtext', 'allennlp']
            }
        },
        'tensorflow': {
            'python2.7': {
                'cpu': {
                    'installation': 'tenforflow'
                },
                'cuda8': {
                    'installation': 'tenforflow-gpu'
                },
                'cuda9': {
                    'installation': 'tenforflow-gpu'
                },
                'cuda10': {
                    'installation': 'tenforflow-gpu'
                },
                'other_packages': []
            },
            'python3.6': {
                'cpu': {
                    'installation': 'tenforflow'
                },
                'cuda8': {
                    'installation': 'tensorflow'
                },
                'cuda9': {
                    'installation': 'tenforflow-gpu'
                },
                'cuda10': {
                    'installation': 'tenforflow-gpu'
                },
                'other_packages': []
            }
        }
    },
    'NVIDIA_DOCKER_INSTALLATION': {
        'installation': [
            'ENV PATH /usr/local/nvidia/bin/:$PATH',
            'ENV LD_LIBRARY_PATH /usr/local/nvidia/lib:/usr/local/nvidia/lib64',
            'ENV NVIDIA_VISIBLE_DEVICES all',
            'ENV NVIDIA_DRIVER_CAPABILITIES compute,utility',
            'LABEL com.nvidia.volumes.needed="nvidia_driver"'
        ]
    },
    'BACKEND_INSTALLATION': {
        'cuda8': {
            'installation': '/webapp/api/utils/base_files/install_cuda8.sh'
        },
        'cuda9': {
            'installation': '/webapp/api/utils/base_files/install_cuda9.sh'
        },
        'cuda10': {
            'installation': '/webapp/api/utils/base_files/install_cuda10.sh'
        },
        'nvidia-docker': {
            'installation': '/webapp/api/utils/base_files/install_nvidia-docker.sh'
        }
    }
}