from flask import Flask,request
from flask_restplus import Api, Resource, fields
from ..models.signup import Upload

app = Flask(__name__)
api = Api(app)
app.config.from_pyfile('../../config.py')
signin = api.model('signin',{
	'fname':fields.String,
	'lname':fields.String,
	'email':fields.String,
	'dob':fields.String,
	'location':fields.String,
	'password':fields.String
	})


@api.route('/auth/signup')
class SignUp(Resource):
	"""
	class to sign up new users
	"""
	@api.expect(signin)
	def post(self):
		data = request.get_json()
		obj = Upload(data)
		return(obj.uploadData())

@api.route('/auth/login')
class LogIn(Resource):
	"""
	class to log in users
	"""
	def post(self):
		return({'result': 'testing'})

@api.route('/rides')
class Rides(Resource):
	"""
	class to get all rides
	"""
	def get(self):
		return({'result': 'testing'})

@api.route('/rides/<rideId>')
class OneRide(Resource):
	"""
	class to get a single ride
	"""
	def get(self):
		return({'result': 'testing'})

@api.route('/users/rides')
class PostRide(Resource):
	"""
	class to post new ride
	"""
	def post(self):
		return({'result': 'testing'})

@api.route('/rides/<rideId>/requests')
class PostRequest(Resource):
	"""
	class to post a ride request
	"""
	def post(self):
		return({'result':'testing'})

@api.route('/users/rides/<rideId>/requests')
class FetchRequest(Resource):
	"""
	class to fetch all request
	"""
	def get(self):
		return({'result':'testing'})

@api.route('/users/rides/<rideId>/requests/<requestId>')
class PickRequest(Resource):
	"""
	class to accept or reject request
	"""
	def put(self):
		return({'result':'testing'})


