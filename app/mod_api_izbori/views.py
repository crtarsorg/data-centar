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


@mod_api_izbori.route("/<string:election_type>/godina/<int:year>/teritorija", methods=['GET'])
def parliamentary_votes_grouped_by_territory(election_type, year):
    rsp = izbori_data_provider.get_votes_grouped_by_territory(election_type, year)
    return Response(response=json_util.dumps(rsp), status=200, mimetype='application/json')


@mod_api_izbori.route("/<string:election_type>/godina/<int:year>/teritorija/<string:territory_slug>", methods=['GET'])
def parliamentary_votes_for_territory(election_type, year, territory_slug):
    rsp = izbori_data_provider.get_votes_grouped_by_territory(election_type, year, territory_slug)
    return Response(response=json_util.dumps(rsp), status=200, mimetype='application/json')


@mod_api_izbori.route("/<string:election_type>/godina/<int:year>/izborna-lista", methods=['GET'])
def parliamentary_votes_grouped_by_party(election_type, year):
    rsp = izbori_data_provider.get_votes_grouped_by_party_or_candidate(election_type, year)
    return Response(response=json_util.dumps(rsp), status=200, mimetype='application/json')


@mod_api_izbori.route("/<string:election_type>/godina/<int:year>/izborna-lista/<string:party_slug>", methods=['GET'])
def parliamentary_votes_for_party(election_type, year, party_slug):
    rsp = izbori_data_provider.get_votes_grouped_by_party_or_candidate(election_type, year, party_slug)
    return Response(response=json_util.dumps(rsp), status=200, mimetype='application/json')


@mod_api_izbori.route("/<string:election_type>/godina/<int:year>/krug/<string:round_slug>/teritorija", methods=['GET'])
def presidential_votes_grouped_by_territory(election_type, year, round_slug):
    rsp = izbori_data_provider.get_votes_grouped_by_territory(election_type, year, None, round_slug)
    return Response(response=json_util.dumps(rsp), status=200, mimetype='application/json')


@mod_api_izbori.route("/<string:election_type>/godina/<int:year>/krug/<string:round_slug>/teritorija/<string:territory_slug>", methods=['GET'])
def presidential_votes_for_territory(election_type, year, round_slug, territory_slug):
    rsp = izbori_data_provider.get_votes_grouped_by_territory(election_type, year, territory_slug, round_slug)
    return Response(response=json_util.dumps(rsp), status=200, mimetype='application/json')


@mod_api_izbori.route("/<string:election_type>/godina/<int:year>/krug/<string:round_slug>/kandidat", methods=['GET'])
def presidential_votes_grouped_by_candidate(election_type, year, round_slug):
    rsp = izbori_data_provider.get_votes_grouped_by_party_or_candidate(election_type, year, None, round_slug)
    return Response(response=json_util.dumps(rsp), status=200, mimetype='application/json')


@mod_api_izbori.route("/<string:election_type>/godina/<int:year>/krug/<string:round_slug>/kandidat/<string:candidate_slug>", methods=['GET'])
def presidential_votes_for_candidate(election_type, year, round_slug, candidate_slug):
    rsp = izbori_data_provider.get_votes_grouped_by_party_or_candidate(election_type, year, candidate_slug, round_slug)
    return Response(response=json_util.dumps(rsp), status=200, mimetype='application/json')

