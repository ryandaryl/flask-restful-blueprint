import os
from flask import Flask, Blueprint
import flask_restful
from setuptools import find_packages
import project.platform.route_decorator

app = Flask(__name__)
blueprints = {}

def get_config():
    app.config.from_object('config.Config')
    environment = os.environ.get('FLASK_ENV', app.config.get('DEFAULT_ENVIRONMENT'))
    app.config.from_object('config.' + environment)

def get_blueprints(filter_path=''):
    for path in find_packages():
        if filter_path in path:
            blueprints[path] = Blueprint(path, path)
            __import__(path)
            app.register_blueprint(blueprints[path])

get_config()
get_blueprints('project.platform.')