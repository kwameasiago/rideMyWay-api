import re, datetime, ast,json
from ..db.db import *


class checkData:
	"""
	class contains methods for data validation
	"""
	def __init__(self):
		self.dataError = None

	def checkWhiteSpace(self,items):
		items = list(items.values())
		for item in items:
			if item.isspace():
				self.dataError = {'result':'Invalid input(Only whitespace)'},405
				return(self.dataError)
		return(False)

	def checkEmptyData(self,items):
		items = list(items.values())
		for item in items:
			if not item:
				self.dataError = {'result':'Invalid input (Empty data)'},405
				return(self.dataError)
		return False

	def checkEmail(self,items):
		items = items
		match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$',
			items['email'])
		if match == None:
			self.dataError = {'result':'Invalid data email'},405
			return(self.dataError)
		else:
			return False





class Upload2(checkData):
	def __init__(self,data):
		self.data = data
		self.WhiteSpace = checkData.checkWhiteSpace(self,self.data)
		self.empty = checkData.checkEmptyData(self,self.data)
		self.email = checkData.checkEmail(self,self.data)
		self.loginUser = loginUser(self.data['email'],self.data['password'])

	def uploadData(self,token):
		if self.WhiteSpace != False:
			return(self.WhiteSpace)
		elif self.empty != False:
			return(self.empty)
		elif self.email != False:
			return(self.email)
		elif self.loginUser == True:
			return({'token':token},201)
		else:
			return(self.loginUser)




			




