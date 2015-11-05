from flask import Blueprint, Response, request, render_template
import json
from app import mongo

mod_api = Blueprint('api', __name__, url_prefix='/api')

@mod_api.route("/sum", methods=['POST'])
def sum():
    query_params = request.data
    json_response = request_mongo_json_response(query_params)
    return Response(response=json.dumps(json_response), status=200, mimetype='application/json')


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


def request_mongo_json_response(query_params):

    match = {
        "$match": {
            "tipPodataka": query_params['data']
        }
    }

    if query_params['godine'] != []:
        match['$match']["godine"] = {'$in': query_params['godine']}

    if query_params['opstine'] != []:
        match['$match']["opstine"]['latinica'] = {'$in': query_params['opstine']}

    if query_params['klasifikacijaBroj'] != []:
        match['$match']["klasifikacijaBroj"] = {'$in': query_params['klasifikacijaBroj']}

    # Execute mongo request
    json_doc = mongo.db.datacentar.opstine.aggregate([match])

    return json_doc