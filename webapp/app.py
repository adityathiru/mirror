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
from webapp.utils.tools import validate_form, ElasticWriter
from webapp.utils.config import ELASTICSEARCH


app = Flask(__name__)
CORS(app)

indexer = ElasticWriter(host=ELASTICSEARCH['host'],
                        port=ELASTICSEARCH['port'],
                        e_index=ELASTICSEARCH['e_index'])


def jsonify_status_code(**kw):
    response = jsonify(**kw)
    response.status_code = kw['code']
    return response


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404


@app.errorhandler(405)
def page_not_allowd(e):
    # note that we set the 405 status explicitly
    return render_template('405.html'), 405


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
    if validate_form(dict_form_data) != True:
        return render_template('configurator.html', error= validate_form(dict_form_data))
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
    indexer.write({
        'project_name': project_name,
        'process_id': process_id
    })
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
    indexer.write({
        'download': True,
    })
    return send_file(zipfile_path, attachment_filename=project_name+'.zip')


if __name__ == "__main__":
    run_server(app, host='0.0.0.0', port=8000, debug=True)
