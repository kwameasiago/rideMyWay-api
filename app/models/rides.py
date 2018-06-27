class Rides:
	'class to add new ride'	
	def __init__(self):
		self.ride_data = []
		self.request_data = []
		self.return_data = None


	def isEmpty_ride_data(self):
		if len(self.ride_data) == 0:
			return True
		else:
			return False

	def view_ride(self):
		return self.ride_data

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
		'id':len(self.ride_data)
		}
		self.ride_data.append(item)
		return {'result':'Content Uploaded'},201

	def ride_exist(self,id):
		id = int(id)
		if id > len(self.ride_data):
			return False
		elif id < 0:
			return False
		else:
			return True

	def view_ride_single(self,id):
		return self.ride_data[int(id)]

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
		'id':len(self.request_data),
		'ride_id':ride_id
		}
		self.request_data.append(item)
		return {'result':'Content Uploaded'}
