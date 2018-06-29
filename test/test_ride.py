import unittest
import json
from app.views.views import app


class SignUpTest(unittest.TestCase):
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
		fname={
		'fname':'',
		'lname': 'Asiago',
		'email': 'kwame@gmail.com',
		'dob': '2-3-2018',
		'Location': 'kasarani',
		'password': 'password'
		}
		response = self.test.post('/auth/signup',
			headers=self.headers,data=json.dumps(fname))
		self.assertEqual(response.status_code,405)
		data = json.loads(response.get_data().decode('utf-8'))
		self.assertEqual(data['result'],'Invalid input (Empty data)')

	def testEmptyFname(self):
		"""
		test if string is empty name
		"""
		fname={
		'fname':'kwame',
		'lname': '',
		'email': 'kwame@gmail.com',
		'dob': '2-3-2018',
		'Location': 'kasarani',
		'password': 'password'
		}
		response = self.test.post('/auth/signup',
			headers=self.headers,data=json.dumps(fname))
		self.assertEqual(response.status_code,405)
		data = json.loads(response.get_data().decode('utf-8'))
		self.assertEqual(data['result'],'Invalid input (Empty data)')
