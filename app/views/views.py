from flask import Flask,request
from flask_restplus import Api, Resource, fields
from ..models.signup import Upload
from ..models.signin import Upload2

app = Flask(__name__)
api = Api(app)
app.config.from_pyfile('../../config.py')
signUp = api.model('signin',{
	'fname':fields.String,
	'lname':fields.String,
	'email':fields.String,
	'dob':fields.String,
	'location':fields.String,
	'password':fields.String
	})
signIn = api.model('signup',{
	'email':fields.String,
	'password':fields.String
	})


@api.route('/auth/signup')
class SignUp(Resource):
	"""
	class to sign up new users
	"""
	@api.expect(signUp)
	def post(self):
		data = request.get_json()
		signup = Upload(data)
		return(signup.uploadData())

@api.route('/auth/login')
class LogIn(Resource):
	"""
	class to log in users
	"""
	@api.expect(signIn)
	def post(self):
		data = request.get_json()
		signin = Upload2(data)
		return(signin.uploadData())

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


