from flask import Flask, request
from flask_restplus import Resource, Api, fields
from ..models.rides import ride,fetchRide,rideRequest

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
    'friends': fields.Integer,
    'start': fields.String,
    'finish': fields.String,
    })



@api.route('/rides')
class rides(Resource):
    def get(self):
        getRide = fetchRide()
        if getRide.emptyRide():
            return({'result':'There are no ride'},404)
        else:
            return(getRide.rideData)


    @api.expect(new_ride)
    def post(self):
        data = request.get_json()
        obj = ride(data['name'],data['start'],data['finish'],
            data['date'],data['capacity'])
        obj.add_item()
        return({'result':'Uploaded'},201)


@api.route('/rides/<rideId>')
class rides_id(Resource):
    def get(self, rideId):
        try:     
            sRide = fetchRide()
            if sRide.checkRide(rideId):
                return (sRide.rideData[int(rideId)])
            else:
                return ({'result':'unavailable'})
        except IndexError:
            return ({'result':'unavailable'},404)


@api.route('/rides/<rideId>/requests')
class ride_requests(Resource):
    @api.expect(ride_request)
    def post(self, rideId):
        data = request.get_json()
        try:
            sRide = fetchRide()
            if sRide.checkRide(rideId):
                posRide = rideRequest(data['name'],data['start'],data['finish'],data['friends'])
                posRide.add_item()
                return({'result':'uploaded'},201)
            else:
                return ({'result':'unavailable'},404)
        except IndexError:
            return ({'result':'unavailable'},404)