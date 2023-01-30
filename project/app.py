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

@app.route('/hi')
def index():
    return "hsdsdsd!"

@app.route('/getHits', methods=['GET'])
def getHits():
    cursor.execute("SELECT * FROM Hits")
    data = cursor.fetchone()
    count = data[0]
    return 'El valor de hits es {} .\n'.format(count)

@app.route('/resetHits', methods=['DELETE'])
def resetHits():
    cursor.execute("UPDATE Hits SET value=0")
    return "se ha reseteado el valor hits, ahora es cero \n"
#EJEMPLO en una terminal a parte:  curl -i -X DELETE http://localhost:8000/resetHits

@app.route('/setHits/<int:newHits>', methods=['PUT'])
def setHits(newHits):
    hits = newHits
    cursor.execute("UPDATE Hits SET value= {}".format(hits))
    return "el valor de hits se cambio a {} \n".format(hits)
#EJEMPLO en una terminal a parte:  curl -i -X PUT http://localhost:8000/setHits/23
