import os
from flask import Flask, Blueprint
from flask.ext import restful

class HelloWorld(restful.Resource):
    def get(self):
        return {'hello': 'world'}

blueprint = Blueprint('my_blueprint', __name__)

api = restful.Api(blueprint, prefix="/blueprint")
api.add_resource(HelloWorld, "/helloworld")

app = Flask(__name__)
app.register_blueprint(blueprint)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)