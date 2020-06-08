import pymongo
import pprint
import json
import string
import re
import gensim
from gensim.parsing.preprocessing import remove_stopwords, STOPWORDS
import nltk as nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer 
from back_end.part_of_speech import get_part_of_speech

#Dit is de databaselink
myclient = pymongo.MongoClient("mongodb+srv://JacobKrmn:root@employmentinsights-edrz0.gcp.mongodb.net/test?retryWrites=true&w=majority")
dbname = "EmploymentInsights"
mydb = myclient[dbname]

# Zien van de connectie
print(mydb)

#De functie om alle punctuations er uit te halen.
remove_punctuations = str.maketrans('', '', string.punctuation)
remove_digits = str.maketrans('', '', string.digits)
all_stopwords = gensim.parsing.preprocessing.STOPWORDS
lemmatizer = WordNetLemmatizer()


vacature_description = []
divided_sentense_vacature_list = []


#Het splitten van beschrijvingen van alle vacatures
for description in mydb.Vacatures.find():
    only_description = description['description']
    without_stopwords = remove_stopwords(only_description)
    sentences = without_stopwords.split('.')
    for sentence in sentences:
        vacature_description.append(sentence.translate(remove_punctuations).translate(remove_digits).lower())

#Het zeten vna elke sentence in een list
for divided_sentence in vacature_description:
    divided = divided_sentence.split()
    new_divided = []
    for divided_word in divided:
        lemmatized_words = lemmatizer.lemmatize(divided_word, get_part_of_speech(divided_word))
        new_divided.append(lemmatized_words)
    divided_sentense_vacature_list.append(new_divided)