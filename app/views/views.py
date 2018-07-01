import jwt, datetime
from flask import Flask,request
from flask_restplus import Api, Resource, fields
from functools import wraps
from ..models.signup import Upload
from ..models.signin import Upload2

app = Flask(__name__)
authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'X-API-KEY'
    }
}
api = Api(app, authorizations=authorizations)
app.config.from_pyfile('../../config.py')
token = jwt.encode({'user':'kwame','exp':datetime.datetime.utcnow()+datetime.timedelta(minutes=20)},app.config['SECRET_KEY'])
token = token.decode('UTF-8')

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


def token_required(f):
	@wraps(f)
	def decorated(*args,**kwargs):
		token = None
		if 'X-API-KEY' in request.headers:
			token = request.headers['X-API-KEY'] 
		if not token:
			return({'result':'token is missing'})
		try:
			data = jwt.decode(token,app.config['SECRET_KEY'])
		except:
			return({'result':'token is invalid'})
		return(f(*args,**kwargs))
	return(decorated)

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
		return(signin.uploadData(token))

@api.route('/rides')
class Rides(Resource):
	"""
	class to get all rides
	"""
	@api.doc(security='apikey')
	@token_required
	def get(self):
		return({'result': 'testing'})

@api.route('/rides/<rideId>')
class OneRide(Resource):
	"""
	class to get a single ride
	"""
	@api.doc(security='apikey')
	@token_required
	def get(self):
		return({'result': 'testing'})

@api.route('/users/rides')
class PostRide(Resource):
	"""
	class to post new ride
	"""
	@api.doc(security='apikey')
	@token_required
	def post(self):
		return({'result': 'testing'})

@api.route('/rides/<rideId>/requests')
class PostRequest(Resource):
	"""
	class to post a ride request
	"""
	@api.doc(security='apikey')
	@token_required
	def post(self):
		return({'result':'testing'})

@api.route('/users/rides/<rideId>/requests')
class FetchRequest(Resource):
	"""
	class to fetch all request
	"""
	@api.doc(security='apikey')
	@token_required
	def get(self):
		return({'result':'testing'})

@api.route('/users/rides/<rideId>/requests/<requestId>')
class PickRequest(Resource):
	"""
	class to accept or reject request
	"""
	@api.doc(security='apikey')
	@token_required
	def put(self):
		return({'result':'testing'})


