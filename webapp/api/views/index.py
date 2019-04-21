from flask import jsonify, request,render_template, Response
from webapp.api import app
# from werkzeug.datastructures import ImmutableMultiDict
from webapp.api.utils.requirements_generator import requirements_generator

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
    dict_form_data["pylibs"] = request.form.getlist("pylibs")
    dict_form_data["deep_ll"] = request.form.getlist("deep_ll")
    requirements_generator(dict_form_data).python_modules_requirements()
    requirements_generator(dict_form_data).display_requirements_dict()
    return "ok"
