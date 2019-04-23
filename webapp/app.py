import os
import uuid
import shutil

from flask_cors import CORS
from flask import Flask, jsonify, request, render_template, Response, send_file, redirect, url_for

from webapp.webserver import run_server
from webapp.utils.requirements_generator import RequirementsGenerator
from webapp.utils.dockerfile_generator import DockerFileGenerator
from webapp.utils.dockercompose_generator import DockerComposeGenerator
from webapp.utils.executable_generator import ExecutableGenerator

app = Flask(__name__)
CORS(app)


def jsonify_status_code(**kw):
    response = jsonify(**kw)
    response.status_code = kw['code']
    return response


@app.route('/home', methods=['GET'])
@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')


@app.route('/configurator', methods=['GET'])
def requirements():
    return render_template('configurator.html')


@app.route('/processing', methods=['POST'])
def requirements_post():
    form_data = request.form
    dict_form_data = form_data.to_dict()

    process_id = str(uuid.uuid4())
    path_to_project = '/var/lib/data/{}/'.format(process_id)
    if not os.path.exists(path_to_project):
        os.makedirs(path_to_project)

    dict_form_data["pylibs"] = request.form.getlist("pylibs")
    dict_form_data["dl_frameworks"] = request.form.getlist("dl_frameworks")
    dict_form_data["editors"] = request.form.getlist("editors")
    project_name = dict_form_data["project_name"]

    # REQUIREMENTS GENERATOR
    requirements_generator = RequirementsGenerator(dict_form_data, path_to_project)
    requirements_generator.python_modules_requirements()

    # DOCKERFILE GENERATOR
    path_to_baseimage = os.path.join(path_to_project, 'base_image')
    shutil.copytree('/webapp/utils/base_files/base_image', path_to_baseimage)

    dockerfile_generator = DockerFileGenerator(path_to_project, requirements_dict=dict_form_data)
    dockerfile_generator.create_dockerfile()

    if dict_form_data['editors'] is not None:
        # COPY EDITOR FILES
        path_to_editors = os.path.join(path_to_project, 'editors')
        shutil.copytree('/webapp/utils/base_files/editors', path_to_editors)

    # DOCKERCOMPOSE GENERATOR
    dockercompose_generator = DockerComposeGenerator(path_to_project, requirements_dict=dict_form_data)
    dockercompose_generator.create_dockercompose()

    # GENERATE EXECUTABLE
    executable_generator = ExecutableGenerator(path_to_project, requirements_dict=dict_form_data)
    executable_generator.generate_executable()

    print('project_id', str(process_id))
    return redirect(url_for('processed', project_name=project_name, process_id=process_id))


@app.route('/processed/<process_id>/<project_name>')
def processed(process_id, project_name):
    dir_path = os.path.join("/var/lib/data/", process_id)
    zipfile_path = os.path.join("/var/lib/data", process_id)
    shutil.make_archive(zipfile_path, 'zip', dir_path)
    return render_template('processed.html', process_id=process_id, project_name=project_name)


@app.route('/download/<process_id>/<project_name>')
def download_file(process_id, project_name):
    zipfile_path = os.path.join("/var/lib/data", process_id + ".zip")
    return send_file(zipfile_path, attachment_filename=project_name+'.zip')


if __name__ == "__main__":
    run_server(app, host='0.0.0.0', port=8000, debug=True)
