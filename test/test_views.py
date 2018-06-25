import unittest
from flask import json
from app.views.views import app

class viewsTest(unittest.TestCase):
	def setUp(self):
		self.test = app.test_client(self)
		self.headers={'Content-type': 'application/json'}
		self.post_ride = {
		'name': 'kwame',
		'capacity': 1,
		'time': '12:30pm',
		'date': 12,
		'month': 'june',
		'year': 2018,
		'pick up point': 'kasarani',
		'destination': 'mwiki',
		'contact': '072346582'
		}

		self.post_request = {
		'name': 'kwame',
		'pickup time': '12:30',
		'destination': 'kasarani',
		'pick up point': 'mwiki',
		}

	#test status codes
	def test_rideGet(self):
		response = self.test.get('/rides',headers = self.headers)
		self.assertEqual(response.status_code,404)
		self.assertTrue('There are no new rides' in response.data)

	def test_rideGet_data(self):
		response = self.test.post('/rides',data=json.dumps(self.post_ride),headers = self.headers)
		response = self.test.get('/rides',headers = self.headers)
		self.assertEqual(response.status_code,200)
		self.assertIn('name', response.data)
		self.assertIn('capacity', response.data)
		self.assertIn('time', response.data)
		self.assertIn('date', response.data)
		self.assertIn('month', response.data)
		self.assertIn('year', response.data)
		self.assertIn('pick up point', response.data)
		self.assertIn('destination', response.data)
		self.assertIn('contact', response.data)

	def test_ridePost(self):
		response = self.test.post('/rides',data=json.dumps(self.post_ride),headers = self.headers)
		self.assertEqual(response.status_code,201)
		self.assertTrue('Ride uploaded' in response.data)

	def test_single_ride(self):
		response = self.test.get('/rides/0',headers =self.headers)
		self.assertEqual(response.status_code,200)
		self.assertEqual(response.status_code,200)
		self.assertIn('name', response.data)
		self.assertIn('capacity', response.data)
		self.assertIn('time', response.data)
		self.assertIn('date', response.data)
		self.assertIn('month', response.data)
		self.assertIn('year', response.data)
		self.assertIn('pick up point', response.data)
		self.assertIn('destination', response.data)
		self.assertIn('contact', response.data)

	def test_single_rideNot(self):
		response = self.test.get('/rides/-2',headers =self.headers)
		self.assertEqual(response.status_code,404)
		self.assertIn('not found', response.data)

	def test_ride_request(self):
		response =self.test.post('/rides/0/requests',data = json.dumps(self.post_request),headers = self.headers)
		self.assertEqual(response.status_code,201)
		self.assertIn('uploaded',response.data)


	def test_ride_requestNot(self):
		response =self.test.post('/rides/-3/requests',data = json.dumps(self.post_request),headers = self.headers)
		self.assertEqual(response.status_code,404)
		self.assertIn('not found', response.data)

	#test data 
	
