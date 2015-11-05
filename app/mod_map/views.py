from flask import Blueprint, render_template
from app.commons.data_request_form import DataRequestForm

mod_map = Blueprint('map', __name__, url_prefix='/mapa')

@mod_map.route('/', methods=['GET'])
def index():
    form = DataRequestForm()
    return render_template('mod_map/index.html', form=form);

