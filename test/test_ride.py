import unittest
import json
import jwt
import datetime
from app.views.views import app


class TestAddRide(unittest.TestCase):
    """
    class for testing ride data
    """
    def setUp(self):
        self.test = app.test_client()
        self.login = {'email': 'johndoe@gmail.com','password':'string'}
        self.response = self.test.post('/auth/login',headers = {'Content-type': 'application/json'}, data=json.dumps(self.login))
        self.data = json.loads(self.response.get_data().decode('utf-8'))
        self.headers = {'Authorization': 'Bearer '+ self.data}
        self.userData = {
        'start': 'kahawa',
        'finish': 'mwiki',
        'date': '1-2-2018',
        'slot': 4,
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
        'slot': 4,
        'email': 'john@gmail.com',
        'time': '12:30:PM'
        }
        response = self.test.post('/users/rides', headers=self.headers,
            data=json.dumps(emptyStart))
        data = json.loads(response.get_data().decode('utf-8'))
        #self.assertEqual(response.status_code, 405)
        self.assertIn('error',data)
        print(self.token)


    def testEmptyFinish(self):
        emptyFinish = {
        'start': 'kahawa',
        'finish': '',
        'date': '1-2-2018',
        'slot': 4,
        'email': 'john@gmail.com',
        'time': '12:30:PM'
        }
        response = self.test.post('/users/rides', headers=self.headers,
            data=json.dumps(emptyFinish))
        data = json.loads(response.get_data().decode('utf-8'))
        #self.assertEqual(response.status_code, 405)
        self.assertIn('error',data)


    def testEmptyDate(self):
        emptyDate = {
        'start': 'kahawa',
        'finish': 'mwiki',
        'date': '',
        'slot': 4,
        'email': 'john@gmail.com',
        'time': '12:30:PM'
        }
        response = self.test.post('/users/rides', headers=self.headers,
            data=json.dumps(emptyDate))
        data = json.loads(response.get_data().decode('utf-8'))
        #self.assertEqual(response.status_code, 405)
        self.assertIn('error',data)


    def testSlot(self):
        testSlot = {
        'start': 'kahawa',
        'finish': 'mwiki',
        'date': '1-2-2018',
        'slot': -4,
        'email': 'john@gmail.com',
        'time': '12:30:PM'
        }
        response = self.test.post('/users/rides', headers=self.headers,
            data=json.dumps(testSlot))
        data = json.loads(response.get_data().decode('utf-8'))
        #self.assertEqual(response.status_code, 405)
        self.assertIn('error',data)

    def testEmail(self):
        testEmail = {
        'start': 'kahawa',
        'finish': 'mwiki',
        'date': '1-2-2018',
        'slot': 4,
        'email': 'johngmailco',
        'time': '12:30:PM'
        }
        response = self.test.post('/users/rides', headers=self.headers,
            data=json.dumps(testEmail))
        data = json.loads(response.get_data().decode('utf-8'))
        token = json.loads(response.data.decode('utf-8'))
        #self.assertEqual(response.status_code, 405)
        self.assertIn('error', data)

    def testTime(self):
        testTime = {
        'start': '',
        'finish': 'mwiki',
        'date': '1-2-2018',
        'slot': 4,
        'email': 'john@gmail.com',
        'time': '132:330:PM'
        }
        response = self.test.post('/users/rides', headers=self.headers,
            data=json.dumps(testTime))
        data = json.loads(response.get_data().decode('utf-8'))
        #self.assertEqual(response.status_code, 405)
        self.assertIn('error',data)

    def testSpaceStart(self):
        testSpaceStart = {
        'start': '    ',
        'finish': 'mwiki',
        'date': '1-2-2018',
        'slot': 4,
        'email': 'john@gmail.com',
        'time': '12:30:PM'
        }
        response = self.test.post('/users/rides', headers=self.headers,
            data=json.dumps(testSpaceStart))
        data = json.loads(response.get_data().decode('utf-8'))
        #self.assertEqual(response.status_code, 405)
        self.assertIn('error',data)

    def testSpaceFinish(self):
        testSpaceFinish = {
        'start': 'kahawa',
        'finish': '   ',
        'date': '1-2-2018',
        'slot': 4,
        'email': 'john@gmail.com',
        'time': '12:30:PM'
        }
        response = self.test.post('/users/rides', headers=self.headers,
            data=json.dumps(testSpaceFinish))
        data = json.loads(response.get_data().decode('utf-8'))
        #self.assertEqual(response.status_code, 405)
        self.assertIn('error',data)
