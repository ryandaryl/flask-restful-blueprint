import os
from flask import Flask, Blueprint
import flask_restful

app = Flask(__name__)

app.config.from_object('config.Config')
environment = os.environ.get('FLASK_ENV', app.config.get('DEFAULT_ENVIRONMENT'))
for e in environment.split(','):
    app.config.from_object('.'.join(['config', e.title()]))

blueprint = Blueprint('my_blueprint', __name__)

class HelloWorld(flask_restful.Resource):
    def get(self):
        return {'hello': 'world'}

api = flask_restful.Api(blueprint, prefix="/blueprint")
api.add_resource(HelloWorld, "/helloworld")

app.register_blueprint(blueprint)

if __name__ == "__main__":
    app.run(
      host=app.config.get('HOST'),
      port=int(app.config.get('PORT'))
    )