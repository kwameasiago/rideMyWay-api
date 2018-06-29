import unittest
import json
from app.views.views import app


class rideTest(unittest.TestCase):
	def setUp(self):
		self.test = app.test_client()
		self.headers = {'Content-type': 'application/json'}
		self.ride = {
		'start':'kiambu',
		'finish':'mwiki',
		'capacity': 2,
		'date': '1-2-2018',
		'time':'12:20',
		'user_id':1
		}

	def testEmptyFname(self):
		"""
		test if string is empty name
		"""
		response = self.test.post('/auth/signup',
			headers=self.headers,data=json.dumps(self.ride))
		self.assertEqual(response.status_code,405)
		data = json.loads(response.get_data().decode('utf-8'))
		self.assertEqual(data['result'],'Invalid input (Empty data)')

	def testEmptyLname(self):
		"""
		test if string is empty name
		"""
		response = self.test.post('/auth/signup',
			headers=self.headers,data=json.dumps(self.ride))
		self.assertEqual(response.status_code,405)
		data = json.loads(response.get_data().decode('utf-8'))
		self.assertEqual(data['result'],'Invalid input (Empty data)')


	def testEmptyDate(self):
		"""
		test if string is empty name
		"""
		response = self.test.post('/auth/signup',
			headers=self.headers,data=json.dumps(self.ride))
		self.assertEqual(response.status_code,405)
		data = json.loads(response.get_data().decode('utf-8'))
		self.assertEqual(data['result'],'Invalid input (Empty data)')


	def testEmptyTime(self):
		"""
		test if string is empty name
		"""
		response = self.test.post('/auth/signup',
			headers=self.headers,data=json.dumps(self.ride))
		self.assertEqual(response.status_code,405)
		data = json.loads(response.get_data().decode('utf-8'))
		self.assertEqual(data['result'],'Invalid input (Empty data)')


	def testWhiteSpace(self):
		"""
		test if contains white space only
		"""
		response = self.test.post('/auth/signup',
			headers=self.headers,data=json.dumps(self.ride))
		self.assertEqual(response.status_code,405)
		data = json.loads(response.get_data().decode('utf-8'))
		self.assertEqual(data['result'],'Invalid input(Only whitespace)')


	def testSame(self):
		"""
		test if user exist
		"""
		response = self.test.post('/auth/signup',
			headers=self.headers,data=json.dumps(self.ride))
		self.assertEqual(response.status_code,405)
		data = json.loads(response.get_data().decode('utf-8'))
		self.assertEqual(data['result'],'Two rides at the same time')


	def testDate(self):
		"""
		test if user exist
		"""
		response = self.test.post('/auth/signup',
			headers=self.headers,data=json.dumps(self.ride))
		self.assertEqual(response.status_code,405)
		data = json.loads(response.get_data().decode('utf-8'))
		self.assertEqual(data['result'],'Invalid date') 




