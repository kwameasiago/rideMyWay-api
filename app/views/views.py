from flask import Flask, request
from ..models.rides import ride,fetchRide
from flask_restplus import Resource, Api, fields


app = Flask(__name__)
api = Api(app)
app.config.from_pyfile('../../config.py')




new_ride = api.model('new_ride',{
    'name': fields.String,
    'start': fields.String,
    'finish': fields.String,
    'date': fields.String,
    'capacity':fields.Integer
    })

ride_request = api.model('ride_request',{
    'name': fields.String,
    'time': fields.String,
    'start': fields.String,
    'finish': fields.String,
    })



@api.route('/rides')
class rides(Resource):
    def get(self):
        getRide = fetchRide()
        if len(getRide.rideData) == 0 :
            return({'result':'there are no ride'})
        else:
            return(getRide.rideData)


    @api.expect(new_ride)
    def post(self):
        data = request.get_json()
        obj = ride(data['name'],data['start'],data['finish'],
            data['date'],data['capacity'])
        obj.add_item()
        return(obj.rideData)


@api.route('/rides/<rideId>')
class rides_id(Resource):
    def get(self, rideId):     
        sRide = fetchRide()
        if sRide.checkRide(rideId):
            return ({'result':'unavailable'})
        else:
            return(sRide.rideData[id])


@api.route('/rides/<rideId>/requests')
class ride_requests(Resource):
    @api.expect(ride_request)
    def post(self, rideId):
        pass
