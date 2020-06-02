import mysql.connector
# Verbinding met de database.
config = {
  'user': 'Alexander',
  'password': 'root',
  'host': '127.0.0.1',
  'database': 'vacaturesite',
  'raise_on_warnings': True
}

cnx = mysql.connector.connect(**config)



cursor = cnx.cursor()

test = ("INSERT INTO reports "
        "(telefoonnummer, email_adres, onderwerp, bericht) "
        "VALUES (%s, %s, %s, %s)")
data = ('0612345678', 'iets@hotmail.com', 'bug', 'Het werkt niet.')  

cursor.execute(test, data)

cnx.commit()
cursor.close()
cnx.close()