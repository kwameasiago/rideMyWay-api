import unittest
import json
import jwt
import datetime
import requests
from app.views.views import app


class TestAddRide(unittest.TestCase):
    """
    class for testing ride data
    """
    def setUp(self):
        self.test = app.test_client()
        self.login = {"email": "kwam@gmail.com", "password": "string"}
        self.register={
        'firstName': 'kwame',
        'lastName': 'Asiago',
        'email': 'kwam@gmail.com',
        'birthDate': '2-3-2018',
        'location': 'kasarani',
        'password': 'string'}
        postData = self.test.post('/auth/signup',content_type='application/json',
            data=json.dumps(self.register))
        response = self.test.post('/auth/login',content_type='application/json',
            data = json.dumps(self.login))
        data = json.loads(response.get_data().decode('utf-8'))
        token = data['Use token:-']
        #token = json.loads(response.data)['Use token:-']
        self.headers={"X-API-KEY": '{}'.format(token)}
        # self.token = self.data['Use token:-']
        # self.headers = {'Authorization': 'Bearer {}'.format(self.token)}


    def tearDown(self):
        self.test = None
        self.headers = None
        self.userData = None


    def test_EmptyStart(self):
        emptyStart = {
        'start': '',
        'finish': 'mwiki',
        'departureDate': '1-2-2018',
        'slot': 4,
        'email': 'john@gmail.com'
        }
        response = self.test.post('/users/rides', content_type='application/json',
            data=json.dumps(emptyStart), headers=self.headers)
        data = json.loads(response.get_data().decode('utf-8'))
        self.assertEqual(response.status_code, 405)
        self.assertIn('Invalid',data['result'])



    def testEmptyFinish(self):
        emptyFinish = {
        'start': 'kahawa',
        'finish': '',
        'departureDate': '1-2-2018',
        'slot': 4,
        'email': 'john@gmail.com'
        }
        response = self.test.post('/users/rides', content_type='application/json',
            data=json.dumps(emptyFinish), headers=self.headers)
        data = json.loads(response.get_data().decode('utf-8'))
        self.assertEqual(response.status_code, 405)
        self.assertIn('Invalid',data['result'])


    def testEmptyDate(self):
        emptyFinish = {
        'start': 'kahawa',
        'finish': 'mwiki',
        'departureDate': '',
        'slot': 4,
        'email': 'john@gmail.com'
        }
        response = self.test.post('/users/rides', content_type='application/json',
            data=json.dumps(emptyFinish), headers=self.headers)
        data = json.loads(response.get_data().decode('utf-8'))
        self.assertEqual(response.status_code, 405)
        self.assertIn('Invalid',data['result'])


    def testSlot(self):
        testSlot = {
        'start': 'kahawa',
        'finish': 'mwiki',
        'departureDate': '1-2-2018',
        'slot': -4,
        'email': 'john@gmail.com'
        }
        response = self.test.post('/users/rides', content_type='application/json',
            data=json.dumps(testSlot), headers=self.headers)
        data = json.loads(response.get_data().decode('utf-8'))
        self.assertEqual(response.status_code, 405)
        self.assertIn('Invalid slot number(less than zero)',data['result'])

    def testEmail(self):
        testEmail = {
        'start': 'kahawa',
        'finish': 'mwiki',
        'departureDate': '1-2-2018',
        'slot': 4,
        'email': 'johngmailco',
        }
        response = self.test.post('/users/rides', content_type='application/json',
            data=json.dumps(testEmail), headers=self.headers)
        data = json.loads(response.get_data().decode('utf-8'))
        token = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 405)
        self.assertIn('Invalid data email', data['result'])


    def testSpaceStart(self):
        testSpaceStart = {
        'start': '    ',
        'finish': 'mwiki',
        'departureDate': '1-2-2018',
        'slot': 4,
        'email': 'john@gmail.com',
        }
        response = self.test.post('/users/rides', content_type='application/json',
            data=json.dumps(testSpaceStart), headers=self.headers)
        data = json.loads(response.get_data().decode('utf-8'))
        self.assertEqual(response.status_code, 405)
        self.assertIn('Invalid input(Only whitespace)',data['result'])

    def testSpaceFinish(self):
        testSpaceFinish = {
        'start': 'kahawa',
        'finish': '   ',
        'departureDate': '1-2-2018',
        'slot': 4,
        'email': 'john@gmail.com',
        }
        response = self.test.post('/users/rides', content_type='application/json',
            data=json.dumps(testSpaceFinish), headers=self.headers)
        data = json.loads(response.get_data().decode('utf-8'))
        self.assertEqual(response.status_code, 405)
        self.assertIn('Invalid input(Only whitespace)',data['result'])
