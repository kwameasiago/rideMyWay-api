import re
import datetime
from ..db.db import *


class CheckUserData:
    """
    class contains methods for data validation
    """
    def __init__(self):
        self.dataError = None

    def checkWhiteSpace(self, items):
        items = list(items.values())
        for item in items:
            if item.isspace():
                self.dataError = {'result': 'Invalid input(Only whitespace)'}, 405
                return(self.dataError)
        return(False)

    def checkEmptyData(self, items):
        items = list(items.values())
        for item in items:
            if not item:
                self.dataError = {'result': 'Invalid input (Empty data)'}, 405
                return(self.dataError)
        return False

    def checkEmail(self, items):
        items = items
        match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$',
            items['email'])
        if match is None:
            self.dataError = {'result': 'Invalid data email'}, 405
            return(self.dataError)
        else:
            return False


class Login(CheckUserData):
    """
    This class Checks login credentials and if met return Tocken 
    """
    def __init__(self, data):
        self.data = data
        self.WhiteSpace = CheckUserData.checkWhiteSpace(self, self.data)
        self.empty = CheckUserData.checkEmptyData(self, self.data)
        self.email = CheckUserData.checkEmail(self, self.data)
        self.loginUser = loginUser(self.data['email'], self.data['password'])


    def uploadData(self, token):
        if self.WhiteSpace is not False:
            return(self.WhiteSpace)
        elif self.empty is not False:
            return(self.empty)
        elif self.email is not False:
            return(self.email)
        elif self.loginUser is True:
            return({'Use token:-': token}, 200)
        else:
            return(self.loginUser)
