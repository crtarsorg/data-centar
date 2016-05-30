from flask import Blueprint, render_template
import random
from app.utils.option import Option

mod_landing_page = Blueprint('landing_page', __name__, static_url_path='static')

@mod_landing_page.route('/', methods=['GET'])
def index():
    return render_template('mod_landing_page/index.html', lang_code='en')

@mod_landing_page.route('/<lang_code>', methods=['GET'])
def root():
    return render_template('mod_landing_page/index.html')
