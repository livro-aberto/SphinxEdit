from flask import Flask

import os

# Setup Flask app and app.config
app = Flask(__name__)




def create_app(extra_config_settings={}):
    """
    Initialize Flask applicaton
    """
    import application.views

    app.config.from_object('config')

    # Read extra config settings from function parameter 'extra_config_settings'
    app.config.update(extra_config_settings)  # Overwrite with 'extra_config_settings' parameter

    app.config['LANGUAGE'] = 'pt_BR'
    if app.testing or app.config['TESTING']:
        app.config['LANGUAGE'] = 'en_US'
        app.config['BOOKCLOUD_URL_PREFIX'] = ''

    app.register_blueprint(application.views.sphinxedit,
                           url_prefix=app.config['BOOKCLOUD_URL_PREFIX'])

    return app



