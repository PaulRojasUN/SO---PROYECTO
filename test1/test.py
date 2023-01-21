
import psycopg2

#establishing the connection
conn = psycopg2.connect(
   user='postgres',host='127.0.0.1', port='5432'
)
#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#cursor.execute("CREATE DATABASE hitscounter");

cursor.execute("CREATE TABLE Hits (value INT)");
cursor.execute("INSERT INTO Hits VALUES (1)");
cursor.execute("UPDATE Hits SET value=value+1");
cursor.execute("SELECT * FROM Hits");
data = cursor.fetchone()
print(data[0])
#print(cursor.fetchone())
#Executing an MYSQL function using the execute() method
#cursor.execute("select version()")

# Fetch a single row using fetchone() method.
#data = cursor.fetchone()
#print("Connection established to: ",data)

#Closing the connection
conn.close()
