from flask import jsonify, request,render_template, Response
from webapp.api import app
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
    print(request.form.to_dict())
    return "ok"
