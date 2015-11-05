from flask import Blueprint, render_template
import random

mod_landing_page = Blueprint('landing_page', __name__, static_url_path='static')

@mod_landing_page.route('/', methods=['GET'])
def index():
    bg_id = random.randint(1, 7)
    return render_template('mod_landing_page/index.html', bg_id=str(bg_id))

