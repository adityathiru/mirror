from flask import jsonify, request, render_template, Response
from webapp.api import app
# from werkzeug.datastructures import ImmutableMultiDict
from webapp.api.utils.requirements_generator import RequirementsGenerator


def jsonify_status_code(**kw):
    response = jsonify(**kw)
    response.status_code = kw['code']
    return response


@app.route('/requirements', methods=['GET'])
def requirements():
    return render_template('index.html')


@app.route('/processing/<process_id>', methods=['POST'])
def requirements_post(process_id):
    form_data = request.form
    dict_form_data = form_data.to_dict()
    user_config_path = '/webapp/user/{}/'.join(process_id)

    dict_form_data["pylibs"] = request.form.getlist("pylibs")
    dict_form_data["deep_ll"] = request.form.getlist("deep_ll")

    RequirementsGenerator(dict_form_data, user_config_path).python_modules_requirements()
    RequirementsGenerator(dict_form_data, user_config_path).display_requirements_dict()
    return "ok"
