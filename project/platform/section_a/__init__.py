from flask import Blueprint
import flask_restful

section_a_blueprint = Blueprint('section_a', __name__)
api = flask_restful.Api(section_a_blueprint, prefix="/blueprint")

@api.route('/helloworld')
class HelloWorld(flask_restful.Resource):
    def get(self):
        return {'hello': 'world'}