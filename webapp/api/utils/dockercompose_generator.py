import os
import yaml
from collections import OrderedDict 


class DockerComposeGenerator:
    def __init__(self, path, requirements_dict):
        self.path = path
        self.requirements_dict = requirements_dict

    def create_dockercompose(self):
        pass

    def generate_dockercompose(self, data):
        path_to_dockercompose = os.path.join(self.path, 'docker-compose.yml')
        with open(path_to_dockercompose, 'w+') as f:
            yaml.dump(dict(data), f, default_flow_style=False)


if __name__ == '__main__':
    requirements_dict = {'project_name': 'project_mark1', 'python_version': 'python2', 'primary_architecture': 'cpu',
                         'dl_frameworks': ['pytorch', 'tensorflow'],
                         'pylibs': ['numpy', 'scipy', 'pandas', 'matplotlib', 'scikit-learn'],
                         'project_path': '/Users/aditya/Personal/projects/mirror/editor'}
    data = {
        'version': '2.0',
        'services': {
            "webapp": {
                  "build": {"context": "webapp/"},
                  "image": "projectmirror/webapp:1.0",
                  "volumes": [
                      "./webapp:/webapp",
                      "./webapp/data:/var/lib/data"],
                  'ports': ['8000:8000'],
                  "networks": ["elk"],
                  "restart": "on-failure"
            },
        }
    }

    dockercompose_generator = DockerComposeGenerator('./', requirements_dict)
    dockercompose_generator.generate_dockercompose(data)
