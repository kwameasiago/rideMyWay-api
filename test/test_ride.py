import unittest
from app.models.rides import rides


obj = rides()
class rideTest(unittest.TestCase):
	def setUp(self):
		self.ride_data = {
		'username':'kwame',
		'car capacity':3,
		'contact':'072345678',
		'time':'12:30pm',
		'date':12,
		'month':'june',
		'year':2018,
		'destination': 'kasarani',
		'pickup':'mwiki'
		}

		self.request_data = {
		'name':'kwame',
		'pickup time': '12:30pm',
		'destination': 'kasarani',
		'pick up point': 'mwiki'
		}



	#test adding a ride
	def test_adding_ride(self):
		result = self.ride_data
		self.assertTrue(obj.add_ride(
			result['username'],
			result['car capacity'],
			result['contact'],
			result['time'],
			result['date'],
			result['month'],
			result['year'],
			result['destination'],
			result['pickup']
			))
	#Happy test
	def test_username(self):
		self.assertIn('username',self.ride_data)
	
	def test_carCapacity(self):
		self.assertIn('car capacity',self.ride_data)

	def test_contact(self):
		self.assertIn('contact',self.ride_data)

	def test_time(self):
		self.assertIn('time',self.ride_data)

	def test_date(self):
		self.assertIn('date',self.ride_data)

	def test_month(self):
		self.assertIn('month',self.ride_data)

	def test_year(self):
		self.assertIn('year',self.ride_data)

	def test_destination(self):
		self.assertIn('destination',self.ride_data)

	def test_pickup(self):
		self.assertIn('pickup',self.ride_data)

	def test_emptyValue_username(self):
		result = self.ride_data['username']
		self.assertNotEqual(result,'')
	
	def test_emptyValue_carCapacity(self):
		result = self.ride_data['car capacity']
		self.assertNotEqual(result,'')

	def test_emptyValue_contact(self):
		result = self.ride_data['contact']
		self.assertNotEqual(result,'')

	def test_emptyValue_time(self):
		result = self.ride_data['time']
		self.assertNotEqual(result,'')

	def test_emptyValue_date(self):
		result = self.ride_data['date']
		self.assertNotEqual(result,'')

	def test_emptyValue_month(self):
		result = self.ride_data['month']
		self.assertNotEqual(result,'')

	def test_emptyValue_year(self):
		result = self.ride_data['year']
		self.assertNotEqual(result,'')

	def test_emptyValue_destination(self):
		result = self.ride_data['destination']
		self.assertNotEqual(result,'')

	def test_emptyValue_pickup(self):
		result = self.ride_data['pickup']
		self.assertNotEqual(result,'')

	#test fetching all data
	def test_fetchAll(self):
		self.assertTrue(obj.fetch_all(self.ride_data))

	def test_fetchOne_Is(self):
		result = self.ride_data
		obj.add_ride(
			result['username'],
			result['car capacity'],
			result['contact'],
			result['time'],
			result['date'],
			result['month'],
			result['year'],
			result['destination'],
			result['pickup']
			)
		self.assertTrue(obj.fetch_one(1,obj.all_ride))

	def test_fetchOne_Not(self):
		result = self.ride_data
		obj.add_ride(
			result['username'],
			result['car capacity'],
			result['contact'],
			result['time'],
			result['date'],
			result['month'],
			result['year'],
			result['destination'],
			result['pickup']
			)
		self.assertFalse(obj.fetch_one(-25,obj.all_ride))

	def test_adding_request(self):
		ride_data =self.ride_data
		result =self.request_data
		obj.add_ride(
			ride_data['username'],
			ride_data['car capacity'],
			ride_data['contact'],
			ride_data['time'],
			ride_data['date'],
			ride_data['month'],
			ride_data['year'],
			ride_data['destination'],
			ride_data['pickup']
			)
		self.assertTrue(obj.request_ride(
			0,
			result['name'],
			result['pickup time'],
			result['destination'],
			result['pick up point'],
			obj.all_ride
			))

	def test_adding_requestNot(self):
		ride_data =self.ride_data
		result =self.request_data
		obj.add_ride(
			ride_data['username'],
			ride_data['car capacity'],
			ride_data['contact'],
			ride_data['time'],
			ride_data['date'],
			ride_data['month'],
			ride_data['year'],
			ride_data['destination'],
			ride_data['pickup']
			)
		self.assertFalse(obj.request_ride(
			-9,
			result['name'],
			result['pickup time'],
			result['destination'],
			result['pick up point'],
			obj.all_ride
			))
