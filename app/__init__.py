from flask import Flask, request, g, abort
import os
import ConfigParser
from logging.handlers import RotatingFileHandler
from flask.ext.pymongo import PyMongo
from flask.ext.cors import CORS
from flask.ext.babel import Babel
import tldextract


babel = Babel()

# Create MongoDB database object.
mongo = PyMongo()

def create_app():
    # Here we  create flask instance
    app = Flask(__name__)

    # Allow cross-domain access to API.
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

    # Load application configurations
    load_config(app)

    # Configure logging.
    configure_logging(app)

    # Init modules
    init_modules(app)

    # Initialize the app to work with MongoDB
    mongo.init_app(app, config_prefix='MONGO')

    # init internationalization
    babel.init_app(app)

    # Get local based on domain name used.
    @babel.localeselector
    def get_locale():
        """Direct babel to use the language defined in the session."""
        return g.get('current_lang', 'en')

    @app.before_request
    def before():
        if request.view_args and 'lang_code' in request.view_args:
            if request.view_args['lang_code'] not in ('sr', 'en'):
                return abort(404)
            g.current_lang = request.view_args['lang_code']
            request.view_args.pop('lang_code')

    return app


def load_config(app):
    ''' Reads the config file and loads configuration properties into the Flask app.
    :param app: The Flask app object.
    '''
    # Get the path to the application directory, that's where the config file resides.
    par_dir = os.path.join(__file__, os.pardir)
    par_dir_abs_path = os.path.abspath(par_dir)
    app_dir = os.path.dirname(par_dir_abs_path)

    # Read config file
    config = ConfigParser.RawConfigParser()
    config_filepath = app_dir + '/config.cfg'
    config.read(config_filepath)

    #app.config['HOST'] = config.get('Application', 'HOST')
    app.config['SERVER_PORT'] = config.get('Application', 'SERVER_PORT')
    app.config['MONGO_DBNAME'] = config.get('Mongo', 'DB_NAME')

    # Set the secret key, keep this really secret, we use it to secure wtform filed data
    app.secret_key = config.get('Application', 'SECRET_KEY')

    # Logging path might be relative or starts from the root.
    # If it's relative then be sure to prepend the path with the application's root directory path.
    log_path = config.get('Logging', 'PATH')
    if log_path.startswith('/'):
        app.config['LOG_PATH'] = log_path
    else:
        app.config['LOG_PATH'] = app_dir + '/' + log_path

    app.config['LOG_LEVEL'] = config.get('Logging', 'LEVEL').upper()


def configure_logging(app):
    ''' Configure the app's logging.
     param app: The Flask app object
    '''

    log_path = app.config['LOG_PATH']
    log_level = app.config['LOG_LEVEL']

    # If path directory doesn't exist, create it.
    log_dir = os.path.dirname(log_path)
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Create and register the log file handler.
    log_handler = RotatingFileHandler(log_path, maxBytes=250000, backupCount=5)
    log_handler.setLevel(log_level)
    app.logger.addHandler(log_handler)

    # First log informs where we are logging to.
    # Bit silly but serves  as a confirmation that logging works.
    app.logger.info('Logging to: %s', log_path)


def init_modules(app):

    # Import blueprint modules
    from app.mod_landing_page.views import mod_landing_page
    #from app.mod_map.views import mod_map
    from app.mod_api.views import mod_api
    from app.mod_api_izbori.views import mod_api_izbori
    from app.mod_about.views import mod_about
    from app.mod_search.views import mod_search

    app.register_blueprint(mod_landing_page)
    #app.register_blueprint(mod_map)
    app.register_blueprint(mod_api)
    app.register_blueprint(mod_api_izbori)
    app.register_blueprint(mod_about) 
    app.register_blueprint(mod_search) 
