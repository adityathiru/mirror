import os
from webapp.utils.config import SUPPORTED_CONFIGURATIONS
from webapp.utils.tools import get_backend


class ExecutableGenerator:
    def __init__(self, path, requirements_dict):
        self.requirements_dict = requirements_dict
        self.path = path

    def generate_executable(self):
        backend = get_backend(self.requirements_dict)

        project_name = self.requirements_dict['project_name']
        path_to_executable = os.path.join(self.path, self.requirements_dict['project_name'])

        with open(path_to_executable, "w+") as output_file:
            output_file.write('#!/bin/bash\n')
            if backend != 'cpu':
                with open(SUPPORTED_CONFIGURATIONS["BACKEND_INSTALLATION"][backend]["installation"]) as install_commands:
                    output_file.write("cat > install_cuda.sh <<EOF\n")
                    while install_commands.readline():
                        output_file.write(install_commands.readline())
                output_file.write("EOF\n")
                output_file.write("./install_cuda.sh\n")

                nvidia_docker_installation_list = SUPPORTED_CONFIGURATIONS["NVIDIA_DOCKER_INSTALLATION"]["installation"]
                output_file.write("cat > install_nvidia-docker.sh <<EOF\n")
                output_file.writelines('\n'.join(nvidia_docker_installation_list))
                output_file.write("\nEOF\n")
                output_file.write("./install_nvidia-docker.sh\n")

            output_file.write("docker build -t projectmirror/{}_baseimage:1.0".format(self.requirements_dict.get("project_name")) + " base_image\n")
            output_file.write("docker stop {}\n".format(project_name))
            output_file.write("docker-compose down\n")
            output_file.write("docker-compose build\n")
            output_file.write("docker-compose up -d\n")
            output_file.write("docker exec -it {} bash\n".format(project_name))

        os.chmod(path_to_executable, 0o777)


if __name__ == '__main__':
    requirements = {'project_name': 'project_mark1','cuda_version':'cuda8', 'python_version': 'python2', 'primary_architecture': 'cpu',
                    'dl_frameworks': ['pytorch', 'tensorflow'],
                    'pylibs': ['numpy', 'scipy', 'pandas', 'matplotlib', 'scikit-learn'],
                    'project_path': '/Users/aditya/Personal/projects/mirror/editor'}

    ExecutableGenerator('./', requirements_dict=requirements).generate_executable()
