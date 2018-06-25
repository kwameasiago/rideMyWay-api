from flask import Flask, request
from ..models.rides import rides
from flask_restplus import Resource, Api, fields


app = Flask(__name__)
api = Api(app)
app.config.from_pyfile('../../config.py')

@api.route('/rides')
class rides(Resource):
    def get(self):
        pass


    @api.expect(new_ride)
    def post(self):
        pass


@api.route('/rides/<rideId>')
class rides_id(Resource):
    def get(self, rideId):     
        pass


@api.route('/rides/<rideId>/requests')
class ride_requests(Resource):
    @api.expect(ride_request)
    def post(self, rideId):
        pass
