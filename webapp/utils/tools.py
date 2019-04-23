import re
import os
from webapp.utils.config import SUPPORTED_CONFIGURATIONS


def get_backend(requirements_dict):
    if all([requirements_dict.get('cuda_version'), requirements_dict.get('cuda_version') in SUPPORTED_CONFIGURATIONS['SUPPORTED_GPU']]):
        return requirements_dict['cuda_version']
    else:
        return 'cpu'


def validate_form(form_dict):
    form_dict['project_name'] = form_dict['project_name'].lower()
    if not re.match("^[a-z0-9_]*$", form_dict['project_name']):
        return "Please use lowercase numbers and underscore for project_name."
    if not os.path.isabs(form_dict['project_path']):
        return "Please enter the absolute path for project path."
    else:
        return True


if __name__ == '__main__':
    print(validate_form({"project_name":"Project_123","project_path" : "/user/project_name"}))