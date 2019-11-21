import flask
from flask_restful import Resource, Api
import  logging as logger
app = Flask(__name__)
api = Api(app)



api.add_resource('hello')

class Task(Resource):

    def get(self):
        logger.debug("inside get method")
        return {"message":"get method"}, 200

    def post(self):
        logger.debug("inside post method")
        return {"message": "post method"}, 200

    def put(self):
        logger.debug("inside put method")
        return {"message": "put method"}, 200

    def delete(self):
        logger.debug("inside delete method")
        return {"message": "delete method"}, 200

