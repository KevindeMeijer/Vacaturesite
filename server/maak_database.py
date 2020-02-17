import mysql.connector

connection = mysql.connector.connect(host='localhost', user = 'root', passwd = 'titatovenaar', db = 'test')

query = 'CREATE TABLE data (ID INTEGER PRIMARY KEY AUTO_INCREMENT, catagorie VARCHAR(50), beschijving VARCHAR(1000));'

mycursor = connection.cursor()
mycursor.execute(query)
connection.commit()