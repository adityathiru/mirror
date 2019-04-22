from webapp.api.utils.config import SUPPORTED_CONFIGURATIONS
from webapp.api.utils.tools import get_backend
import os

class ExecutableGenerator:
    def __init__(self, requirements_dict, path):
        self.requirements_dict = requirements_dict
        self.path = path

    def generate_executable(self):
        executable = []
        backend = get_backend(self.requirements_dict)
        output_file = open(os.path.join(self.path, "exec.dat"), "w+")
        if backend != 'cpu':
            with open(SUPPORTED_CONFIGURATIONS["BACKEND_INSTALLATION"][backend]["installation"]) as install_commands:
                output_file.write("cat > install_cuda.sh <<EOF\n")
                while install_commands.readline():
                    output_file.write(install_commands.readline())
            output_file.write("EOF\n")
            output_file.write("./install_cuda.sh\n")
        output_file.write("docker build -t projectmirror/{}".format(self.requirements_dict.get("project_name")) + " .\n")
        output_file.write("docker-compose down\n")
        output_file.write("docker-compose build\n")
        output_file.write("docker-compose up\n")
        output_file.close()


if __name__ == '__main__':
    requirements= {'project_name': 'project_mark1','cuda_version':'cuda8', 'python_version': 'python2', 'primary_architecture': 'cpu',
                         'dl_frameworks': ['pytorch', 'tensorflow'],
                         'pylibs': ['numpy', 'scipy', 'pandas', 'matplotlib', 'scikit-learn'],
                         'project_path': '/Users/aditya/Personal/projects/mirror/editor'}
    ExecutableGenerator(requirements).generate_executable()
