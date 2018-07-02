class ride:
	def __init__(self,name,start,finish,date,capacity):
		self.name = name
		self.start = start
		self.finish = finish,
		self.date = date
		self.capacity = capacity
	
	rideData = []
	def add_item(self):	
		payload = {
		'name':self.name,
		'start':self.start,
		'finish':self.finish,
		'date':self.date,
		'capacity':self.capacity,
		'id':len(ride.rideData)
		}

		ride.rideData.append(payload)
		return True
class rideRequest:
	def __init__(self,name,start,finish,friends):
		self.name = name
		self.start = start
		self.finish = finish,
		self.friends = friends
	
	requestData = []
	def add_item(self):	
		payload = {
		'name':self.name,
		'start':self.start,
		'finish':self.finish,
		'friends':self.friends,
		'id':len(rideRequest.requestData)
		}

		rideRequest.requestData.append(payload)
		return True


class fetchRide(ride):
	def __init__(self):
		self.rideData = ride.rideData

	def emptyRide(self):
		if len(ride.rideData) == 0:
			return True
		else:
			return False

	def checkRide(self,rid):
		data=len(ride.rideData)
		if data == 0 and int(rid) < 0:
			return False
		elif int(rid) <= data:
			return True
		else:
			return False





