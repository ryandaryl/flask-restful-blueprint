import os
from flask import Flask, Blueprint
import flask_restful
from setuptools import find_packages
import project.platform.route_decorator

app = Flask(__name__)

def get_config():
    app.config.from_object('config.Config')
    environment = os.environ.get('FLASK_ENV', app.config.get('DEFAULT_ENVIRONMENT'))
    app.config.from_object('config.' + environment)

def get_blueprints(filter_path=''):
    for path in find_packages():
        if filter_path in path:
            blueprint = path.replace(filter_path, '') + '_blueprint'
            app.register_blueprint(getattr(__import__(path, fromlist=['']), blueprint))

get_config()
get_blueprints('project.platform.')