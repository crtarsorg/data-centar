from flask import Blueprint, Response, request, render_template
from app.data_manager.data_provider import DataProvider
from app.commons.data_request_form import DataRequestForm
from app.utils.mongo_utils import MongoUtils
from bson import json_util
import json

utils = MongoUtils()

mod_api = Blueprint('api', __name__, url_prefix='/api')

@mod_api.route("/", methods=['GET'])
def index():
    '''
    Renders the API documentation page.
    :return:
    '''
    sum_req_form = DataRequestForm()
    return render_template('mod_api/index.html', sum_req_form=sum_req_form)

@mod_api.route("/zbir", methods=['POST'])
def sum():
    query_params = json.loads(request.data)
    json_response = DataProvider().calculate_sum_of_expenditure_types(query_params)
    return Response(response=json_util.dumps(json_response), status=200, mimetype='application/json')

@mod_api.route('/prosek', methods=['POST'])
def averages():
    json_resp = DataProvider().retrieve_average_data_for_classification_number(json.loads(request.data))
    return Response(response=json_util.dumps(json_resp), status=200, mimetype='application/json')

@mod_api.route("/ekonomska-klasifikacija", methods=['GET', 'POST'])
def activities():

    if request.method == 'POST':
        query_params = json.loads(request.data)
        json_response = DataProvider().calculate_sum_of_expenditure_types(query_params)

    elif request.method == 'GET':
        data_type = request.args.get('dataType')
        json_response = utils.retrieve_classification_numbers(data_type)

    return Response(response=json.dumps(json_response), status=200, mimetype='application/json')

@mod_api.route('/sakupiti-klasifikacija-za-opstine', methods=['POST'])
def aggregated_classifications():
    json_resp = DataProvider().retrieve_aggregated_classification_info_for_municipalities(json.loads(request.data))
    return Response(response=json_util.dumps(json_resp), status=200, mimetype="application/json")

@mod_api.route('/spisak-opstina-za-klasifikacija-broj', methods=['POST']) # List of municipalities for given class. number
def list_of_municipalities():
    query_params = json.loads(request.data)
    json_resp = DataProvider().calculate_sum_of_expenditure_types(query_params)

    return Response(response=json_util.dumps(json_resp), status=200, mimetype="application/json")

