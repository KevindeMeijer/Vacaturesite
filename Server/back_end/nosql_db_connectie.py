import pymongo
import pprint
import json
import string
import re
from string import digits

myclient = pymongo.MongoClient("mongodb+srv://JacobKrmn:root@employmentinsights-edrz0.gcp.mongodb.net/test?retryWrites=true&w=majority")

dbname = "EmploymentInsights"
mydb = myclient[dbname]

# Zien van de connectie
print(mydb)
#De functie om alle punctuations er uit te halen.
remove_punctuations = str.maketrans('', '', string.punctuation)
remove_digits = str.maketrans('', '', digits)

vacatures = []
vacature_description = []
divided_sentense_vacature_list = []

# Krijgen van alle volledige vacatures in de database
for vacature in mydb.Vacatures.find():
    vacatures.append(vacature)

#Het splitten van beschrijvingen van alle vacatures
for description in mydb.Vacatures.find():
    sentences = description['description'].split('.')
    for sentence in sentences:
        vacature_description.append(sentence.translate(remove_punctuations).translate(remove_digits).lower())

#Het zeten vna elke sentence in een list
for divided_sentence in vacature_description:
    divided = divided_sentence.split()
    divided_sentense_vacature_list.append(divided)
