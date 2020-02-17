import requests
import json
import mysql.connector
import re

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

def getrequest(url):

    r = requests.get(url)
    response = r.json()
    return response

product_owner = getrequest("https://api.adzuna.com/v1/api/jobs/gb/search/1?app_id=61301d90&app_key=dded4a5b76451ca2c842479cc3281aaa&results_per_page=1000&what=product%20owner")

r_po = product_owner['results']

connection = mysql.connector.connect(host='localhost', user='root', passwd='titatovenaar', db='test')

for beschrijving in r_po:
    clean_desctiption = cleanhtml(str(beschrijving['description']))
    val = ('product owner', clean_desctiption)
    query = 'INSERT INTO data (catagorie, info) VALUES (%s, %s);'

    mycursor = connection.cursor()
    mycursor.execute(query, val)
    connection.commit()










