import pymongo
import pprint
import json
import string
import re

myclient = pymongo.MongoClient("mongodb+srv://JacobKrmn:root@employmentinsights-edrz0.gcp.mongodb.net/test?retryWrites=true&w=majority")

dbname = "EmploymentInsights"
mydb = myclient[dbname]

# Zien van de connectie
print(mydb)

translator = str.maketrans('', '', string.punctuation)

vacatures = []
vacature_description = []
vacature_list = []

# Krijgen van alle vacatures in de database
for post in mydb.Vacatures.find():
    vacatures.append(post)

for beschrijving in mydb.Vacatures.find():
    sentences = beschrijving['description'].split('.')
    for sentence in sentences:
        vacature_description.append(sentence.translate(translator).lower())

for losse_vacature in vacature_description:
    los = losse_vacature.split()
    vacature_list.append(los)

pprint.pprint(vacatures)
# print(vacature_list)

