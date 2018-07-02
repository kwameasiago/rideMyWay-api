import psycopg2 
from  werkzeug.security import generate_password_hash , check_password_hash


con = psycopg2.connect(dbname='ride', user='postgres', host='localhost', password='python')

def insertUser(data):
	fname,lname,location = data['fname'],data['lname'],data['location']
	password ,email,dob= data['password'],data['email'],data['dob']
	newPassword = generate_password_hash(password,method='sha256')
	try:
		cur = con.cursor()
		sql = "INSERT INTO users(fname,lname,email,location,dob,password) VALUES('{}','{}','{}','{}','{}','{}')".format(fname,lname,email,location,dob,newPassword)
		cur.execute(sql);
		con.commit()
		return({'result':'account created'})
	except psycopg2.Error as e:
		con.rollback()
		return({e.pgcode:e.pgerror},500)

def emailExist(email):
	try:
		cur = con.cursor()
		sql="SELECT * FROM users WHERE EMAIL='{}'".format(email)
		cur.execute(sql)
		item = cur.fetchall()
		if item:
			return(True)
		else:
			return(False)
	except TypeError:
		return{'result':'Invalid data type'},404

def loginUser(email,password):
	try:
		cur = con.cursor()
		sql = "SELECT 	password FROM users WHERE email='{}'".format(email)
		cur.execute(sql)
		item = cur.fetchone()
		if check_password_hash(item[0],password):
			return(True)
		else:
			return(({'result':'Invalid email or password'}),401
			)
	except TypeError:
		return({'result':'Invalid email or password'}),401

