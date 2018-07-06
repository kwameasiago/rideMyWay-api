import re
import datetime
from ..db.db import *


class CheckRequestData:
    """
    class to validate request data
    """
    def checkWhiteSpace(self, items):
        items = [items['start'], items['finish'], items['status']]
        for item in items:
            if item.isspace():
                self.dataError = {'result': 'Invalid input(Only whitespace)'}, 405
                return(self.dataError)
        return(False)

    def checkEmptyData(self, items):
        items = [items['start'], items['finish'], items['status']]
        for item in items:
            if not item:
                self.dataError = {'result': 'Invalid input (Empty data)'}, 405
                return(self.dataError)
        return False

    def CheckFriendsNo(self, items):
        if items['friends'] < 0:
            self.dataError = {'result': 'Invalid slot number(less than zero)'}, 405
            return(self.dataError)
        else:
            try:
                items['friends'].is_integer()
                self.dataError = {'result': 'Invalid slot number(Mast be an int)'}, 405
                return(self.dataError)
            except AttributeError:
                return(False)


    def checkStatus(self,items):
        if items != 'pending':
            return {'result':'Invalid Status (expecting pending)'}
        else:
            return False


class UploadRequest(CheckRequestData):
    def __init__(self,data):
        self.data = data
        self.checkWhiteSpace = CheckRequestData.checkWhiteSpace(self,self.data)
        self.checkEmptyData = CheckRequestData.checkEmptyData(self,self.data)
        self.CheckFriends = CheckRequestData.CheckFriendsNo(self,self.data)
        self.checkStatus = CheckRequestData.checkStatus(self,self.data['status'])

    def uploadData(self):
        if self.checkEmptyData is not False:
            return self.checkEmptyData
        elif self.checkWhiteSpace is not False:
            return self.checkWhiteSpace
        elif self.CheckFriends is not False:
            return self.CheckFriends
        elif self.checkStatus is not False:
            return self.checkStatus
        else:
            return insertRequest(self.data)
