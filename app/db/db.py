import psycopg2
from werkzeug.security import generate_password_hash, check_password_hash


con = psycopg2.connect(dbname='ride', user='postgres', host='localhost', password='python')


def insertUser(data):
    fname, lname, location = data['fname'], data['lname'], data['location']
    password, email, dob = data['password'], data['email'], data['dob']
    newPassword = generate_password_hash(password, method='sha256')
    try:
        cur = con.cursor()
        sql = "INSERT INTO users(fname, lname, email, location, dob, password) VALUES('{}', '{}', '{}', '{}', '{}', '{}')".format(fname, lname, email, location, dob, newPassword)
        cur.execute(sql)
        con.commit()
        return({'result': 'account created'})
    except psycopg2.Error as e:
        con.rollback()
        return({e.pgcode: e.pgerror}, 500)


def emailExist(email):
    try:
        cur = con.cursor()
        sql = "SELECT * FROM users WHERE EMAIL='{}'".format(email)
        cur.execute(sql)
        item = cur.fetchall()
        if item:
            return(True)
        else:
            return(False)
    except TypeError:
        return{'result': 'Invalid data type'}, 404


def getUser(self,email):
    try:
        cur = con.cursor()
        sql = "SELECT id FROM users WHERE email = '{}'".format(email)
        cur.execute(sql)
        item = cur.fetchone()
        if item:
            return item
    except:
        return({e.pgcode, e.pgerror},500)

def loginUser(email, password):
    try:
        cur = con.cursor()
        sql = "SELECT   password FROM users WHERE email='{}'".format(email)
        cur.execute(sql)
        item = cur.fetchone()
        if check_password_hash(item[0], password):
            return(True)
        else:
            return(({'result': 'Invalid email or password'}), 401)
    except TypeError:
        return({'result': 'Invalid email or password'}), 401


def insertRide(data):
    start, finish, slots = data['start'], data['finish'], data['slots']
    email, date = data['email'], data['date']
    try:
        cur = con.cursor()
        sql = "INSERT INTO rides(start, finish, slots, email, date) VALUES('{}','{}','{}','{}','{}')".format(start, finish, slots, email, date)
        cur.execute(sql)
        con.commit()
        return({'result': 'Ride offer posted'})
    except psycopg2.Error as e:
        return({e.pgcode, e.pgerror},500)

