import re
import datetime
from ..db.db import *


class CheckDate:
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

    def CheckDate(self, items):
        if '-' not in items['birthDate']:
            self.dataError = {'result': 'Invalid Date'}, 405
            return(self.dataError)
        date = items['birthDate'].split('-')
        date = list(map(int, date))
        day, month, year = int(date[0]), int(date[1]), int(date[2])
        ValidDate = True
        try:
            datetime.datetime(int(year), int(month), int(day))
        except ValueError:
            ValidDate = False

        if ValidDate is False:
            self.dataError = {'result': 'Invalid Date'}, 405
            return(self.dataError)
        else:
            return(False)


class Register(CheckDate):
    def __init__(self, data):
        self.data = data
        self.WhiteSpace = CheckDate.checkWhiteSpace(self, self.data)
        self.empty = CheckDate.checkEmptyData(self, self.data)
        self.email = CheckDate.checkEmail(self, self.data)
        self.date = CheckDate.CheckDate(self, self.data)
        self.emailExist = emailExist(self.data['email'])

    def uploadData(self):
        if self.WhiteSpace is not False:
            return(self.WhiteSpace)
        elif self.empty is not False:
            return(self.empty)
        elif self.email is not False:
            return(self.email)
        elif self.date is not False:
            return(self.date)
        elif self.emailExist is True:
            return({'result': 'Email already exist'}), 405
        else:
            return(insertUser(self.data))
