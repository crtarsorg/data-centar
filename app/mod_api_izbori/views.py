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


@mod_api_izbori.route("/<int:data_source>/<string:election_type>/godina/<int:year>/teritorija/instanca/<int:territory_level>", methods=['GET', 'POST'])
def parliamentary_votes_grouped_by_territory(data_source, election_type, year, territory_level):
    rsp = izbori_data_provider.get_votes_grouped_by_territory(data_source, election_type, year, territory_level)
    return Response(response=json_util.dumps(rsp), status=200, mimetype='application/json')

@mod_api_izbori.route("/map/landingpage/<int:datasource>", methods=['GET', 'POST'])
def parliamentary_votes_grouped_by_territory_landingpage(datasource):
    rsp = izbori_data_provider.get_votes_grouped_by_territory_landingpage(datasource)
    return Response(response=json_util.dumps(rsp), status=200, mimetype='application/json')

@mod_api_izbori.route("/<int:data_source>/<string:election_type>/godina/<int:year>/teritorija/<string:teritorija_slug>/instanca/<int:territory_level>/krug/<string:krug>", methods=['GET'])
def results_by_territory(data_source, election_type, year,teritorija_slug, territory_level,krug):

    rsp = izbori_data_provider.get_results_by_territory(data_source, election_type, year, teritorija_slug, territory_level,krug)
    return Response(response=json_util.dumps(rsp), status=200, mimetype='application/json')

@mod_api_izbori.route("/landingpage/<int:data_source>/<string:election_type>/teritorija/<string:teritorija_slug>/instanca/<int:territory_level>/krug/<string:krug>", methods=['GET'])
def results_by_territory_landing_page(data_source, election_type,teritorija_slug, territory_level,krug):
    rsp = izbori_data_provider.get_results_by_territory_landingpage(data_source, election_type, teritorija_slug, territory_level,krug)
    return Response(response=json_util.dumps(rsp), status=200, mimetype='application/json')


@mod_api_izbori.route("/<int:data_source>/<string:election_type>/godina/<int:year>/teritorija/instanca/<int:territory_level>/<string:territory_slug>", methods=['GET'])
def parliamentary_votes_for_territory(data_source, election_type, year, territory_level, territory_slug):

    rsp = izbori_data_provider.get_votes_grouped_by_territory(data_source, election_type, year, territory_level, territory_slug)
    return Response(response=json_util.dumps(rsp), status=200, mimetype='application/json')


@mod_api_izbori.route("/<int:data_source>/<string:election_type>/godina/<int:year>/izborna-lista", methods=['GET'])
def parliamentary_votes_grouped_by_party(data_source, election_type, year):

    rsp = izbori_data_provider.get_votes_grouped_by_party_or_candidate(data_source, election_type, year)
    return Response(response=json_util.dumps(rsp), status=200, mimetype='application/json')


@mod_api_izbori.route("/<int:data_source>/<string:election_type>/godina/<int:year>/izborna-lista/<string:party_slug>", methods=['GET'])
def parliamentary_votes_for_party(data_source, election_type, year, party_slug):

    rsp = izbori_data_provider.get_votes_grouped_by_party_or_candidate(data_source, election_type, year, party_slug)
    return Response(response=json_util.dumps(rsp), status=200, mimetype='application/json')


@mod_api_izbori.route("/<int:data_source>/<string:election_type>/godina/<int:year>/krug/<string:round_slug>/teritorija", methods=['GET'])
def presidential_votes_grouped_by_territory(data_source, election_type, year, round_slug):
    rsp = izbori_data_provider.get_votes_grouped_by_territory(data_source, election_type, year, None, None, round_slug)
    return Response(response=json_util.dumps(rsp), status=200, mimetype='application/json')


@mod_api_izbori.route("/<int:data_source>/<string:election_type>/godina/<int:year>/krug/<string:round_slug>/teritorija/<string:territory_slug>", methods=['GET'])
def presidential_votes_for_territory(data_source, election_type, year, round_slug, territory_slug):
    rsp = izbori_data_provider.get_votes_grouped_by_territory(data_source, election_type, year, None, territory_slug, round_slug)
    return Response(response=json_util.dumps(rsp), status=200, mimetype='application/json')


@mod_api_izbori.route("/<int:data_source>/<string:election_type>/godina/<int:year>/krug/<string:round_slug>/kandidat", methods=['GET'])
def presidential_votes_grouped_by_candidate(data_source, election_type, year, round_slug):

    rsp = izbori_data_provider.get_votes_grouped_by_party_or_candidate(data_source, election_type, year, None, round_slug)
    return Response(response=json_util.dumps(rsp), status=200, mimetype='application/json')


@mod_api_izbori.route("/<int:data_source>/<string:election_type>/godina/<int:year>/krug/<string:round_slug>/kandidat/<string:candidate_slug>", methods=['GET'])
def presidential_votes_for_candidate(data_source, election_type, year, round_slug, candidate_slug):

    rsp = izbori_data_provider.get_votes_grouped_by_party_or_candidate(data_source, election_type, year, candidate_slug, round_slug)
    return Response(response=json_util.dumps(rsp), status=200, mimetype='application/json')

@mod_api_izbori.route("/<int:data_source>/<string:election_type_slug>/godina/<int:godina>/instanca/<int:instanca>/krug/<string:round_slug>", methods=['GET'])
def top_indicators(data_source,election_type_slug,godina, instanca,round_slug):
        rsp = izbori_data_provider.get_top_indicators_by_type(data_source, election_type_slug, godina, instanca,round_slug)
        return Response(response=json_util.dumps(rsp), status=200, mimetype='application/json')

@mod_api_izbori.route("/datasource/<int:datasource>/<string:election_type_slug>/godina/<int:godina>/instanca/<int:instanca>", methods=['GET'])
def total_voters_turnout(datasource,election_type_slug,godina,instanca):
        rsp = izbori_data_provider.get_total_voters_turnout(datasource,election_type_slug, godina,instanca)
        return Response(response=json_util.dumps(rsp), status=200, mimetype='application/json')

@mod_api_izbori.route("/landingpage/<int:datasource>", methods=['GET'])
def top_indicators_by_type_landingpage(datasource):
        rsp = izbori_data_provider.get_top_indicators_by_type_landingpage(datasource)
        return Response(response=json_util.dumps(rsp), status=200, mimetype='application/json')

@mod_api_izbori.route("/parties", methods=['GET'])
def political_parties():
        rsp = izbori_data_provider.get_political_parties()
        return Response(response=json_util.dumps(rsp), status=200, mimetype='application/json')

@mod_api_izbori.route("/parties/<string:kanditat_name>", methods=['GET'])
def political_parties_selected(kanditat_name):
        rsp = izbori_data_provider.get_political_parties(kanditat_name)
        return Response(response=json_util.dumps(rsp), status=200, mimetype='application/json')

@mod_api_izbori.route("/winners/<int:data_source>/<string:election_type_slug>/godina/<int:godina>/instanca/<int:instanca>/krug/<string:krug>", methods=['GET'])
def winners_per_territory(data_source,election_type_slug,godina,instanca,krug):
    rsp = izbori_data_provider.get_winners_for_each_territory(data_source,election_type_slug,godina,instanca,krug)
    return Response(response=json_util.dumps(rsp), status=200, mimetype='application/json')


@mod_api_izbori.route("/<int:data_source>/<string:election_type_slug>/godina/<int:godina>/teritorija/<string:territory_slug>/kandidat/<string:candidate_slug>/instanca/<int:instanca>/krug/<string:krug>", methods=['GET'])
def results_by_territory_by_candidate(data_source,election_type_slug,godina,territory_slug, candidate_slug,instanca,krug):
    rsp = izbori_data_provider.get_results_by_territory_by_candidate(data_source,election_type_slug,godina,territory_slug,candidate_slug,instanca,krug)
    return Response(response=json_util.dumps(rsp), status=200, mimetype='application/json')






