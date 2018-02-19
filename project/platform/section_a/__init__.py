import flask_restful
from project import blueprints
import coverage
coverage.process_startup()

api = flask_restful.Api(blueprints[__name__], prefix="/blueprint")

@api.route('/helloworld')
class HelloWorld(flask_restful.Resource):
    def get(self):
        return {'hello': 'world'}
