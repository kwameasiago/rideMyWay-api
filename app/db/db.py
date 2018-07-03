import psycopg2 
con = psycopg2.connect(dbname='ride', user='postgres', host='localhost', password='python')

def insertUser(data):
	firstName,lastName,location = data['firstName'],data['lastName'],data['location']
	password ,email,dob= data['password'],data['email'],data['birthDate']
	try:
		cur = con.cursor()
		sql = "INSERT INTO users(firstName,lastName,email,password,location,birthDate) VALUES('{}','{}','{}','{}','{}','{}')".format(fistName,lastName,email,location,password,location,birthDate)
		cur.execute(sql);
		con.commit()
		con.close()
		return({'result':'account created'})
	except psycopg2.Error as e:
		con.rollback()
		return({e.pgcode:e.pgerror},500)
