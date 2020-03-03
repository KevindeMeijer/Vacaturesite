import requests
import mysql.connector
import re

def cleanhtml(raw_html):    #schoont een html tekst op van haken van tekst opmaak
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext


def getrequest(url):
    r = requests.get(url)
    response = r.json()
    return response

pagina = 0      #in het begin staat de  'teller' op 0
aantal_paginas = 5      #aantal pagina's die je wil gebruiken (kan je later veranderen)
query = 'INSERT INTO alle_data (b, results) VALUES (%s, %s);'

while pagina <= aantal_paginas:
    #50 resultaten per stuk
    alles = getrequest("https://api.adzuna.com/v1/api/jobs/gb/search/1?app_id=61301d90&app_key=dded4a5b76451ca2c842479cc3281aaa&results_per_page=1000&what=ICT")
    alles_results = alles['results']   #gebruik aleen de results van de json
    connection = mysql.connector.connect(host='localhost', user='root', passwd='titatovenaar', db='test')

    for item in alles_results:  #item is een dict met alle info per vacature
        val = ('bullshit', cleanhtml(str(item)))
        mycursor = connection.cursor()
        mycursor.execute(query, val)
        connection.commit()



    pagina += 1

