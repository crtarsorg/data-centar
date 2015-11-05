from flask import Blueprint, Response, request, render_template
import json
from app.data_manager.rashodi_data_feeder import RashodiDataFeed

from bson import json_util
from requestforms import SumRequestForm, ClassificationsRequestForm

mod_api = Blueprint('api', __name__, url_prefix='/api')

@mod_api.route("/zbir", methods=['POST'])
def sum():
    query_params = request.data
    json_response = RashodiDataFeed().calculate_sum_of_expenditure_types(json.loads(query_params))
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
    sum_req_form = SumRequestForm()
    return render_template('mod_api/index.html', sum_req_form=sum_req_form)
