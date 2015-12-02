from flask import Blueprint, render_template

mod_search = Blueprint('search', __name__, url_prefix='/search')

@mod_search.route('/', methods=['GET'])
def index():
    return render_template('mod_search/index.html')
