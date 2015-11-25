from flask import Blueprint, render_template

mod_about = Blueprint('about', __name__, static_url_path='static')

@mod_about.route('/', methods=['GET'])
def index():
    return render_template('mod_about/index.html')
