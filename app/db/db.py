import psycopg2
from werkzeug.security import generate_password_hash, check_password_hash


con = psycopg2.connect(dbname='ride', user='postgres', host='localhost', password='python')

# insert user data


def insertUser(data):
    firstName, lastName, location = data['firstName'], data['lastName'], data['location']
    password, email, birthDate = data['password'], data['email'], data['birthDate']
    newPassword = generate_password_hash(password, method='sha256')
    try:
        cur = con.cursor()
        sql = "INSERT INTO users "\
        "(firstName, lastName, email, location, birthDate, password) VALUES "\
        "('{}', '{}', '{}', '{}', '{}', '{}')".format(firstName, lastName, email, location, birthDate, newPassword)
        cur.execute(sql)
        con.commit()
        return({'result': 'account created'})
    except psycopg2.Error as e:
        con.rollback()
        return({e.pgcode: e.pgerror}, 500)


# check if email exist


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

# check user credentials


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


# post a ride offer


def postRide(data):
    try:
        cur = con.cursor()
        slq_id = "SELECT id FROM users WHERE email = '{}'".format(data['user_email'])
        cur.execute(slq_id)
        userId = cur.fetchone()
        userId = userId[0]
        start, finish, slot = data['start'], data['finish'], data['slot']
        email, departureDate = data['email'], data['departureDate']
        sql = "INSERT INTO rides (start, finish, slot, email, departure_date,user_id) "\
        "VALUES('{}','{}','{}','{}','{}',{})" .format(start, finish, slot, email, departureDate, userId)
        cur.execute(sql)
        con.commit()
        return({'result': 'Ride offer created'})
    except psycopg2.Error as e:
        con.rollback()
        return({e.pgcode: e.pgerror}, 500)


# get all rides


def getAllRides():
    cur = con.cursor()
    sql = "SELECT start, finish, slot, email, departure_date FROM rides"
    cur.execute(sql)
    rides = cur.fetchall()
    allRides = []
    i = 0
    while (i<len(rides)):
        allRides.append({
            'start': rides[i][0],
            'finish': rides[i][1],
            'slot':rides[i][2],
            'email': rides[i][3],
            'departure_date': rides[i][4]})
        i = i + 1
    return allRides


# get one ride


def getOneRide(rideId):
    try:
        cur = con.cursor()
        sql = "SELECT start, finish, slot, email, departure_date FROM rides WHERE id={}".format(rideId)
        cur.execute(sql)
        oneRide = cur.fetchall()
        oneRide = {
        'start': oneRide[0][0],
        'finish': oneRide[0][1],
        'slot': oneRide[0][2],
        'email': oneRide[0][3],
        'departure_date': oneRide[0][4]}
        return oneRide
    except IndexError:
        return{'result':'ride not found'}, 404