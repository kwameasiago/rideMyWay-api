import unittest
import json
from app.views.views import app


class SignUpTest(unittest.TestCase):
	"""
	class for testing user data
	"""
	def setUp(self):
		self.userData = {
		'fname':'kwame',
		'lname': 'Asiago',
		'email': 'kwame@gmail.com',
		'dob': '2-3-2018',
		'Location': 'kasarani',
		'password': 'password'
		}
		self.test = app.test_client()
		self.headers = {'Content-type': 'application/json'}

	def tearDown(self):
		self.userData = None
		self.test = None
		self.headers = None

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

	def testEmptyLname(self):
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

	def testEmptyDate(self):
		"""
		test if string is empty date
		"""
		date={
		'fname':'kwame',
		'lname': 'Asiago',
		'email': 'kwame@gmail.com',
		'dob': '',
		'Location': 'kasarani',
		'password': 'password'
		}
		response = self.test.post('/auth/signup',
			headers=self.headers,data=json.dumps(date))
		self.assertEqual(response.status_code,405)
		data = json.loads(response.get_data().decode('utf-8'))
		self.assertEqual(data['result'],'Invalid input (Empty data)')

	def testEmptyEmail(self):
		"""
		test if string is empty email
		"""
		email={
		'fname':'kwame',
		'lname': 'Asiago',
		'email': '',
		'dob': '2/3/2018',
		'Location': 'kasarani',
		'password': 'password'
		}
		response = self.test.post('/auth/signup',
			headers=self.headers,data=json.dumps(email))
		self.assertEqual(response.status_code,405)
		data = json.loads(response.get_data().decode('utf-8'))
		self.assertEqual(data['result'],'Invalid input (Empty data)')

	def testEmptyLocation(self):
		"""
		test if string is empty Location
		"""
		location={
		'fname':'kwame',
		'lname': 'Asiago',
		'email': 'kwame@gmail.com',
		'dob': '2/3/2018',
		'Location': '',
		'password': 'password'
		}
		response = self.test.post('/auth/signup',
			headers=self.headers,data=json.dumps(location))
		self.assertEqual(response.status_code,405)
		data = json.loads(response.get_data().decode('utf-8'))
		self.assertEqual(data['result'],'Invalid input (Empty data)')

	def testEmptyPassword(self):
		"""
		test if string is empty Location
		"""
		password={
		'fname':'kwame',
		'lname': 'Asiago',
		'email': 'kwame@gmail.com',
		'dob': '2/3/2018',
		'Location': 'kasarani',
		'password': ''
		}
		response = self.test.post('/auth/signup',
			headers=self.headers,data=json.dumps(password))
		self.assertEqual(response.status_code,405)
		data = json.loads(response.get_data().decode('utf-8'))
		self.assertEqual(data['result'],'Invalid input (Empty data)')

	def testEmail(self):
		"""
		test if invalid email
		"""
		email={
		'fname':'kwame',
		'lastName': 'Asiago',
		'email': '@.',
		'dob': '2/3/2018',
		'Location': 'kasarani',
		'password': 'password'
		}
		response = self.test.post('/auth/signup',
			headers=self.headers,data=json.dumps(email))
		self.assertEqual(response.status_code,405)
		data = json.loads(response.get_data().decode('utf-8'))
		self.assertEqual(data['result'],'Invalid data email')

	def testDate(self):
		"""
		test if invalide date
		"""
		date={
		'fname':'kwame',
		'lname': 'Asiago',
		'email': 'kwame@gmail.com',
		'dob': '2/33/2018',
		'Location': 'kasarani',
		'password': 'password'
		}
		response = self.test.post('/auth/signup',
			headers=self.headers,data=json.dumps(date))
		self.assertEqual(response.status_code,405)
		data = json.loads(response.get_data().decode('utf-8'))
		self.assertEqual(data['result'],'Invalid Date')

	def testWhiteSpace(self):
		"""
		test if contains white space only
		"""
		whitespace={
		'fname':' ',
		'lname': 'Asiago',
		'email': 'kwame@gmail.com',
		'dob': '2/33/2018',
		'Location': 'kasarani',
		'password': 'password'
		}
		response = self.test.post('/auth/signup',
			headers=self.headers,data=json.dumps(whitespace))
		self.assertEqual(response.status_code,405)
		data = json.loads(response.get_data().decode('utf-8'))
		self.assertEqual(data['result'],'Invalid input(Only whitespace)')

	def testExist(self):
		"""
		test if user exist
		"""
		whitespace={
		'fname':' ',
		'lname': 'Asiago',
		'email': 'kwame@gmail.com',
		'dob': '2/33/2018',
		'Location': 'kasarani',
		'password': 'password'
		}
		response = self.test.post('/auth/signup',
			headers=self.headers,data=json.dumps(self.userData))
		self.assertEqual(response.status_code,405)
		data = json.loads(response.get_data().decode('utf-8'))
		self.assertEqual(data['result'],'Email already exist')


class SignInTest(unittest.TestCase):
	def setUp(self):
		self.userData = {
		'email':'kwameasago@gmail.com',
		'password':'password'
		}
		self.headers = {'Content-type':'application/json'}
		self.test = app.test_client()

	def tearDown(self):
		self.userData = None
		self.headers = None
		self.test = None

	def testEmptyEmail2(self):
		"""test if email is empty
		"""
		empty={
		'email':'',
		'password':'password'
		}
		response = self.test.post('/auth/login',
			headers=self.headers,data=json.dumps(empty))
		self.assertEqual(response.status_code,405)

	def testEmptyPassword2(self):
		"""
		test if password if empty
		"""
		response = self.test.post('/auth/login',
			headers=self.headers,data=json.dumps(self.userData))
		self.assertEqual(response.status_code,401)
		data =json.loads(response.get_data().decode('utf-8'))
		self.assertEqual(data['result'],'Invalid email or password')

	def testInvalidLogIn(self):
		response = self.test.post('/auth/login',
			headers=self.headers,data=json.dumps(self.userData))
		self.assertEqual(response.status_code,401)
		data=json.loads(response.get_data().decode('utf-8'))
		self.assertEqual(data['result'],'Invalid email or password')

	def wrongDataType(self):
		datatype={
		'email':1,
		'password':'password'
		}
		response = self.test.post('/auth/login',
			headers=self.headers,data=json.dumps(datatype))
		self.assertEqual(response.status_code,405)
		data = json.loads(response.get_data().decode('utf-8'))
		assertEqual(data['result'],'Invalid data type')
