from flask import Flask, current_app
from routes import *
import rq_dashboard
import os
def create_app(script_info=None):

    # instantiate the app
    app = Flask(__name__)

    # set config
    app.config.from_object(rq_dashboard.default_settings)
    app.config['REDIS_URL'] = "redis://redis:6379/0"

    # register blueprints
    app.register_blueprint(routes)
    app.register_blueprint(rq_dashboard.blueprint, url_prefix="/brain/rq")
    # shell context for flask cli
    app.shell_context_processor({'app': app})

    return app
