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
		"username": "string",
		"capacity": 10,
		"destination": "string",
		"month": "June",
		"pickup": "sting",
		"time": "string",
		"year": 2018,
		"date": "string",
		"email": "string@gmail.com"
		}


		self.post_request = {
		"username": "",
		"pick_up_point": "string",
		"destination": "string",
		"pick_up_time": " s "
		}

	def tearDown(self):
		"""
		Realese flask app instances
		"""
		self.test = None
		self.headers = None
		self.post_ride = None


	def test_no_ride(self):
		"""
		Test status code of get  rides
		"""
		response = self.test.post('/rides',
			data=json.dumps(self.post_ride),headers=self.headers)
		self.assertEqual(response.status_code,201)
		response2 =self.test.get('/rides',headers=self.headers)
		self.assertEqual(response2.status_code,200)



	def test_single_data(self):
		"""
		test when ride account does not exist
		"""
		response = self.test.get('/rides/-34',headers=self.headers)
		self.assertEqual(response.status_code,404)
		self.assertIn('invalid ride id',response.data)

	def test_single_dataFound(self):
		"""
		test when ride account exist
		"""
		response = self.test.post('/rides',
			data=json.dumps(self.post_ride),headers=self.headers)
		response2 = self.test.get('rides/0',headers=self.headers)
		self.assertEqual(response2.status_code,200)
		self.assertIn('username',response2.data)

	def test_post_ride(self):
		"""
		test for when posting a ride
		"""
		response = self.test.post('/rides',
			data=json.dumps(self.post_ride),headers=self.headers)
		self.assertEqual(response.status_code,201)
		self.assertIn('Content Uploaded',response.data)

	def test_post_keys(self):
		"""
		test for when posting with the wrong keys
		"""
		post_ride = {
		"usernamer": 'sad',
		"capacity": 10,
		"destination": "string",
		"month": "June",
		"pickup": "strng",
		"time": "string",
		"year": 2018,
		"date": "string",
		"email": "string"
		}
		response = self.test.post('/rides',
			data=json.dumps(post_ride),headers=self.headers)
		self.assertEqual(response.status_code,403)
		self.assertIn('Incorrect key(s) used',response.data)
	

	def test_post_ride_same_points(self):
		"""
		test for when the pick up point and the destination are the same
		"""
		post_ride = {
		"username": 'sad',
		"capacity": 10,
		"destination": "string",
		"month": "June",
		"pickup": "string",
		"time": "string",
		"year": 2018,
		"date": "string",
		"email": "string"
		}
		response = self.test.post('/rides',
			data=json.dumps(post_ride),headers = self.headers)
		self.assertIn('destination and pick up point are identical',response.data)
		self.assertEqual(response.status_code,403)

	def test_empty_username(self):
		"""
		test for when user post empty data
		"""
		post_ride = {
		"username": '',
		"capacity": 10,
		"destination": "string",
		"month": "June",
		"pickup": "sting",
		"time": "string",
		"year": 2018,
		"date": "string",
		"email": "string"
		}
		response = self.test.post('/rides',
			data=json.dumps(post_ride),headers = self.headers)
		self.assertIn('All the fields are required',response.data)
		self.assertEqual(response.status_code,403)

	def test_empty_destination(self):
		"""
		test for when user post empty data
		"""
		post_ride = {
		"username": "kwam",
		"capacity": 10,
		"destination": "",
		"month": "June",
		"pickup": "sting",
		"time": "string",
		"year": 2018,
		"date": "string",
		"email": "string"
		}
		response = self.test.post('/rides',
			data=json.dumps(post_ride),headers = self.headers)
		self.assertIn('All the fields are required',response.data)
		self.assertEqual(response.status_code,403)	

	def test_empty_month(self):
		"""
		test for when user post empty data
		"""
		post_ride = {
		"username": "kwa",
		"capacity": 10,
		"destination": "string",
		"month": "",
		"pickup": "sting",
		"time": "string",
		"year": 2018,
		"date": "string",
		"email": "string"
		}
		response = self.test.post('/rides',
			data=json.dumps(post_ride),headers = self.headers)
		self.assertIn('All the fields are required',response.data)
		self.assertEqual(response.status_code,403)

	def test_empty_pickup(self):
		"""
		test for when user post empty data
		"""
		post_ride = {
		"username": "sadd",
		"capacity": 10,
		"destination": "string",
		"month": "June",
		"pickup": "",
		"time": "string",
		"year": 2018,
		"date": "string",
		"email": "string"
		}
		response = self.test.post('/rides',
			data=json.dumps(post_ride),headers = self.headers)
		self.assertIn('All the fields are required',response.data)
		self.assertEqual(response.status_code,403)

	def test_empty_time(self):
		"""
		test for when user post empty data
		"""
		post_ride = {
		"username": 'ssss',
		"capacity": 10,
		"destination": "string",
		"month": "June",
		"pickup": "sting",
		"time": "",
		"year": 2018,
		"date": "string",
		"email": "string"
		}
		response = self.test.post('/rides',
			data=json.dumps(post_ride),headers = self.headers)
		self.assertIn('All the fields are required',response.data)
		self.assertEqual(response.status_code,403)

	def test_empty_date(self):
		"""
		test for when user post empty data
		"""
		post_ride = {
		"username": 'ssss',
		"capacity": 10,
		"destination": "string",
		"month": "June",
		"pickup": "sting",
		"time": "string",
		"year": 2018,
		"date": "",
		"email": "string"
		}
		response = self.test.post('/rides',
			data=json.dumps(post_ride),headers = self.headers)
		self.assertIn('All the fields are required',response.data)
		self.assertEqual(response.status_code,403)

	def test_empty_email(self):
		"""
		test for when user post empty data
		"""
		post_ride = {
		"username": 'ssd',
		"capacity": 10,
		"destination": "string",
		"month": "June",
		"pickup": "sting",
		"time": "string",
		"year": 2018,
		"date": "string",
		"email": ""
		}
		response = self.test.post('/rides',
			data=json.dumps(post_ride),headers = self.headers)
		self.assertIn('All the fields are required',response.data)
		self.assertEqual(response.status_code,403)

	def test_correct_email(self):
		"""
		test for when user post empty data
		"""
		post_ride = {
		"username": 'ssd',
		"capacity": 10,
		"destination": "string",
		"month": "June",
		"pickup": "sting",
		"time": "string",
		"year": 2018,
		"date": "string",
		"email": "sas"
		}
		response = self.test.post('/rides',
			data=json.dumps(post_ride),headers = self.headers)
		self.assertIn('Incorrect Email',response.data)
		self.assertEqual(response.status_code,403)

	def test_correct_email2(self):
		"""
		test for when user post empty data
		"""
		post_ride = {
		"username": 'ssd',
		"capacity": 10,
		"destination": "string",
		"month": "June",
		"pickup": "sting",
		"time": "string",
		"year": 2018,
		"date": "string",
		"email": "@."
		}
		response = self.test.post('/rides',
			data=json.dumps(post_ride),headers = self.headers)
		self.assertIn('Incorrect Email',response.data)
		self.assertEqual(response.status_code,403)

	def test_ride_space_only_username(self):
		"""
		test when posting only white space
		"""
		post_ride = {
		"username": '    ',
		"capacity": 10,
		"destination": "string",
		"month": "June",
		"pickup": "sting",
		"time": "string",
		"year": 2018,
		"date": "string",
		"email": "string"
		}
		response = self.test.post('/rides',
			data=json.dumps(post_ride),headers = self.headers)
		self.assertIn('Input not allowed.white space Error',response.data)
		self.assertEqual(response.status_code,403)

	def test_ride_space_only_destination(self):
		"""
		test when posting only white space
		"""
		post_ride = {
		"username": "sdad",
		"capacity": 10,
		"destination": "    ",
		"month": "June",
		"pickup": "sting",
		"time": "string",
		"year": 2018,
		"date": "string",
		"email": "string"
		}
		response = self.test.post('/rides',
			data=json.dumps(post_ride),headers = self.headers)
		self.assertIn('Input not allowed.white space Error',response.data)
		self.assertEqual(response.status_code,403)

	def test_ride_space_only_month(self):
		"""
		test when posting only white space
		"""
		post_ride = {
		"username": "sdad",
		"capacity": 10,
		"destination": "mwiki",
		"month": "   ",
		"pickup": "sting",
		"time": "string",
		"year": 2018,
		"date": "string",
		"email": "string"
		}
		response = self.test.post('/rides',
			data=json.dumps(post_ride),headers = self.headers)
		self.assertIn('Input not allowed.white space Error',response.data)
		self.assertEqual(response.status_code,403)

	def test_ride_space_only_pickup(self):
		"""
		test when posting only white space
		"""
		post_ride = {
		"username": "sdad",
		"capacity": 10,
		"destination": "mwiki",
		"month": "kas",
		"pickup": "   ",
		"time": "string",
		"year": 2018,
		"date": "string",
		"email": "string"
		}
		response = self.test.post('/rides',
			data=json.dumps(post_ride),headers = self.headers)
		self.assertIn('Input not allowed.white space Error',response.data)
		self.assertEqual(response.status_code,403)

	def test_ride_space_only_time(self):
		"""
		test when posting only white space
		"""
		post_ride = {
		"username": "sdad",
		"capacity": 10,
		"destination": "mwiki",
		"month": "june",
		"pickup": "sting",
		"time": "   ",
		"year": 2018,
		"date": "string",
		"email": "string"
		}
		response = self.test.post('/rides',
			data=json.dumps(post_ride),headers = self.headers)
		self.assertIn('Input not allowed.white space Error',response.data)
		self.assertEqual(response.status_code,403)

	def test_ride_space_only_date(self):
		"""
		test when posting only white space
		"""
		post_ride = {
		"username": "sdad",
		"capacity": 10,
		"destination": "mwiki",
		"month": "dsa",
		"pickup": "sting",
		"time": "string",
		"year": 2018,
		"date": " ",
		"email": "string"
		}
		response = self.test.post('/rides',
			data=json.dumps(post_ride),headers = self.headers)
		self.assertIn('Input not allowed.white space Error',response.data)
		self.assertEqual(response.status_code,403)

	def test_ride_space_only_email(self):
		"""
		test when posting only white space
		"""
		post_ride = {
		"username": "sdad",
		"capacity": 10,
		"destination": "mwiki",
		"month": "sad",
		"pickup": "sting",
		"time": "string",
		"year": 2018,
		"date": "string",
		"email": "  "
		}
		response = self.test.post('/rides',
			data=json.dumps(post_ride),headers = self.headers)
		self.assertIn('Input not allowed.white space Error',response.data)
		self.assertEqual(response.status_code,403)




	def test_ride_year(self):
		post_ride = {
		"username": 'kwwame',
		"capacity": 10,
		"destination": "string",
		"month": "June",
		"pickup": "sting",
		"time": "string",
		"year": 2017,
		"date": "string",
		"email": "string"
		}
		response = self.test.post('/rides',
			data=json.dumps(post_ride),headers = self.headers)
		self.assertIn('Incorrect year',response.data)
		self.assertEqual(response.status_code,403)

	def test_post_request(self):
		response = self.test.post('/rides/-4/requests',
			data=json.dumps(self.post_request),headers = self.headers)
		self.assertIn('invalid ride id',response.data)
		self.assertEqual(response.status_code,404)

	def test_ride_capacity(self):
		post_ride = {
		"username": 'kwwame',
		"capacity": 0,
		"destination": "string",
		"month": "June",
		"pickup": "sting",
		"time": "string",
		"year": 2018,
		"date": "string",
		"email": "string"
		}
		response = self.test.post('/rides',
			data=json.dumps(post_ride),headers = self.headers)
		self.assertIn('Incorrect capacity',response.data)
		self.assertEqual(response.status_code,403)


	def test_ride_month(self):
		post_ride = {
		"username": 'kwwame',
		"capacity": 20,
		"destination": "string",
		"month": "asad",
		"pickup": "sting",
		"time": "string",
		"year": 2018,
		"date": "string",
		"email": "string"
		}
		response = self.test.post('/rides',
			data=json.dumps(post_ride),headers = self.headers)
		self.assertIn('Incorrect Month',response.data)
		self.assertEqual(response.status_code,403)

	def test_post_request(self):
		response = self.test.post('/rides/-4/requests',
			data=json.dumps(self.post_request),headers = self.headers)
		self.assertIn('invalid ride id',response.data)
		self.assertEqual(response.status_code,404)

	def test_empty_request_username(self):
		post_request = {
		"username": "",
		"pick_up_point": "string",
		"destination": "string",
		"pick_up_time": "dsas"
		}
		response = self.test.post('/rides/0/requests',
			data=json.dumps(post_request),headers = self.headers)
		self.assertIn('All the fields are required',response.data)
		self.assertEqual(response.status_code,403)

	def test_empty_request_pickup(self):
		post_request = {
		"username": "",
		"pick_up_point": "  ",
		"destination": "string",
		"pick_up_time": "sadd"
		}
		response = self.test.post('/rides/0/requests',
			data=json.dumps(post_request),headers = self.headers)
		self.assertIn('All the fields are required',response.data)
		self.assertEqual(response.status_code,403)

	def test_empty_request_destination(self):
		post_request = {
		"username": "sda",
		"pick_up_point": "string",
		"destination": "",
		"pick_up_time": "dsadsa"
		}
		response = self.test.post('/rides/0/requests',
			data=json.dumps(post_request),headers = self.headers)
		self.assertIn('All the fields are required',response.data)
		self.assertEqual(response.status_code,403)

	def test_empty_request_time(self):
		post_request = {
		"username": "sda",
		"pick_up_point": "string",
		"destination": "",
		"pick_up_time": ""
		}
		response = self.test.post('/rides/0/requests',
			data=json.dumps(post_request),headers = self.headers)
		self.assertIn('All the fields are required',response.data)
		self.assertEqual(response.status_code,403)

	def test_whitespace_request_username(self):
		post_request = {
		"username": "  ",
		"pick_up_point": "string",
		"destination": "string",
		"pick_up_time": "adxs"
		}
		response = self.test.post('/rides/0/requests',
			data=json.dumps(post_request),headers = self.headers)
		self.assertIn('Input not allowed.white space Error',response.data)
		self.assertEqual(response.status_code,403)

	def test_whitespace_request_pickup(self):
		post_request = {
		"username": "dsad",
		"pick_up_point": "    ",
		"destination": "string",
		"pick_up_time": "adxs"
		}
		response = self.test.post('/rides/0/requests',
			data=json.dumps(post_request),headers = self.headers)
		self.assertIn('Input not allowed.white space Error',response.data)
		self.assertEqual(response.status_code,403)

	def test_whitespace_request_destination(self):
		post_request = {
		"username": "sdad",
		"pick_up_point": "string",
		"destination": "  ",
		"pick_up_time": "adxs"
		}
		response = self.test.post('/rides/0/requests',
			data=json.dumps(post_request),headers = self.headers)
		self.assertIn('Input not allowed.white space Error',response.data)
		self.assertEqual(response.status_code,403)

	def test_whitespace_request_time(self):
		post_request = {
		"username": "sda",
		"pick_up_point": "string",
		"destination": "string",
		"pick_up_time": "  "
		}
		response = self.test.post('/rides/0/requests',
			data=json.dumps(post_request),headers = self.headers)
		self.assertIn('Input not allowed.white space Error',response.data)
		self.assertEqual(response.status_code,403)

	def test_request_same_points(self):
		post_request = {
		"username": "dasd",
		"pick_up_point": "string",
		"destination": "string",
		"pick_up_time": " s "
		}
		response = self.test.post('/rides/0/requests',
			data=json.dumps(post_request),headers = self.headers)
		self.assertIn('destination and pick up point are identical',response.data)
		self.assertEqual(response.status_code,403)