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
        return "Error insert into db"
    finally:
        cnx.close()
    return None


def load_sql(question):
    cnx = mysql.connector.connect(**config)
    try:
        cursor = cnx.cursor()
        cursor.execute(question)
        result = cursor.fetchall()
        return result
    except:
        return "Error loading report"
    finally:
        cnx.close()
    return None
    