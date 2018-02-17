from flask import Blueprint
import flask_restful

class HelloWorld(flask_restful.Resource):
    def get(self):
        return {'hello2': 'world2'}

section_b_blueprint = Blueprint('section_b', __name__)

api = flask_restful.Api(section_b_blueprint, prefix="/blueprint2")
api.add_resource(HelloWorld, "/helloworld")