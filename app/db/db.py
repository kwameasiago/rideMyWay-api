import psycopg2 
con = psycopg2.connect(dbname='ride', user='postgres', host='localhost', password='python')

def insertUser(data):
	fname,lname,location = data['fname'],data['lname'],data['location']
	password ,email,dob= data['password'],data['email'],data['dob']
	try:
		cur = con.cursor()
		sql = "INSERT INTO users(fname,lname,email,password,location,dob) VALUES('{}','{}','{}','{}','{}','{}')".format(fname,lname,email,location,password,location,dob)
		cur.execute(sql);
		con.commit()
		con.close()
		return({'result':'account created'})
	except psycopg2.Error as e:
		con.rollback()
		return({e.pgcode:e.pgerror},500)
