class CheckRideData:
    def __init__(self):
        self.DataErr = None


    def CheckEmptyData(self, items):
        items = list(items.values())
        for item in items:
            if not item:
                self.dataError = {'result':'Invalid input (Empty data)'},405
                return(self.dataError)
        return False


    def CheckwhiteSpaceData(self, items):
        items = list(items.values())
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
        start, finish = items['start'], item['finish']
        if start == finish:
            self.dataError = {'result': 'Start point and Finish point are the same'}
        else:
            return False


    def checkDate(self, items):
        if '-' not in items['dob']:
            self.dataError = {'result':'Invalid Date'},405
            return(self.dataError)
        date = items['dob'].split('-')
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


class ModifyRide(CheckRideData):
    def __init__(self,data):
        self.data = data
        self.CheckEmptyData = CheckRideData.CheckEmptyData(self, self.data)
        self.CheckwhiteSpaceData = CheckRideData.CheckwhiteSpaceData(self, self.data)
        self.CheckEmail = CheckRideData.CheckEmail(self, self.data)
        self.CheckLocation = CheckRideData.CheckLocation(self, self.data)
        self.checkDate = CheckRideData.checkDate(self, self.data)
