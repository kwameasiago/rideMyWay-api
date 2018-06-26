class rides:
	'class to relating to rides'
	ride_data = []
	request_data = []
	return_data = None

class new_ride(rides):
	'class to add new ride'		

	def isEmpty_ride_data(self):
		if len(rides.ride_data) == 0:
			return True
		else:
			return False

	def view_ride(self):
		return rides.ride_data

	def add_ride(self,username,capacity,time,date,month,year,pickup,destination,email):
		item = {
		'username': username,
		'capacity': capacity,
		'time': time,
		'date': date,
		'month': month,
		'year':year,
		'pickup': pickup,
		'destination': destination,
		'email': email,
		'id':len(rides.ride_data)
		}
		rides.ride_data.append(item)
		return {'result':'Content Uploaded'},201

	def ride_exist(self,id):
		id = int(id)
		if id > len(rides.ride_data):
			return False
		elif id < 0:
			return False
		else:
			return True

	def view_ride_single(self,id):
		return rides.ride_data[int(id)]

	def key_format(self,items):
		items = items.keys()
		if 'username' not in items:
			return False
		elif 'capacity' not in items:
			return False
		elif 'time' not in items:
			return False
		elif 'date' not in items:
			return False
		elif 'month' not in items:
			return False
		elif 'year' not in items:
			return False
		elif 'pickup' not in items:
			return False
		elif 'destination' not in items:
			return False
		elif 'email' not in items:
			return False
		else:
			return True

	def is_string(self,input):
		if isinstance(str(input['username']),str):
			return True
		elif isinstance(input['time'],str):
			return True
		elif isinstance(input['date'],str):
			return True
		elif isinstance(input['month'],str):
			return True
		elif isinstance(input['destination'],str):
			return True
		elif isinstance(input['email'],str):
			return True
		else:
			return False

	def is_integer(self,input):
		if isinstance(int(input['year']),int):
			return True
		elif isinstance(int(input['capacity']),int):
			return True
		else:
			return False

	def same_direction(self,pickup,destination):
		if pickup == destination:
			return True
		else:
			return False
	def is_empty(self,input):
		if len(input['username']) == 0:
			return True
		elif len(input['time']) == 0:
			return True
		elif len(input['date']) == 0:
			return True
		elif len(input['month']) == 0:
			return True
		elif len(input['pickup']) == 0:
			return True
		elif len(input['destination']) == 0:
			return True
		elif len(input['email']) == 0:
			return True
		else:
			return False

	def only_space(self,input):
		if input['username'].isspace():
			return True
		elif input['time'].isspace():
			return True
		elif input['month'].isspace():
			return True
		elif  input['pickup'].isspace():
			return True
		elif input['destination'].isspace():
			return True
		elif input['email'].isspace():
			return True
		elif input['date'].isspace():
			return True
		else:
			return False

	def correct_data(self,input):
		months = ['january', 'jebruary', 'march', 'april', 'may', 'june', 'july', 'august',
		 'september', 'october', 'november', 'december']
		if input['capacity'] < 1:
			return 'capacity'
		elif input['year'] < 2018:
			return 'year'
		elif input['month'].lower() not in months:
			return 'month'
		else:
			return True

	def key_format_request(self,items):
		items = items.keys()
		if 'username' not in items:
			return False
		elif 'pick_up_time' not in items:
			return False
		elif 'destination' not in items:
			return False
		elif 'pick_up_point' not in items:
			return False
		else:
			return True

	def is_empty_request(self,input):
		if len(input['username']) == 0:
			return True
		elif len(input['pick_up_time']) == 0:
			return True
		elif len(input['destination']) == 0:
			return True
		elif len(input['pick_up_point']) == 0:
			return True
		else:
			return False

	def only_space_request(self,input):
		if input['username'].isspace():
			return True
		elif input['pick_up_time'].isspace():
			return True
		elif input['destination'].isspace():
			return True
		elif  input['pick_up_point'].isspace():
			return True
		else:
			return False

	def is_string_request(self,input):
		if isinstance(input['username'],str):
			return True
		elif isinstance(input['pick_up_time'],str):
			return True
		elif isinstance(input['destination'],str):
			return True
		elif isinstance(input['pick_up_point'],str):
			return True
		else:
			return False

	def add_request(self,username,pick_up_time,destination,pick_up_point,ride_id):
		item = {
		'username': username,
		'pick_up_point': pick_up_time,
		'time': destination,
		'date': pick_up_point,
		'id':len(rides.request_data),
		'ride_id':ride_id
		}
		rides.request_data.append(item)
		return {'result':'Content Uploaded'}


"""obj = new_ride()
print(obj.isEmpty_ride_data())
print(obj.view_ride())
print(obj.add_ride('username','capacity','time','date','month','year','pickup','destination','email'))
print(obj.add_ride('kwame','capacity','time','date','month','year','pickup','destination','email'))
print(obj.view_ride())
print(obj.ride_exist(1))
print(obj.view_ride_single(1))
print(obj.key_format({'username':'username'}))
print(obj.same_direction('as','as'))
print(obj.is_empty(' '))
print(obj.only_space(' '))
#print(obj.is_string({'time':'234'}))
print(obj.is_integer({'capacity':1,'year':2}))"""
