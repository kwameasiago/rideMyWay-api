from flask import Flask, request
from flask_restplus import Resource, Api, fields


app = Flask(__name__)
api = Api(app)
app.config.from_pyfile('../../config.py')

@api.route('/rides')
class rides(Resource):
    def get(self):
        return({'result':'testing'})
        
    def post(self):
        return({'result':'testing'})


@api.route('/rides/<rideId>')
class rides_id(Resource):
    def get(self, rideId):     
        return({'result':'testing'})


@api.route('/rides/<rideId>/requests')
class ride_requests(Resource):
    def post(self, rideId):
        return({'result':'testing'})
