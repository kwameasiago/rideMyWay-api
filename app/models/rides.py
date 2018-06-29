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


class fetchRide(ride):
	def __init__(self):
		self.rideData = ride.rideData

	def checkRide(self,rid):
		if rid > len(self.rideData) and rid < 0:
			return False
		else:
			return True




