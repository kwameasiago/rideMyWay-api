import unittest
import json
from app.views.views import app


class TestAddRequest(unittest.TestCase):
	def setUp(self):
		self.access_token = 
		self.headers = {'Content-type': 'application/json', 'Authorization': 'Bearer '+ access_token}
		self.test = app.test_client()
		self.requestData = {
		'start': 'kahawa west',
		'finish': 'nairobi cbd',
		'slot': 0,
		'departure_date': '1-2-2018',
		'email': 'alex@gmail.com'
		}

	def tearDown(self):
		self.headers = None
		self.test = None
		self.requestData = None

	def testMissingToken(self):
		"""
		test if token is missong
		"""
		response = self.test.post('/users/rides',headers=self.headers,data=json.dumps(self.requestData))
		self.assertEqual(response.status_code,401)
		data = json.loads(response.get_data().decode('utf-8'))
		self.assertEqual(data['result'],'sd')

	def testEmptyStart(self):
		"""
		test when start point is empty
		"""
		response = self.test.post('/users/rides',headers = self.headers, data = json.dumps(self.requestData))
		self.assertEqual(response.status_code,405)


	def testEmptyFinish(self):
		"""
		test when finish point is empty
		"""
		response = self.test.post('/users/rides', headers=self.headers, data=json.dumps(self.requestData))
		self.assertEqual(response.status_code,405)

	def testValueSlot(self):
		"""
		test when adding wrong slot value
		"""
		response = self.test.post('/users/rides',headers = self.headers, data = json.dumps(self.requestData))
		self.assertEqual(response.status_code,405)

	def testEmptyEmail(self):
		"""
		test when empty email
		"""
		response = self.test.post('/users/rides', headers=self.headers,data = json.dumps(self.requestData))
		self.assertEqual(response.status_code,405)

	def testEmptyDepartureDate(self):
		"""
		test when departure is empty
		"""
		response = self.test.post('/users/rides',headers=self.headers,data = json.dumps(self.requestData))
		self.assertEqual(response.status_code,405)

	def testValidEmail(self):
		"""
		test correct email formar
		"""
		response =  self.test.post('/users/rides', headers=self.headers, data=json.dumps(self.requestData))
		self.assertEqual(response.status_code,405)

	def testValidDate(self):
		"""
		test correct departure date format
		"""
		response = self.test.post('/users/rides',headers=self.headers,data=json.dumps(self.requestData))
		self.assertEqual(response.status_code,405)