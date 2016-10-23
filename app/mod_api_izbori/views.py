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


@mod_api_izbori.route("/<string:election_type_slug>/godina/<int:year>/teritorija", methods=['GET'])
def votes_grouped_by_territory(election_type_slug, year):
    rsp = izbori_data_provider.get_votes_grouped_by_territory(election_type_slug, year)
    return Response(response=json_util.dumps(rsp), status=200, mimetype='application/json')


@mod_api_izbori.route("/<string:election_type_slug>/godina/<int:year>/teritorija/<string:territorySlug>", methods=['GET'])
def votes_for_territory(election_type_slug, year, territorySlug):
    rsp = izbori_data_provider.get_votes_grouped_by_territory(election_type_slug, year, territorySlug)
    return Response(response=json_util.dumps(rsp), status=200, mimetype='application/json')


@mod_api_izbori.route("/<string:election_type_slug>/godina/<int:year>/izborna-lista", methods=['GET'])
def votes_grouped_by_party(election_type_slug, year):
    rsp = izbori_data_provider.get_votes_grouped_by_party(election_type_slug, year)
    return Response(response=json_util.dumps(rsp), status=200, mimetype='application/json')


@mod_api_izbori.route("/<string:election_type_slug>/godina/<int:year>/izborna-lista/<string:izborna_lista_slug>", methods=['GET'])
def votes_for_party(election_type_slug, year, izborna_lista_slug):
    rsp = izbori_data_provider.get_votes_grouped_by_party(election_type_slug, year, izborna_lista_slug)
    return Response(response=json_util.dumps(rsp), status=200, mimetype='application/json')

