import os
from webapp.api.utils.installation import (add_nvidiadocker_support, install_deeplearning_frameworks)
from webapp.api.utils.tools import get_backend


class DockerFileGenerator:
    def __init__(self, path, requirements_dict):
        self.path = path
        self.requirements_dict = requirements_dict

    def create_dockerfile(self):
        lines_to_docker_file = []
        path_to_dockerfile = os.path.join(self.path, 'Dockerfile')
        path_to_requirements = os.path.join(self.path, 'requirements.txt')

        project_name = self.requirements_dict['project_name']

        # SETTING UP BASIC BASEIMAGE AND FILE STRUCTURE
        base_image = 'FROM projectmirror/{}:1.0'.format(project_name)
        working_dir = 'WORKDIR /{}'.format(project_name)
        copy_project_to_working_dir = 'COPY . /{}'.format(project_name)

        lines_to_docker_file.extend([base_image,
                                    working_dir,
                                    copy_project_to_working_dir])

        # SETTING UP NVIDIA-DOCKER FOR GPUs
        backend = get_backend(self.requirements_dict)
        if backend != 'cpu':
            docker_nvidia_commands_list = add_nvidiadocker_support(backend)
            lines_to_docker_file.extend(docker_nvidia_commands_list)

        # SETTING UP DEEP LEARNING FRAMEWORKS
        deeplearning_frameworks = self.requirements_dict['dl_frameworks']
        python_version = self.requirements_dict['python_version']

        docker_dl_frameworks_commands_list = install_deeplearning_frameworks(deeplearning_frameworks, python_version, backend)
        lines_to_docker_file.extend(docker_dl_frameworks_commands_list)

        if os.path.exists(path_to_requirements):
            if python_version == 'python2':
                pip_install_docker_command = 'RUN pip install - r requirements.txt'
            elif python_version == 'python3':
                pip_install_docker_command = 'RUN pip3 install -r requirements.txt'
            else:
                raise ValueError('Invalid Python Version: {}'.format(python_version))

            lines_to_docker_file.append(pip_install_docker_command)

        with open(path_to_dockerfile, 'w+') as f:
            f.writelines('\n'.join(lines_to_docker_file))

        return path_to_dockerfile


if __name__ == "__main__":
    requirements_dict = {'project_name': 'project_mark1', 'python_version': 'python2', 'primary_architecture': 'cpu',
                         'dl_frameworks': ['pytorch', 'tensorflow'],
                         'pylibs': ['numpy', 'scipy', 'pandas', 'matplotlib', 'scikit-learn'],
                         'project_path': '/Users/aditya/Personal/projects/mirror/editor'}

    dockerfile_generator = DockerFileGenerator('./', requirements_dict)
    dockerfile_generator.create_dockerfile()

