import mysql.connector
import pymysql.cursors

# Verbinding met de database.
config = {
  'user': 'Alexander',
  'password': 'root',
  'host': '127.0.0.1',
  'database': 'vacaturesite',
  'raise_on_warnings': True
}
connection = pymysql.connect(host = '127.0.0.1',
                             user = 'Alexander',
                             password = 'root',
                             db = 'vacaturesite')

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
        cursor = cnx.cursor(dictionary=True)
        cursor.execute(question)
        result = cursor.fetchall()
        return result
    except:
        return "Error loading report"
    finally:
        cnx.close()
    return None

# Grafieken vullen
januari = "SELECT `job_title` FROM `vacatures` WHERE `date_added` BETWEEN '2016-01-02' AND '2016-01-03'"

februari = "SELECT `job_title` FROM `vacatures` WHERE `date_added` BETWEEN '2016-02-06' AND '2016-02-26'"

maart = "SELECT `job_title` FROM `vacatures` WHERE `date_added` BETWEEN '2016-03-05' AND '2016-03-18'"

april = "SELECT `job_title` FROM `vacatures` WHERE `date_added` BETWEEN '2016-04-10' AND '2016-04-15'"

mei = "SELECT `job_title` FROM `vacatures` WHERE `date_added` BETWEEN '2016-05-07' AND '2016-05-31'"

juni = "SELECT `job_title` FROM `vacatures` WHERE `date_added` BETWEEN '2016-06-01' AND '2016-06-30'"

juli = "SELECT `job_title` FROM `vacatures` WHERE `date_added` BETWEEN '2016-07-01' AND '2016-07-31'"

augustus = "SELECT `job_title` FROM `vacatures` WHERE `date_added` BETWEEN '2016-08-01' AND '2016-08-31'"

september = "SELECT `job_title` FROM `vacatures` WHERE `date_added` BETWEEN '2016-09-01' AND '2016-09-30'"

oktober = "SELECT `job_title` FROM `vacatures` WHERE `date_added` BETWEEN '2016-10-01' AND '2016-10-31'"

november = "SELECT `job_title` FROM `vacatures` WHERE `date_added` BETWEEN '2016-11-01' AND '2016-11-30'"

december = "SELECT `job_title` FROM `vacatures` WHERE `date_added` BETWEEN '2016-12-01' AND '2016-12-31'"

try:
    with connection.cursor() as cursor:
        cursor.execute(januari)
        januari_execute = cursor.fetchall()
        print("Januari gelukt")
    with connection.cursor() as cursor:
        cursor.execute(februari)
        februari_execute = cursor.fetchall()
        print("Februari gelukt")
    with connection.cursor() as cursor:
        cursor.execute(maart)
        maart_execute = cursor.fetchall()
        print("Maart gelukt")
    with connection.cursor() as cursor:
        cursor.execute(april)
        april_execute = cursor.fetchall()
        print("April gelukt")
    with connection.cursor() as cursor:
        cursor.execute(mei)
        mei_execute = cursor.fetchall()
        print("Mei gelukt")
    with connection.cursor() as cursor:
        cursor.execute(juni)
        juni_execute = cursor.fetchall()
        print("Juni gelukt")
    with connection.cursor() as cursor:
        cursor.execute(juli)
        juli_execute = cursor.fetchall()
        print("Juli gelukt")
    with connection.cursor() as cursor:
        cursor.execute(augustus)
        augustus_execute = cursor.fetchall()
        print("Augustus gelukt")
    with connection.cursor() as cursor:
        cursor.execute(september)
        september_execute = cursor.fetchall()
        print("September gelukt")
    with connection.cursor() as cursor:
        cursor.execute(oktober)
        oktober_execute = cursor.fetchall()
        print("Oktober gelukt")
    with connection.cursor() as cursor:
        cursor.execute(november)
        november_execute = cursor.fetchall()
        print("November gelukt")
    with connection.cursor() as cursor:
        cursor.execute(december)
        december_execute = cursor.fetchall()
        print("December gelukt")
finally:
    connection.close()
    