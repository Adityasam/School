import random
import string
from .models import *
from datetime import datetime, timedelta

def generate_id(length=15):
    # define the set of characters to use in the string
    characters = string.ascii_letters + string.digits

    # generate the random string
    random_string = ''.join(random.choice(characters) for i in range(length))
    return random_string

def parse_data(data):
    alldata = []
    for f in data:
        dt = {}
        fac = f.__dict__
        
        first_key = next(iter(fac))
        first_value = fac.pop(first_key)

        for field, value in fac.items():
            dt[field.lower()] = "" if value is None else value
        alldata.append(dt)

    return alldata

def parse_curser(cursor):
    alldata = []
    newdata = cursor.fetchall()
    columns = [col[0] for col in cursor.description]
    for d in newdata:
        temp = {}
        for column in columns:
            temp[column.lower()] = d[columns.index(column)] if d[columns.index(column)] is not None else ''
        alldata.append(temp)

    return alldata

def current_session():
    ses = SchoolSession.objects.filter(Deleted = False, Active=True)
    activesession = ""
    activesessionid = ""
    if len(ses) > 0:
        activesession = ses[0].Title
        activesessionid = ses[0].id
    return str(activesessionid)
