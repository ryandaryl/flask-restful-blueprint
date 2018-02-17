from flask import Blueprint
import flask_restful

class HelloWorld(flask_restful.Resource):
    def get(self):
        return {'hello': 'world'}

section_a_blueprint = Blueprint('section_a', __name__)

api = flask_restful.Api(section_a_blueprint, prefix="/blueprint")
api.add_resource(HelloWorld, "/helloworld")