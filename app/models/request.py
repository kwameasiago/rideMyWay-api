import re
import datetime
from ..db.db import *


class checkRequestData:
	"""
	class to validate request data
	"""
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



class uploadRequest(checkRequestData):
	def __init__(self):
		self.data = data
		self.checkWhiteSpace = checkRequestData.checkWhiteSpace(self,self.data)
		self.checkEmptyData = checkRequestData.checkWhiteSpace(self,self.data)
		self.CheckFriends = checkRequestData(self,self.data)

	def UploadData(self):
		if self.checkEmptyData is not False:
            return self.checkEmptyData
        elif self.checkWhiteSpace is not False:
            return self.checkWhiteSpace
        else:
        	pass