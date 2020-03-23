import pymongo
import pprint
import json

myclient = pymongo.MongoClient("mongodb+srv://JacobKrmn:root@employmentinsights-edrz0.gcp.mongodb.net/test?retryWrites=true&w=majority")

dbname = "EmploymentInsights"
mydb = myclient[dbname]

# Zien van de connectie
print(mydb)

#lijst van de collections
# for coll in mydb.list_collection_names():
#     print(coll)

vacatures = []
# Krijgen van alle vacatures in de database
for post in mydb.Vacatures.find():
    vacatures.append(post)

vacature_title = []
vacature_description = []


een_vacature = mydb.Vacatures.find_one()
goed = een_vacature["id"]
print(een_vacature["id"])


for titel in mydb.Vacatures.find():
    vacature_title.append(titel['title'])

for beschrijving in mydb.Vacatures.find():
    vacature_description.append(beschrijving['description'])

