import pymongo
import pprint
import json

myclient = pymongo.MongoClient("mongodb+srv://JacobKrmn:root@employmentinsights-edrz0.gcp.mongodb.net/test?retryWrites=true&w=majority")

dbname = "EmploymentInsights"
mydb = myclient[dbname]

# Zien van de connectie
print(mydb)

#lijst van de collections
for coll in mydb.list_collection_names():
    print(coll)


# Krijgen van alle vacatures in de database
for post in mydb.Vacatures.find():
    pprint.pprint(post)