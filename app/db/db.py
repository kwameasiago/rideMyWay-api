import psycopg2
from werkzeug.security import generate_password_hash, check_password_hash


con = psycopg2.connect(dbname='ride', user='postgres', host='localhost', password='python')


def insertUser(data):
    firstName, lastName, location = data['firstName'], data['lastName'], data['location']
    password, email, birthDate = data['password'], data['email'], data['birthDate']
    newPassword = generate_password_hash(password, method='sha256')
    try:
        cur = con.cursor()
        sql = "INSERT INTO users(firstName, lastName, email, location, birthDate, password) VALUES('{}', '{}', '{}', '{}', '{}', '{}')".format(firstName, lastName, email, location, birthDate, newPassword)
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
