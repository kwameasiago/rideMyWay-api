class rides:
	def __init__(self):
		self.all_ride = []
		self.all_request = []
	def add_ride(self,username,car_capacity,contact,time,date,month,year,destination,pickup):
		data = {
		'username':username,
		'car capacity':car_capacity,
		'contact':contact,
		'time':time,
		'date':date,
		'month':month,
		'year':year,
		'destination': destination,
		'pickup':pickup,
		}
		data['id'] = len(self.all_ride)
		self.all_ride.append(data)
		return True
	
	def fetch_all(self,items):
		if len(items) > 0:
			return True
		else:
			return False
	
	def fetch_one(self,id,items):
		index = 0
		while (index < len(items)):
			if int(id) == items[index]['id']:
				return True
			index = index + 1
		

	def request_ride(self,id,name,time,destination,pickup,items):
		index=0
		data ={
		'name':name,
		'time':time,
		'destination':destination,
		'pickup':pickup,
		'id':len(self.all_request)+1
		}

		while (index<len(items)):
			if id < 0:
				return False
			if id > len(items):
				return False
			if id == items[index]['id']:
				data['ride id'] = items[index]['id']
				self.all_request.append(data)
				return True
			index=index+1

"""obj = rides()
obj.add_ride('one','yesy','yesy','yesy','yesy','yesy','yesy','yesy','sd')

print(obj.fetch_all(obj.all_ride))
print(obj.fetch_one(0,obj.all_ride))
print(obj.request_ride(0,'name','time','destination','pickup',obj.all_ride))
"""