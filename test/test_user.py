import unittest
import json
from app.views.views import app


class SignUpTest(unittest.TestCase):
	"""
	class for testing user data
	"""
	def setUp(self):
		self.userData = {
		'firstName':'kwame',
		'lastName': 'Asiago',
		'email': 'kwame@gmail.com',
		'date': '2/3/2018',
		'Location': 'kasarani'
		}
		self.test = app.test_client()
		self.headers = {'Content-type': 'application/json'}

	def tearDown(self):
		self.userData = None
		self.test = None
		self.headers = None

	def testEmptyName(self):
		"""
		test if string is empty name
		"""
		response = self.test.post('/auth/signup',
			headers=self.headers,data=json.dumps(self.userData))
		self.assertEqual(response.status_code,405)
		data = json.loads(response.get_data().decode('utf-8'))
		self.assertEqual(data['result'],'Invalid data-empty Name')

	def testEmptyDate(self):
		"""
		test if string is empty date
		"""
		response = self.test.post('/auth/signup',
			headers=self.headers,data=json.dumps(self.userData))
		self.assertEqual(response.status_code,405)
		data = json.loads(response.get_data().decode('utf-8'))
		self.assertEqual(data['result'],'Invalid data-empty date')

	def testEmptyEmail(self):
		"""
		test if string is empty email
		"""
		response = self.test.post('/auth/signup',
			headers=self.headers,data=json.dumps(self.userData))
		self.assertEqual(response.status_code,405)
		data = json.loads(response.get_data().decode('utf-8'))
		self.assertEqual(data['result'],'Invalid data-empty email')

	def testEmptyLocation(self):
		"""
		test if string is empty Location
		"""
		response = self.test.post('/auth/signup',
			headers=self.headers,data=json.dumps(self.userData))
		self.assertEqual(response.status_code,405)
		data = json.loads(response.get_data().decode('utf-8'))
		self.assertEqual(data['result'],'Invalid data-empty Loaction')

	def testEmptyPassword(self):
		"""
		test if string is empty Location
		"""
		response = self.test.post('/auth/signup',
			headers=self.headers,data=json.dumps(self.userData))
		self.assertEqual(response.status_code,405)
		data = json.loads(response.get_data().decode('utf-8'))
		self.assertEqual(data['result'],'Invalid data-empty password')

	def testEmail(self):
		"""
		test if invalid email
		"""
		response = self.test.post('/auth/signup',
			headers=self.headers,data=json.dumps(self.userData))
		self.assertEqual(response.status_code,405)
		data = json.loads(response.get_data().decode('utf-8'))
		self.assertEqual(data['result'],'Invalid data email')

	def testDate(self):
		"""
		test if invalide date
		"""
		response = self.test.post('/auth/signup',
			headers=self.headers,data=json.dumps(self.userData))
		self.assertEqual(response.status_code,405)
		data = json.loads(response.get_data().decode('utf-8'))
		self.assertEqual(data['result'],'Invalid data date')

	def testWhiteSpace(self):
		"""
		test if contains white space only
		"""
		response = self.test.post('/auth/signup',
			headers=self.headers,data=json.dumps(self.userData))
		self.assertEqual(response.status_code,405)
		data = json.loads(response.get_data().decode('utf-8'))
		self.assertEqual(data['result'],'input contains white space only')

	def testExist(self):
		"""
		test if user exist
		"""
		response = self.test.post('/auth/signup',
			headers=self.headers,data=json.dumps(self.userData))
		self.assertEqual(response.status_code,409)
		data = json.loads(response.get_data().decode('utf-8'))
		self.assertEqual(data['result'],'Email already exist')


class SignInTest(unittest.TestCase):
	def setUp(self):
		self.userData = {
		'email':'kwameasiago',
		'password':'password'
		}
		self.headers = {'Content-type':'application/json'}
		self.test = app.test_client()

	def tearDown(self):
		self.userData = None
		self.headers = None
		self.test = None

	def testEmptyEmail(self):
		"""test if email is empty
		"""
		response = self.test.post('/auth/login',
			headers=self.headers,data=json.dumps(self.userData))
		self.assertEqual(response.status_code,405)
		data = json.loads(response.get_data().decode('utf-8'))
		self.assertEqual(data['result':'Invalid data-empty email'])

	def testEmptyPassword(self):
		"""
		test if password if empty
		"""
		response = self.test.post('/auth/login',
			headers=self.headers,data=json.dumps(self.userData))
		self.assertEqual(response.status_code,405)
		data =json.loads(response.get_data().decode('utf'))
		self.assertEqual(data['result'],'Invalid data-empty password')

	def testInvalidLogIn(self):
		response = self.test.post('/auth/login',
			headers=self.headers,data=json.dumps(self.userData))
		self.assertEqual(response.status_code,405)
		data=json.loads(response.get_data.decode('utf-8'))
		assertEqual(data['result'],'Invalid password or email')