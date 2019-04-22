from webapp.api.utils.config import SUPPORTED_CONFIGURATIONS


def set_default_python(python_version):
    """
    takes python version, returns list of dockerfile commands for setting default version
    :param python_version:
    :return:
    """
    if python_version not in SUPPORTED_CONFIGURATIONS['SUPPORTED_PYTHON_VERSIONS'].keys():
        raise ValueError('Invalid Python Version')

    docker_python_symlinks_command_list = [
        'RUN rm -f /usr/bin/{python_version} && ln -s /usr/bin/{exact_python_version} /usr/bin/{python_version}'.format(
            python_version=python_version, exact_python_version=SUPPORTED_CONFIGURATIONS['SUPPORTED_PYTHON_VERSIONS'][python_version]),
        'RUN rm -f /usr/bin/python && ln -s /usr/bin/{exact_python_version} /usr/bin/python'.format(
            exact_python_version=SUPPORTED_CONFIGURATIONS['SUPPORTED_PYTHON_VERSIONS'][python_version])]

    return docker_python_symlinks_command_list


def install_deeplearning_frameworks(deeplearning_frameworks, python_version, backend):
    """
    gets the commands required to install the deep learning frameworks and its complimentary packages
    :param deeplearning_frameworks:
    :param python_version:
    :param backend:
    :return docker_dl_frameworks_commands_list:
    """
    if python_version not in SUPPORTED_CONFIGURATIONS['SUPPORTED_PYTHON_VERSIONS'].keys():
        raise ValueError('Invalid Python Version: {}'.format(python_version))

    if backend not in SUPPORTED_CONFIGURATIONS['SUPPORTED_BACKEND']:
        raise ValueError('Invalid Backend: {} not in {}'.format(backend, SUPPORTED_CONFIGURATIONS['SUPPORTED_BACKEND']))

    exact_python_version = SUPPORTED_CONFIGURATIONS['SUPPORTED_PYTHON_VERSIONS'][python_version]
    docker_dl_frameworks_commands_list = []
    for framework in deeplearning_frameworks:
        if framework not in SUPPORTED_CONFIGURATIONS['DEEP_LEARNING_FRAMEWORKS'].keys():
            raise ValueError('Invalid DeepLearning Framework')

        required_config = SUPPORTED_CONFIGURATIONS['DEEP_LEARNING_FRAMEWORKS'][framework][exact_python_version][backend]
        other_packages = SUPPORTED_CONFIGURATIONS['DEEP_LEARNING_FRAMEWORKS'][framework][exact_python_version]['other_packages']

        if python_version == 'python2':
            pip_install_docker_command = 'RUN pip install '
        elif python_version == 'python3':
            pip_install_docker_command = 'RUN pip3 install '
        else:
            raise ValueError('Invalid Python Version: {}'.format(python_version))

        pip_install_dl_framework_installation = pip_install_docker_command + required_config['installation']
        docker_dl_frameworks_commands_list.append(pip_install_dl_framework_installation)

        for package in other_packages:
            docker_dl_frameworks_commands_list.append(pip_install_docker_command + package)

    return docker_dl_frameworks_commands_list


def add_nvidiadocker_support(backend):
    """
    if gpu backend - we add support in dockerfile to communicate with host gpu
    :param backend:
    :return:
    """
    if backend not in SUPPORTED_CONFIGURATIONS['SUPPORTED_GPU']:
        return []

    docker_nvidia_commands_list = SUPPORTED_CONFIGURATIONS['NVIDIA_DOCKER_INSTALLATION']['installation']

    return docker_nvidia_commands_list


def install_backend(backend):
    """
    takes in cuda backend ('cuda8, 'cuda9' etc.) and returns the docker command list for the same
    :param backend:
    :return:
    """
    install_script_path = SUPPORTED_CONFIGURATIONS['NVIDIA_DOCKER_INSTALLATION'][backend]['installation']

    provide_permissions = 'sudo chmod a+x ' + install_script_path
    backend_installation = 'sudo ./' + install_script_path

    backend_commands_list = [provide_permissions,
                             backend_installation]

    return backend_commands_list


def install_editor():
    pass
