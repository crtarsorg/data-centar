from flask import Blueprint, Response, request, render_template
import json
from app.data_manager.rashodi_data_feeder import RashodiDataFeed

from bson import json_util

mod_api = Blueprint('api', __name__, url_prefix='/api')

@mod_api.route("/sum", methods=['POST'])
def sum():
    query_params = request.data
    json_response = RashodiDataFeed().request_mongo_json_response(json.loads(query_params))
    return Response(response=json_util.dumps(json_response), status=200, mimetype='application/json')


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
