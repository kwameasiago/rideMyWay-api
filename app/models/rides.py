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
		return True

	def ride_exist(self,id):
		if id > len(rides.ride_data):
			return False
		elif id < 0:
			return False
		else:
			return True

	def view_ride_single(self,id):
		return rides.ride_data[id]

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

	def is_string(self,word):
		if isinstance(word,str):
			return True
		else:
			return False

	def is_Integer(self,num):
		if isinstance(num,int):
			return True
		else:
			return False

	def same_direction(self,pickup,destination):
		if pickup == destination:
			return True
		else:
			return False
	def is_empty(self,word):
		if len(word)<1:
			return False
		else:
			return True
	def only_space(self,word):
		if word.isspace():
			return True
		else:
			return False

obj = new_ride()
print(obj.isEmpty_ride_data())
print(obj.view_ride())
print(obj.add_ride('username','capacity','time','date','month','year','pickup','destination','email'))
print(obj.add_ride('kwame','capacity','time','date','month','year','pickup','destination','email'))
print(obj.view_ride())
print(obj.ride_exist(1))
print(obj.view_ride_single(1))
print(obj.key_format({'username':'username'}))
print(obj.is_string(''))
print(obj.is_Integer(1))
print(obj.same_direction('as','as'))
print(obj.is_empty(' '))
print(obj.only_space(' '))

