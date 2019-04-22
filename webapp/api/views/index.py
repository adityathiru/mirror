import os
import uuid

from webapp.api import app
from flask import jsonify, request, render_template, Response
from webapp.api.utils.requirements_generator import RequirementsGenerator
from webapp.api.utils.dockerfile_generator import DockerFileGenerator
from webapp.api.utils.dockercompose_generator import DockerComposeGenerator

def jsonify_status_code(**kw):
    response = jsonify(**kw)
    response.status_code = kw['code']
    return response


@app.route('/requirements', methods=['GET'])
def requirements():
    return render_template('index.html')


@app.route('/processing', methods=['POST'])
def requirements_post():
    form_data = request.form
    dict_form_data = form_data.to_dict()

    process_id = uuid.uuid4()
    path_to_project = '/var/lib/data/{}/'.format(process_id)
    if not os.path.exists(path_to_project):
        os.makedirs(path_to_project)

    dict_form_data["pylibs"] = request.form.getlist("pylibs")
    dict_form_data["dl_frameworks"] = request.form.getlist("dl_frameworks")

    # REQUIREMENTS GENERATOR
    requirements_generator = RequirementsGenerator(dict_form_data, path_to_project)
    requirements_generator.python_modules_requirements()

    # DOCKERFILE GENERATOR
    dockerfile_generator = DockerFileGenerator(path_to_project, requirements_dict=dict_form_data)
    dockerfile_generator.create_dockerfile()

    # DOCKERCOMPOSE GENERATOR
    dockercompose_generator = DockerComposeGenerator('./', requirements_dict=dict_form_data)
    dockercompose_generator.create_dockercompose()

    print('project_id', process_id)

    return "ok"
