import time

import psycopg2
from flask import Flask

app = Flask(__name__)
conn = psycopg2.connect(user='postgres', host='127.0.0.1',port='5432', password='1234')

cursor.execute("CREATE TABLE Hits (value INT)");
cursor.execute("INSERT INTO Hits VALUES (0)");

def get_hit_count_aux():
    cursor.execute("UPDATE Hits SET value=value+1");
    cursor.execute("SELECT * FROM Hits");
    data = cursor.fetchone()
    return data[0]

def get_hit_count():
    return get_hit_count_aux();
    '''
    while True:
        try:
            return get_hit_count_aux();
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)
    '''

@app.route('/')
def hello():
    count = get_hit_count()
    return 'Hello World! I have been seen {} times.\n'.format(count)
