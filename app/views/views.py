from flask import Flask, request
from flask_restplus import Resource, Api, fields
from ..models.rides import rides

app = Flask(__name__)
api = Api(app)
app.config.from_pyfile('../../config.py')
obj = rides()
#models
new_ride = api.model('new_ride',{
    'name': fields.String("Name"),
    'capacity': fields.Integer("capacity"),
    'time': fields.String("time"),
    'day': fields.String("day"),
    'month': fields.String("month"),
    'year': fields.Integer("year"),
    'pick up point': fields.String("pick up point"),
    'Destination': fields.String("destination"),
    'contact': fields.String("contact")
    })
ride_request = api.model('ride_request',{
    'name': fields.String,
    'pickup time': fields.String,
    'destination': fields.String,
    'pick up point': fields.String,
    })

@api.route('/rides')
class rides(Resource):
    def get(self):
        if obj.fetch_all(obj.all_ride) == False:
        	return {'result':'There are no new rides'},404
        else:
        	return obj.all_ride,200


    @api.expect(new_ride)
    def post(self):
        obj.all_ride.append(request.get_json())
        return {'status':'Ride uploaded'}, 201


@api.route('/rides/<rideId>')
class rides_id(Resource):
    def get(self, rideId):     
        rideId =int(rideId)
    	if obj.fetch_one(rideId,obj.all_ride) == True:
    		return(obj.all_ride[rideId])
    	else:
    		return({'result':'not found'}),404


@api.route('/rides/<rideId>/requests')
class ride_requests(Resource):
    @api.expect(ride_request)
    def post(self, rideId):
        rideId =int(rideId)
        if obj.fetch_one(rideId,obj.all_ride) == True:
            obj.all_request.append(request.get_json())
            return({'result':'uploaded'})
        else:
            return({'result':'not found'}),404
