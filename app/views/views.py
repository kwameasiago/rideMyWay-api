import re
from flask import Flask, request
from flask_restplus import Resource, Api, fields
from ..models.rides import *


app = Flask(__name__)
api = Api(app)
app.config.from_pyfile('../../config.py')
obj = Rides()

new_ride = api.model('post ride',{
	'username':fields.String('username'),
	'capacity':fields.Integer('capacity'),
	'time':fields.String('Time'),
	'date':fields.String('date'),
	'month':fields.String('month'),
	'year':fields.Integer('Year'),
	'pickup': fields.String('pickup'),
	'destination':fields.String('destination'),
	'email':fields.String('email')
	})
new_request = api.model('post request',{
    'username':fields.String('username'),
    'pick_up_time':fields.String('pick up time'),
    'destination':fields.String('destination'),
    'pick_up_point':fields.String('pick up point')
    })

@api.route('/rides')
class rides(Resource):
    def get(self):
        if obj.isEmpty_ride_data() == True:
        	return {'result':'There are no new rides'},404
        else:
        	return obj.view_ride()
     
    @api.expect(new_ride)   
    def post(self):
    	data = request.get_json()
        match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', data['email'])

        if obj.key_format(data) == False:
        	return {'result': 'Incorrect key(s) used'},403
        elif obj.same_direction(data['pickup'],data['destination']):
            return {'result':'destination and pick up point are identical'},403
        elif obj.is_empty(data):
            return {'result': 'All the fields are required'},403
        elif obj.only_space(data):
            return {'result': 'Input not allowed.white space Error'},403
        if obj.correct_data(data) == 'year':
            return {'result': 'Incorrect year'},403
        elif obj.correct_data(data) == 'capacity':
            return {'result': 'Incorrect capacity'},403
        elif obj.correct_data(data) == 'month': 
            return {'result': 'Incorrect Month'},403
        elif match == None:
            return {'result': 'Incorrect Email'},403
        else:
        	return obj.add_ride(data['username'],data['capacity'],data['time'],
                data['date'],data['month'],data['year'],data['pickup'],data['destination'],data['email'])


@api.route('/rides/<rideId>')
class single_ride(Resource):
    def get(self, rideId):     
        if obj.ride_exist(rideId) == False:
            return {'result': 'invalid ride id'},404
        else:
            return obj.view_ride_single(rideId)



@api.route('/rides/<rideId>/requests')
class ride_requests(Resource):
    @api.expect(new_request)
    def post(self, rideId):
        data = request.get_json()
        if obj.ride_exist(rideId) == False:
            return {'result': 'invalid ride id'},404
        elif obj.key_format_request(data) == False:
            return {'result': 'Incorrect key(s) used'},403
        elif obj.is_empty_request(data):
            return {'result': 'All the fields are required'},403
        elif obj.only_space_request(data):
            return {'result': 'Input not allowed.white space Error'},403
        elif obj.is_string_request(data) == True:
            return {'result': 'Incorrect value data type.'},403
        elif obj.same_direction(data['pick_up_point'],data['destination']):
            return {'result':'destination and pick up point are identical'},403
        else:
            return obj.add_request(data['username'],data['pick_up_time'],
                data['destination'],data['pick_up_point'],rideId)