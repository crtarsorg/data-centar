from flask import Blueprint, render_template

mod_about = Blueprint('about', __name__, url_prefix='/about')

@mod_about.route('/', methods=['GET'])
def index():
    return render_template('mod_about/index.html')
