import unittest
import json
from app.views.views import app


class viewsTest(unittest.TestCase):
	def setUp(self):
		"""

		set up instances
		"""
		self.test = app.test_client(self)
		self.headers = {'Content-type': 'application/json'}
		self.post_ride = {
		'username': 'kwame',
		'capacity': 1,
		'time': '12:30pm',
		'date': 12,
		'month': 'june',
		'year': 2018,
		'pick up point': 'kasarani',
		'destination': 'mwiki',
		'contact': '072346582',
		'email': 'kwame@gmail.com'
		}

		self.post_ride_err = {
		'hsj': 'kwame',
		'capdsaacity': 1,
		'timeda': '12:30pm',
		'dateda': 12,
		'montdh': 'june',
		'yeasrs': 2018,
		'picsk up point': 'kasarani',
		'destscination': 'mwiki',
		'contacsdcat': '072346582',
		'email': 'kwame@gmail.com'
		}

		self.post_request = {
		'username': 'kwame',
		'pickup time': '12:30',
		'destination': 'kasarani',
		'pick up point': 'mwiki',
		}

		self.post_request_err = {
		'nssame': 'kwame',
		'pickssup time': '12:30',
		'destination': 'kasarani',
		'pick up point': 'mwiki',
		}

	def tearDown(self):
		"""

		Realese flask app instances
		"""
		self.test = None
		self.headers = None
		self.post_ride = None
		self.post_ride_err = None
		self.post_request = None
		self.post_request_err = None

	def test_all_data(self):
		"""

		test response when no rides are avialable and when there are available rides
		"""
		response = self.test.get('/rides', headers=self.headers)
		self.assertEqual(response.status_code, 404)
		self.assertIn('There are no new rides', response.data)
		response = self.test.post(
			'/rides',
			data=json.dumps(self.post_ride),
			headers=self.headers)
		response = self.test.get('/rides', headers=self.headers)
		self.assertEqual(response.status_code, 200)

	def test_single_data(self):
		"""
		test if ride account exist or not
		"""
		response = self.test.get('/ride/-3', headers=self.headers)
		self.assertEqual(response.status_code, 404)
		self.assertIn('not found', response.data)
		response = self.test.post(
			'/rides',
			data=json.dumps(self.post_ride),
			headers=self.headers)
		response = self.test.get('/rides/0', headers=self.headers)
		self.assertEqual(response.status_code, 200)

	def test_post_ride(self):
		""" 
		test of post returns 201 status code
		"""
		response = self.test.post(
			'/rides',
			data=json.dumps(self.post_ride),
			headers=self.headers)
		self.assertEqual(response.status_code, 201)

	def test_post_keys(self):
		"""
		test if user inserts an incorrect json format
		"""
		incorrect_json = {'cow': 'milk'}
		response = self.test.post(
			'/rides',
			data=json.dumps(incorrect_json),
			headers=self.headers)
		data = json.loads(response.get_data().decode('utf-8'))
		self.assertEqual(data['result'], 'Incorrect key(s) used')
		self.assertEqual(response.status_code, 400)

	def test_ride_stringData(self):
		"""
		test if user enters a string where"""
		response = self.test.post(
			'/rides',
			data=json.dumps(self.post_ride_err),
			headers=self.headers)
		data = json.loads(response.get_data().decode('utf-8'))
		self.assertEqual(
			data['result'],
			'Incorrect data type. Item should be a string')
		self.assertEqual(response.status_code, 400)

	def test_ride_intData(self):
		"""
		test for interger values
		"""
		self.post_ride['year'] = '123445'
		response = self.test.post(
			'/rides',
			data=json.dumps(self.post_ride),
			headers=self.headers)
		data = json.loads(response.get_data().decode('utf-8'))
		self.assertEqual(
			data['result'],
			'Incorrect data type. Item should be an Int')
		self.assertEqual(response.status_code, 400)

	def test_ride_email1(self):
		"""
		test for correct email format
		"""
		self.post_ride['email'] = 'asw.com'
		response = self.test.post(
			'/rides',
			data=json.dumps(self.post_ride),
			headers=self.headers)
		data = json.loads(response.get_data().decode('utf-8'))
		self.assertEqual(data['result'], 'Incorrect email format')
		self.assertEqual(response.status_code, 400)

	def test_ride_email2(self):
		"""
		test for correct email format
		"""
		self.post_ride['email'] = '@.'
		response = self.test.post(
			'/rides',
			data=json.dumps(self.post_ride),
			headers=self.headers)
		data = json.loads(response.get_data().decode('utf-8'))
		self.assertEqual(data['result'], 'Incorrect email format')
		self.assertEqual(response.status_code, 400)

	def test_ride_email3(self):
		"""
		test for correct email format
		"""
		self.post_ride['email'] = 'qwee@.'
		response = self.test.post(
			'/rides',
			data=json.dumps(self.post_ride),
			headers=self.headers)
		data = json.loads(response.get_data().decode('utf-8'))
		self.assertEqual(data['result'], 'Incorrect email format')
		self.assertEqual(response.status_code, 400)

	def test_post_ride_same_points(self):
		"""
		test whether the desitnation and the pick up point are the same
		"""
		self.post_ride['pick up point'] = 'mwiki'
		self.post_ride['destination'] = 'mwiki'
		response = self.test.post(
			'/rides',
			data=json.dumps(self.post_ride),
			headers=self.headers)
		data = json.loads(response.get_data().decode('utf-8'))
		self.assertEqual(
			data['result'],
			'destination and pick up point are identical')
		self.assertEqual(response.status_code, 400)

	def test_empty_ride(self):
		"""
		test  all the fields are not empty 
		"""
		self.post_ride['username'] = ''
		response = self.test.post(
			'/rides',
			data=json.dumps(self.post_ride),
			headers=self.headers)
		data = json.loads(response.get_data().decode('utf-8'))
		self.assertEqual(data['result'], 'All the fields are required')
		self.assertEqual(response.status_code, 405)

	def test_ride_space_only(self):
		"""
		test if user post only spaces
		"""
		self.post_ride['username'] = '   '
		response=self.test.post(
			'/rides',
			data=json.dumps(self.post_ride),
			headers=self.headers)
		data = json.loads(response.get_data().decode('utf-8'))
		self.assertEqual(response.status_code,405)
		self.assertIn(data['result'],'Input not allowed')

	def test_ride_date(self):
		"""
		test if the date of the ride is current
		"""
		self.post_ride['year'] = 1992
		response = self.test.post(
			'/rides',
			data=json.dumps(self.post_ride),
			headers=self.headers)
		data = json.loads(response.get_data().decode('utf-8'))
		self.assertEqual(data['result'], 'Incorrect date')
		self.assertEqual(response.status_code, 400)


	def test_post_request(self):
		""" 
		test status code for ride is found an when it is not
		"""
		response = self.test.post(
			'/rides/-4/requests',
			data=json.dumps(self.post_request),
			headers=self.headers)
		self.assertEqual(response.status_code, 404)
		response = self.test.post(
			'/rides',
			data=json.dumps(self.post_ride), headers=self.headers)
		response = self.test.post(
			'/rides/0/requests',
			data=json.dumps(self.post_request), headers=self.headers)
		self.assertEqual(response.status_code, 201)

	def test_empty_request(self):
		"""
		test if fields are emprty
		"""
		self.post_request['username'] = ''
		response = self.test.post(
			'/rides',
			data=json.dumps(self.post_ride),
			headers=self.headers)
		response = self.test.post(
			'/rides/-4/requests',
			data=json.dumps(self.post_request),
			headers=self.headers)
		data = json.loads(response.get_data().decode('utf-8'))
		self.assertEqual(data['result'], 'All the fields are required')
		self.assertEqual(response.status_code, 405)

	def test_request_space_only(self):
		"""
		test if user post only spaces
		"""
		self.post_request['username'] = '   '
		response = self.test.post(
			'/rides',
			data = json.dumps(self.post_request),
			headers = self.headers)
		data = json.loads(response.get_data().decode('utf-8'))
		self.assertEqual(response.status_code, 405)
		self.assertEqual(data['result'], 'Input not allowed')


	def test_request_same_point(self):
		"""
		test if destination and pick up points are alike
		"""
		self.post_request['destination'] = 'mwiki'
		self.post_request['pick up point'] = 'mwiki'
		response = self.test.post(
			'/rides',
			data=json.dumps(self.post_ride),
			headers=self.headers)
		response = self.test.post(
			'/rides/-4/requests',
			data=json.dumps(self.post_request),
			headers=self.headers)
		data = json.loads(response.get_data().decode('utf-8'))
		self.assertEqual(
			data['result'],
			'destination and pick up point are identical')
		self.assertEqual(response.status_code, 400)
