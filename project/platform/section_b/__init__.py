from flask import Blueprint
import flask_restful

section_b_blueprint = Blueprint('section_b', __name__)
api = flask_restful.Api(section_b_blueprint, prefix="/blueprint2")

@api.route('/helloworld')
class HelloWorld(flask_restful.Resource):
    def get(self):
        return {'hello2': 'world2'}