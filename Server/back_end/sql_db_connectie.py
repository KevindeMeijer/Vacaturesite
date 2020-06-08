import mysql.connector
# Verbinding met de database.
config = {
  'user': 'Alexander',
  'password': 'root',
  'host': '127.0.0.1',
  'database': 'vacaturesite',
  'raise_on_warnings': True
}

def execute_sql(sql):
    cnx = mysql.connector.connect(**config)
    try:
        cursor = cnx.cursor()
        cursor.execute(sql)
        cnx.commit()
    except:
        return "Error inserting into db"
    finally:
        cnx.close()
    return None

