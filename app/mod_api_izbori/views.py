from flask import Blueprint, Response
from app.data_manager.izbori_data_provider import IzboriDataProvider
from bson import json_util

izbori_data_provider = IzboriDataProvider()

mod_api_izbori = Blueprint('api_izbori', __name__, url_prefix='/api/izbori')


@mod_api_izbori.route("/", methods=['GET'])
def index():
    '''
    Renders the API documentation page.
    :return:
    '''
    return 'Izbori API'


@mod_api_izbori.route("/<int:data_source>/<string:election_type>/godina/<int:year>/teritorija/instanca/<int:territory_level>", methods=['GET'])
def parliamentary_votes_grouped_by_territory(data_source, election_type, year, territory_level):
    if data_source == 2 and year not in [2014, 2016]:
        return Response(response=json_util.dumps(
            {'error': 'Data Source 2 is currently only available for 2014 and 2016 Parliamentary Elections.'}),
                        status=200,
                        mimetype='application/json')
    else:
        rsp = izbori_data_provider.get_votes_grouped_by_territory(data_source, election_type, year, territory_level)
        return Response(response=json_util.dumps(rsp), status=200, mimetype='application/json')


@mod_api_izbori.route("/<int:data_source>/<string:election_type>/godina/<int:year>/teritorija/instanca/<int:territory_level>/<string:territory_slug>", methods=['GET'])
def parliamentary_votes_for_territory(data_source, election_type, year, territory_level, territory_slug):
    if data_source == 2 and year not in [2014, 2016]:
        return Response(response=json_util.dumps(
            {'error': 'Data Source 2 is currently only available for 2014 and 2016 Parliamentary Elections.'}),
                        status=200,
                        mimetype='application/json')
    else:
        rsp = izbori_data_provider.get_votes_grouped_by_territory(data_source, election_type, year, territory_level, territory_slug)
        return Response(response=json_util.dumps(rsp), status=200, mimetype='application/json')


@mod_api_izbori.route("/<int:data_source>/<string:election_type>/godina/<int:year>/izborna-lista", methods=['GET'])
def parliamentary_votes_grouped_by_party(data_source, election_type, year):
    if data_source == 2:
        return Response(response=json_util.dumps(
            {'error': 'Data Source 2 is currently only available for 2014 and 2016 Parliamentary Elections.'}),
                        status=200,
                        mimetype='application/json')
    else:
        rsp = izbori_data_provider.get_votes_grouped_by_party_or_candidate(data_source, election_type, year)
        return Response(response=json_util.dumps(rsp), status=200, mimetype='application/json')


@mod_api_izbori.route("/<int:data_source>/<string:election_type>/godina/<int:year>/izborna-lista/<string:party_slug>", methods=['GET'])
def parliamentary_votes_for_party(data_source, election_type, year, party_slug):
    if data_source == 2:
        return Response(response=json_util.dumps(
            {'error': 'Data Source 2 is currently only available for 2014 and 2016 Parliamentary Elections.'}),
                        status=200,
                        mimetype='application/json')
    else:
        rsp = izbori_data_provider.get_votes_grouped_by_party_or_candidate(data_source, election_type, year, party_slug)
        return Response(response=json_util.dumps(rsp), status=200, mimetype='application/json')


@mod_api_izbori.route("/<int:data_source>/<string:election_type>/godina/<int:year>/krug/<string:round_slug>/teritorija", methods=['GET'])
def presidential_votes_grouped_by_territory(data_source, election_type, year, round_slug):
    if data_source == 2:
        return Response(response=json_util.dumps(
            {'error': 'Data Source 2 is currently only available for 2014 and 2016 Parliamentary Elections.'}),
                        status=200,
                        mimetype='application/json')
    else:
        rsp = izbori_data_provider.get_votes_grouped_by_territory(data_source, election_type, year, None, None, round_slug)
        return Response(response=json_util.dumps(rsp), status=200, mimetype='application/json')


@mod_api_izbori.route("/<int:data_source>/<string:election_type>/godina/<int:year>/krug/<string:round_slug>/teritorija/<string:territory_slug>", methods=['GET'])
def presidential_votes_for_territory(data_source, election_type, year, round_slug, territory_slug):
    if data_source == 2:
        return Response(response=json_util.dumps(
            {'error': 'Data Source 2 is currently only available for 2014 and 2016 Parliamentary Elections.'}),
                        status=200,
                        mimetype='application/json')
    else:
        rsp = izbori_data_provider.get_votes_grouped_by_territory(data_source, election_type, year, None, territory_slug, round_slug)
        return Response(response=json_util.dumps(rsp), status=200, mimetype='application/json')


@mod_api_izbori.route("/<int:data_source>/<string:election_type>/godina/<int:year>/krug/<string:round_slug>/kandidat", methods=['GET'])
def presidential_votes_grouped_by_candidate(data_source, election_type, year, round_slug):
    if data_source == 2:
        return Response(response=json_util.dumps(
            {'error': 'Data Source 2 is currently only available for 2014 and 2016 Parliamentary Elections.'}),
                        status=200,
                        mimetype='application/json')
    else:
        rsp = izbori_data_provider.get_votes_grouped_by_party_or_candidate(data_source, election_type, year, None, round_slug)
        return Response(response=json_util.dumps(rsp), status=200, mimetype='application/json')


@mod_api_izbori.route("/<int:data_source>/<string:election_type>/godina/<int:year>/krug/<string:round_slug>/kandidat/<string:candidate_slug>", methods=['GET'])
def presidential_votes_for_candidate(data_source, election_type, year, round_slug, candidate_slug):
    if data_source == 2:
        return Response(response=json_util.dumps(
            {'error': 'Data Source 2 is currently only available for 2014 and 2016 Parliamentary Elections.'}),
                        status=200,
                        mimetype='application/json')
    else:
        rsp = izbori_data_provider.get_votes_grouped_by_party_or_candidate(data_source, election_type, year, candidate_slug, round_slug)
        return Response(response=json_util.dumps(rsp), status=200, mimetype='application/json')

@mod_api_izbori.route("/<string:election_type_slug>/<int:godina>", methods=['GET'])
def top_indicators(election_type_slug,godina):
        rsp = izbori_data_provider.get_top_indicators_by_type(election_type_slug,godina)
        return Response(response=json_util.dumps(rsp), status=200, mimetype='application/json')