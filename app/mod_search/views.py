from flask import Blueprint, render_template, request

mod_search = Blueprint('search', __name__, url_prefix='/search')

@mod_search.route('/', methods=['GET'])
def index():

    source = request.args.get('source')
    type = request.args.get('type')
    municipality = request.args.get('municipality')
    year = request.args.get('year')

    return render_template('mod_search/index.html',
       source=source,
       type=type,
       municipality=municipality,
       year=year)
