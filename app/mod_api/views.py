from flask import Blueprint, Response, request, render_template
from app.data_manager.prihodi_data_feeder import PrihodiDataFeed
from app.data_manager.rashodi_data_feeder import RashodiDataFeed
from app.commons.data_request_form import DataRequestForm

from bson import json_util
import json

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
    if query_params['tipPodataka'] == "rashodi":
        json_response = RashodiDataFeed().calculate_sum_of_expenditure_types(query_params)
    else:
        json_response = PrihodiDataFeed().calculate_sum_of_expenditure_types(query_params)
    return Response(response=json_util.dumps(json_response), status=200, mimetype='application/json')

@mod_api.route("/ekonomska-klasifikacija", methods=['POST'])
def activities():
    query_params = json.loads(request.data)
    if query_params['tipPodataka'] == "rashodi":
        json_response = RashodiDataFeed().build_json_response_for_parent_categories(query_params)
    else:
        json_response = PrihodiDataFeed().build_json_response_for_parent_categories(query_params)
    return Response(response=json.dumps(json_response), status=200, mimetype='application/json')


@mod_api.route('/klasifikacija-info-za-opstina', methods=['POST'])
def classification_number():
    print json.loads(request.data)
    json_resp = RashodiDataFeed().retrieve_data_for_given_classification_number(json.loads(request.data))
    return Response(response=json_util.dumps(json_resp), status=200, mimetype="application/json")


@mod_api.route('/sakupiti-klasifikacija-za-opstine', methods=['POST'])
def aggregated_classifications():
    json_resp = RashodiDataFeed().retrieve_aggregated_classification_info_for_municipalities(json.loads(request.data))
    return Response(response=json_util.dumps(json_resp), status=200, mimetype="application/json")

@mod_api.route('/spisak-opstina-za-klasifikacija-broj', methods=['POST']) # List of municipalities for given class. number
def list_of_municipalities():
    query_params = json.loads(request.data)

    if query_params['tipPodataka'] == 'rashodi':
        json_resp = RashodiDataFeed().retrieve_list_of_municipalities_for_given_class(query_params)
    else:
        json_resp = PrihodiDataFeed().retrieve_list_of_municipalities_for_given_class(query_params)
    return Response(response=json_util.dumps(json_resp), status=200, mimetype="application/json")
