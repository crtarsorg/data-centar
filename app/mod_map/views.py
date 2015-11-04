from flask import Blueprint, render_template

mod_map = Blueprint('map', __name__, url_prefix='/mapa')

@mod_map.route('/', methods=['GET'])
def index():
    return render_template('mod_map/index.html')

