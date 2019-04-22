import os
import uuid

from webapp.api import app
from flask import jsonify, request, render_template, Response
from webapp.api.utils.requirements_generator import RequirementsGenerator
# from werkzeug.datastructures import ImmutableMultiDict


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
    user_config_path = '/var/lib/data/{}/'.format(process_id)
    if not os.path.exists(user_config_path):
        os.makedirs(user_config_path)

    dict_form_data["pylibs"] = request.form.getlist("pylibs")
    dict_form_data["dl_frameworks"] = request.form.getlist("dl_frameworks")

    requirements_generator = RequirementsGenerator(dict_form_data, user_config_path)
    requirements_generator.python_modules_requirements()


    return "ok"
