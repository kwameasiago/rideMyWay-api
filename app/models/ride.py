import re
import datetime

class CheckRideData:
    def __init__(self):
        self.DataErr = None


    def CheckEmptyData(self, items):
        items = [items['start'], items['finish'], items['email'], items['date']]
        for item in items:
            if not item:
                self.dataError = {'result':'Invalid input (Empty data)'},405
                return(self.dataError)
        return False


    def CheckwhiteSpaceData(self, items):
        items = [items['start'], items['finish'], items['email'], items['date']]
        for item in items:
            if item.isspace():
                self.dataError = {'result':'Invalid input(Only whitespace)'},405
                return(self.dataError)
        return(False)


    def CheckEmail(self, items):
        items = items
        match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$',
            items['email'])
        if match is None:
            self.dataError = {'result':'Invalid data email'},405
            return(self.dataError)
        else:
            return False


    def CheckLocation(self, items):
        start, finish = items['start'], items['finish']
        if start == finish:
            self.dataError = {'result': 'Start point and Finish point are the same'}
        else:
            return False


    def CheckDate(self, items):
        if '-' not in items['date']:
            self.dataError = {'result':'Invalid Date'},405
            return(self.dataError)
        date = items['date'].split('-')
        date = list(map(int, date))
        day,month,year = int(date[0]), int(date[1]), int(date[2])
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


    def CheckSlots(self,items):
        if items['slot'] < 0:
            self.dataError = {'result':'Invalid slot number(less than zero)'},405
            return(self.dataError)
        else:
            try:
                items['slot'].is_integer()
                self.dataError = {'result':'Invalid slot number(Mast be an int)'},405
                return(self.dataError)
            except AttributeError:
                return(False)

            



class ModifyRide(CheckRideData):
    def __init__(self,data):
        self.data = data
        self.CheckEmptyData = CheckRideData.CheckEmptyData(self, self.data)
        self.CheckwhiteSpaceData = CheckRideData.CheckwhiteSpaceData(self, self.data)
        self.CheckEmail = CheckRideData.CheckEmail(self, self.data)
        self.CheckLocation = CheckRideData.CheckLocation(self, self.data)
        self.CheckDate = CheckRideData.CheckDate(self, self.data)
        self.CheckSlots = CheckRideData.CheckSlots(self,self.data)

    def UploadRide(self):
        if self.CheckEmptyData is not False:
            return(self.CheckEmptyData)
        elif self.CheckwhiteSpaceData is not False:
            return(self.CheckwhiteSpaceData)
        elif self.CheckEmail is not False:
            return(self.CheckEmail)
        elif self.CheckLocation is not False:
            return(self.CheckLocation)
        elif self.CheckDate is not False:
            return(self.CheckDate)
        elif self.CheckSlots is not False:
            return(self.CheckSlots)
        else:
            pass
