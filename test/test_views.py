import unittest
from app.views.views import app
from flask import json

class viewsTest(unittest.TestCase):
	def setUp(self):
		self.test = app.test_client(self)
		self.headers={'Content-type': 'application/json'}
		self.post_ride = {
		'name': 'kwame',
		'start': 'kasarani',
		'finish': 'mwiki',
		'date': '12-2-2018',
		'capacity': 'june'
		}

		self.post_request = {
		'name': 'kwame',
		'start': '12:30',
		'finish': 'kasarani',
		'friends': 0,
		}


	def test_getRide(self):
		response = self.test.get('/rides',headers = self.headers)
		self.assertEqual(response.status_code,404)
		data = json.loads(response.get_data().decode('utf-8'))
		self.assertEqual(data['result'],'There are no ride')
		response1 = self.test.post('/rides',data=json.dumps(self.post_ride),headers = self.headers)
		response2 = self.test.get('/rides',headers = self.headers)
		self.assertEqual(response2.status_code,200)

	def test_ridePost(self):
		response = self.test.post('/rides',data=json.dumps(self.post_ride),headers = self.headers)
		self.assertEqual(response.status_code,201)

	def test_single_ride(self):
		response = self.test.get('/rides/0',headers =self.headers)
		self.assertEqual(response.status_code,200)
		response2 = self.test.get('/rides/-3',headers =self.headers)
		self.assertEqual(response2.status_code,404)

	def test_ride_request(self):
		response =self.test.post('/rides/0/requests',data = json.dumps(self.post_request),headers = self.headers)
		self.assertEqual(response.status_code,201)
		data = json.loads(response.get_data().decode('utf-8'))
		self.assertEqual(data['result'],'uploaded')

	def test_no_ride(self):
		response =self.test.post('/rides/323/requests',data = json.dumps(self.post_request),headers = self.headers)
		self.assertEqual(response.status_code,404)
		data = json.loads(response.get_data().decode('utf-8'))
		self.assertEqual(data['result'],'unavailable')
