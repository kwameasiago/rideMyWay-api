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


    def testEmptyStart(self):
        emptyStart = {
        'start': '',
        'finish': 'mwiki',
        'friends': 4,
        'status': 'accepted'
        }
        response = self.test.post('/rides/2/requests', content_type='application/json',
            data=json.dumps(emptyStart), headers=self.headers)
        data = json.loads(response.get_data().decode('utf-8'))
        #self.assertEqual(response.status_code, 405)
        self.assertIn('Invalid input (Empty data)',data['result'])

    def testEmptyFinish(self):
        emptyFinish = {
        'start': 'mwiki',
        'finish': '',
        'friends': 4,
        'status': 'accepted'
        }
        response = self.test.post('/rides/2/requests', content_type='application/json',
            data=json.dumps(emptyFinish), headers=self.headers)
        data = json.loads(response.get_data().decode('utf-8'))
        #self.assertEqual(response.status_code, 405)
        self.assertIn('Invalid input (Empty data)',data['result'])

    def testEmptyStatus(self):
        emptyStatus = {
        'start': 'kasarani',
        'finish': 'mwiki',
        'friends': 4,
        'status': ''
        }
        response = self.test.post('/rides/2/requests', content_type='application/json',
            data=json.dumps(emptyStatus), headers=self.headers)
        data = json.loads(response.get_data().decode('utf-8'))
        #self.assertEqual(response.status_code, 405)
        self.assertIn('Invalid input (Empty data)',data['result'])

    def testSpaceStart(self):
        spaceStart = {
        'start': '   ',
        'finish': 'mwiki',
        'friends': 4,
        'status': 'accepted'
        }
        response = self.test.post('/rides/2/requests', content_type='application/json',
            data=json.dumps(spaceStart), headers=self.headers)
        data = json.loads(response.get_data().decode('utf-8'))
        #self.assertEqual(response.status_code, 405)
        self.assertIn('Invalid input(Only whitespace',data['result'])


    def testSpaceFinish(self):
        spaceFinish = {
        'start': 'mwiki',
        'finish': '   ',
        'friends': 4,
        'status': 'accepted'
        }
        response = self.test.post('/rides/2/requests', content_type='application/json',
            data=json.dumps(spaceFinish), headers=self.headers)
        data = json.loads(response.get_data().decode('utf-8'))
        #self.assertEqual(response.status_code, 405)
        self.assertIn('Invalid input(Only whitespace',data['result'])

    def testSpaceStatus(self):
        spaceStatus = {
        'start': 'kasarani',
        'finish': 'mwiki',
        'friends': 4,
        'status': '  '
        }
        response = self.test.post('/rides/2/requests', content_type='application/json',
            data=json.dumps(spaceStatus), headers=self.headers)
        data = json.loads(response.get_data().decode('utf-8'))
        #self.assertEqual(response.status_code, 405)
        self.assertIn('Invalid input(Only whitespace',data['result'])


    def testFriend(self):
        friends = {
        'start': 'kasarani',
        'finish': 'mwiki',
        'friends': -2,
        'status': 'accepted'
        }
        response = self.test.post('/rides/2/requests', content_type='application/json',
            data=json.dumps(friends), headers=self.headers)
        data = json.loads(response.get_data().decode('utf-8'))
        #self.assertEqual(response.status_code, 405)
        self.assertIn('Invalid slot number(less than zero)',data['result'])


    def testRide(self):
        friends = {
        'start': 'mwiki',
        'finish': 'mwiki',
        'friends': 4,
        'status': 'pending'
        }
        response = self.test.post('/rides/1/requests', content_type='application/json',
            data=json.dumps(friends), headers=self.headers)
        data = json.loads(response.get_data().decode('utf-8'))
        #self.assertEqual(response.status_code, 405)
        self.assertIn('Error Ride does not exist',data['result'])

    def testStatusValues(self):
        friends = {
        'start': 'kasarani',
        'finish': 'mwiki',
        'friends': 4,
        'status': 'asdfg'
        }
        response = self.test.post('/rides/2/requests', content_type='application/json',
            data=json.dumps(friends), headers=self.headers)
        data = json.loads(response.get_data().decode('utf-8'))
        #self.assertEqual(response.status_code, 405)
        self.assertIn('Invalid Status (expecting pending)',data['result'])