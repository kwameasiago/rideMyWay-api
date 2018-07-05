import re
import datetime
from ..db.db import *


class CheckRideData:
    """
    This class contains method to check for correct ride data format
    """
    def __init__(self):
        self.dataErr = None

    def checkWhiteSpace(self, items):
        items = [items['start'], items['finish'], items['email'], items['departureDate']]
        for item in items:
            if item.isspace():
                self.dataError = {'result': 'Invalid input(Only whitespace)'}, 405
                return(self.dataError)
        return(False)

    def checkEmptyData(self, items):
        items = [items['start'], items['finish'], items['email'], items['departureDate']]
        for item in items:
            if not item:
                self.dataError = {'result': 'Invalid input (Empty data)'}, 405
                return(self.dataError)
        return False

    def checkEmail(self, items):
        items = items['email']
        match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', items)
        if match is None:
            self.dataError = {'result': 'Invalid data email'}, 405
            return(self.dataError)
        else:
            return False

    def CheckDate(self, items):
        if '-' not in items['departureDate']:
            self.dataError = {'result': 'Invalid Date'}, 405
            return(self.dataError)
        date = items['departureDate'].split('-')
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

    def CheckLocation(self, items):
        start, finish = items['start'], items['finish']
        if start == finish:
            self.dataError = {'result': 'Start point and Finish point can not be identical'}, 405
            return(self.dataError)
        else:
            return False

    def CheckSlots(self, items):
        if items['slot'] < 0:
            self.dataError = {'result': 'Invalid slot number(less than zero)'}, 405
            return(self.dataError)
        else:
            try:
                items['slot'].is_integer()
                self.dataError = {'result': 'Invalid slot number(Mast be an int)'}, 405
                return(self.dataError)
            except AttributeError:
                return(False)


class AddRide(CheckRideData):
    """
    This class Add the rides data to the database
    """
    def __init__(self, data):
        self.data = data
        self.checkWhiteSpace = CheckRideData.checkWhiteSpace(self, self.data)
        self.checkEmptyData = CheckRideData.checkEmptyData(self, self.data)
        self.checkEmail = CheckRideData.checkEmail(self, self.data)
        self.CheckDate = CheckRideData.CheckDate(self, self.data)
        self.CheckLocation = CheckRideData.CheckLocation(self, self.data)
        self.CheckSlots = CheckRideData.CheckSlots(self, self.data)


    def UploadData(self):
        if self.checkEmptyData is not False:
            return self.checkEmptyData
        elif self.checkWhiteSpace is not False:
            return self.checkWhiteSpace
        elif self.checkEmail is not False:
            return self.checkEmail
        elif self.CheckDate is not False:
            return self.CheckDate
        elif self.CheckLocation is not False:
            return self.CheckLocation
        elif self.CheckSlots is not False:
            return self.CheckSlots
        else:
            return postRide(self.data)


    def __repr__(self):
        return('AddRide ({})').format(self.data)
