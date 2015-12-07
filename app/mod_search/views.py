from flask import Blueprint, render_template, request

mod_search = Blueprint('search', __name__, url_prefix='/search')

@mod_search.route('/', methods=['GET'])
def index():
    source = (request.args.get('source') if request.args.get('source') != None else "EVERYTHING")
    type = (" " + request.args.get('type') if request.args.get('type') != None else "")
    municipality = (request.args.get('municipality') if request.args.get('municipality') != None else "EVERYWHERE")
    year = (request.args.get('year') if request.args.get('year') != None else "ALL YEARS")

    return render_template('mod_search/index.html',
       source=source,
       type=type,
       municipality=municipality,
       year=year)
