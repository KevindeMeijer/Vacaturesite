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

#1000 resultaten
back_end = getrequest("https://api.adzuna.com/v1/api/jobs/gb/search/1?app_id=61301d90&app_key=dded4a5b76451ca2c842479cc3281aaa&results_per_page=1000&what=Back%20end")
front_end = getrequest("https://api.adzuna.com/v1/api/jobs/gb/search/1?app_id=61301d90&app_key=dded4a5b76451ca2c842479cc3281aaa&results_per_page=1000&what=Front%20end")
ai = getrequest("https://api.adzuna.com/v1/api/jobs/gb/search/1?app_id=61301d90&app_key=dded4a5b76451ca2c842479cc3281aaa&results_per_page=1000&what=AI")
cloud = getrequest("https://api.adzuna.com/v1/api/jobs/gb/search/1?app_id=61301d90&app_key=dded4a5b76451ca2c842479cc3281aaa&results_per_page=1000&what=%20cloud")
product_owner = getrequest("https://api.adzuna.com/v1/api/jobs/gb/search/1?app_id=61301d90&app_key=dded4a5b76451ca2c842479cc3281aaa&results_per_page=1000&what=product%20owner")

r_be = back_end['results']
r_fr = front_end['results']
r_ai = ai['results']
r_cl = cloud['results']
r_po = product_owner['results']

connection = mysql.connector.connect(host='localhost', user='root', passwd='titatovenaar', db='test')
for item in (r_be, r_fr, r_ai, r_cl, r_po):
    c = 'ICT'
    if item == r_be:
        c = 'Back end'
    elif item == r_fr:
        c = 'Front end'
    elif item == r_ai:
        c = 'AI'
    elif item == r_cl:
        c = 'cloud'
    elif item == r_po:
        c = 'product owner'

    for beschrijving in r_ai:
        try:
            clean_desctiption = cleanhtml(str(beschrijving['description']))
            val = (c, clean_desctiption)
            print(clean_desctiption)
            query = 'INSERT INTO data (catagorie, info) VALUES (%s, %s);'

            mycursor = connection.cursor()
            mycursor.execute(query, val)
            connection.commit()
        except:
            pass











