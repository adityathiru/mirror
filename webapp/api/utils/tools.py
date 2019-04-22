from webapp.api.utils.config import SUPPORTED_CONFIGURATIONS


def get_backend(requirements_dict):
    if all([requirements_dict.get('cuda_version'), requirements_dict.get('cuda_version') in SUPPORTED_CONFIGURATIONS['SUPPORTED_GPU']]):
        return requirements_dict['cuda_version']
    else:
        return 'cpu'
