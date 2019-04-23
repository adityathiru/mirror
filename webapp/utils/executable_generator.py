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
                    output_file.writelines("".join(install_commands.readlines()))
                output_file.write("EOF\n")
                output_file.write("./install_cuda.sh\n")

                nvidia_docker_installation_list = SUPPORTED_CONFIGURATIONS["NVIDIA_DOCKER_INSTALLATION"]["installation"]
                output_file.write("cat > install_nvidia-docker.sh <<EOF\n")
                output_file.writelines('\n'.join(nvidia_docker_installation_list))
                output_file.write("\nEOF\n")
                output_file.write("./install_nvidia-docker.sh\n")
            output_file.writelines("\n".join(self.generate_function("all",SUPPORTED_CONFIGURATIONS["EXEC"]["all"])).replace('{{project_name}}',project_name))
            output_file.writelines("\n".join(self.generate_function("upd",SUPPORTED_CONFIGURATIONS["EXEC"]["upd"])).replace('{{project_name}}',project_name))
            output_file.writelines("\n".join(self.generate_function("up",SUPPORTED_CONFIGURATIONS["EXEC"]["up"])).replace('{{project_name}}',project_name))
            output_file.writelines("\n".join(self.generate_function("stop",SUPPORTED_CONFIGURATIONS["EXEC"]["stop"])).replace('{{project_name}}',project_name))
            output_file.writelines("\n".join(self.generate_function("kill",SUPPORTED_CONFIGURATIONS["EXEC"]["kill"])).replace('{{project_name}}',project_name))
            output_file.writelines("\n".join(self.generate_function("build",SUPPORTED_CONFIGURATIONS["EXEC"]["build"])).replace('{{project_name}}',project_name))
            output_file.writelines("\n".join(SUPPORTED_CONFIGURATIONS["EXEC"]["trail"]))

        os.chmod(path_to_executable, 0o777)

    def generate_function(self,function_name,function_description):
        function =list()
        function.append(function_name+"() {\n")
        function.extend(function_description)
        function.append("\n}\n")
        return function

if __name__ == '__main__':
    requirements = {'project_name': 'project_mark1','cuda_version':'cuda8', 'python_version': 'python2', 'primary_architecture': 'cpu',
                    'dl_frameworks': ['pytorch', 'tensorflow'],
                    'pylibs': ['numpy', 'scipy', 'pandas', 'matplotlib', 'scikit-learn'],
                    'project_path': '/Users/aditya/Personal/projects/mirror/editor'}

    ExecutableGenerator('./', requirements_dict=requirements).generate_executable()
