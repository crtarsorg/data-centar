from flask import Blueprint, Response, request, render_template
import json

mod_api = Blueprint('api', __name__, url_prefix='/api')

@mod_api.route("/sum", methods=['POST'])
def sum():
    return Response(response=json.dumps({}), status=200, mimetype='application/json')


@mod_api.route("/activities", methods=['POST'])
def activities():
    return Response(response=json.dumps({}), status=200, mimetype='application/json')


@mod_api.route("/", methods=['GET'])
def index():
    '''
    Renders the API documentation page.
    :return:
    '''
    return render_template('mod_api/index.html')


