import time
import psycopg2
from flask import Flask

app = Flask(__name__)

retries = 5
while retries != 0:
    try:
        conn = psycopg2.connect(host="postgres", user="postgres", port="5432", password="postgres")
        break
    except:
        if retries == 0:
            raise Exception("An error has occurred")
        retries -= 1
        time.sleep(0.5)

cursor = conn.cursor()

cursor.execute("CREATE TABLE Hits (value INT)")
cursor.execute("INSERT INTO Hits VALUES (0)")

def get_hit_count():
    cursor.execute("UPDATE Hits SET value=value+1")
    cursor.execute("SELECT * FROM Hits")
    data = cursor.fetchone()
    return data[0]


@app.route('/')
def hello():
    count = get_hit_count()
    return 'Hello World! I have been seen {} times.\n'.format(count)    

