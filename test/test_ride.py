import unittest
import json
from app.views.views import app


class TestAddRide(unittest.TestCase):
	"""
	class for testing ride data
	"""
	def setUp(self):
		self.test = app.test_client()
		self.headers = {'Content-type':'application/json'}
		self.userData = {
		'start': 'kahawa',
		'finish': 'mwiki',
		'date': '1-2-2018',
		'slots': 4,
		'email': 'john@gmail.com',
		'time': '12:30:PM'
		}

	def tearDown(self):
		self.test = None
		self.headers = None
		self.userData = None

	def testEmptyStart(self):
		emptyStart = {
		'start': '',
		'finish': 'mwiki',
		'date': '1-2-2018',
		'slots': 4,
		'email': 'john@gmail.com',
		'time': '12:30:PM'
		}
		response = self.test.post('/users/rides', headers=self.headers,
			data=json.dumps(self.userData))
		data = json.loads(response.get_data().decode('utf-8'))
		self.assertEqual(response.status_code, 405)


	def testEmptyFinish(self):
		emptyStart = {
		'start': 'kahawa',
		'finish': '',
		'date': '1-2-2018',
		'slots': 4,
		'email': 'john@gmail.com',
		'time': '12:30:PM'
		}
		response = self.test.post('/users/rides', headers=self.headers,
			data=json.dumps(self.userData))
		data = json.loads(response.get_data().decode('utf-8'))
		self.assertEqual(response.status_code, 405)


	def testEmptyDate(self):
		emptyStart = {
		'start': 'kahawa',
		'finish': 'mwiki',
		'date': '',
		'slots': 4,
		'email': 'john@gmail.com',
		'time': '12:30:PM'
		}
		response = self.test.post('/users/rides', headers=self.headers,
			data=json.dumps(self.userData))
		data = json.loads(response.get_data().decode('utf-8'))
		self.assertEqual(response.status_code, 405)


	def testSlot(self):
		emptyStart = {
		'start': 'kahawa',
		'finish': 'mwiki',
		'date': '1-2-2018',
		'slots': -4,
		'email': 'john@gmail.com',
		'time': '12:30:PM'
		}
		response = self.test.post('/users/rides', headers=self.headers,
			data=json.dumps(self.userData))
		data = json.loads(response.get_data().decode('utf-8'))
		self.assertEqual(response.status_code, 405)

	def testEmail(self):
		emptyStart = {
		'start': 'kahawa',
		'finish': 'mwiki',
		'date': '1-2-2018',
		'slots': 4,
		'email': 'johngmail.co',
		'time': '12:30:PM'
		}
		response = self.test.post('/users/rides', headers=self.headers,
			data=json.dumps(self.userData))
		data = json.loads(response.get_data().decode('utf-8'))
		self.assertEqual(response.status_code, 405)

	def testTime(self):
		emptyStart = {
		'start': '',
		'finish': 'mwiki',
		'date': '1-2-2018',
		'slots': 4,
		'email': 'john@gmail.com',
		'time': '132:330:PM'
		}
		response = self.test.post('/users/rides', headers=self.headers,
			data=json.dumps(self.userData))
		data = json.loads(response.get_data().decode('utf-8'))
		self.assertEqual(response.status_code, 405)

	def testSpaceStart(self):
		emptyStart = {
		'start': '    ',
		'finish': 'mwiki',
		'date': '1-2-2018',
		'slots': 4,
		'email': 'john@gmail.com',
		'time': '12:30:PM'
		}
		response = self.test.post('/users/rides', headers=self.headers,
			data=json.dumps(self.userData))
		data = json.loads(response.get_data().decode('utf-8'))
		self.assertEqual(response.status_code, 405)

	def testSpaceFinish(self):
		emptyStart = {
		'start': 'kahawa',
		'finish': '   ',
		'date': '1-2-2018',
		'slots': 4,
		'email': 'john@gmail.com',
		'time': '12:30:PM'
		}
		response = self.test.post('/users/rides', headers=self.headers,
			data=json.dumps(self.userData))
		data = json.loads(response.get_data().decode('utf-8'))
		self.assertEqual(response.status_code, 405)
