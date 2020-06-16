# import pprint
# import json
import string
# import re
import gensim
from gensim.parsing.preprocessing import remove_stopwords, STOPWORDS
import nltk as nltk
from nltk.tokenize import word_tokenize
# from nltk.stem import WordNetLemmatizer 
# from part_of_speech import get_part_of_speech
from back_end.sql_db_connectie import januari_execute, februari_execute, maart_execute, april_execute, mei_execute, juni_execute, juli_execute, augustus_execute, september_execute, oktober_execute, november_execute, december_execute

remove_punctuations = str.maketrans('', '', string.punctuation)
remove_digits = str.maketrans('', '', string.digits)
all_stopwords = gensim.parsing.preprocessing.STOPWORDS

januari_titles = []
februari_titles = []
maart_titles = []
april_titles = []
mei_titles = []
juni_titles = []
juli_titles = []
augustus_titles = []
september_titles = []
oktober_titles = []
november_titles = []
december_titles = []
# Alle titels van de vacatures in een list zettten
# Januari
for title_jan in januari_execute:
    titels_jan = "".join(title_jan).lower().translate(remove_punctuations).translate(remove_digits)
    tokenized_jan = word_tokenize(titels_jan)
    januari_titles.append(tokenized_jan)
# Februari
for title_feb in februari_execute:
    titels_feb = "".join(title_feb).lower().translate(remove_punctuations).translate(remove_digits)
    tokenized_feb = word_tokenize(titels_feb)
    februari_titles.append(tokenized_feb)
# Maart
for title_mrt in maart_execute:
    titels_mrt = "".join(title_mrt).lower().translate(remove_punctuations).translate(remove_digits)
    tokenized_mrt = word_tokenize(titels_mrt)
    maart_titles.append(tokenized_mrt)
# April
for title_apr in april_execute:
    titels_apr = "".join(title_apr).lower().translate(remove_punctuations).translate(remove_digits)
    tokenized_apr = word_tokenize(titels_apr)
    april_titles.append(tokenized_apr)
# Mei 
for title_mei in mei_execute:
    titels_mei = "".join(title_mei).lower().translate(remove_punctuations).translate(remove_digits)
    tokenized_mei = word_tokenize(titels_mei)
    mei_titles.append(tokenized_mei)
# Juni 
for title_jun in juni_execute:
    titels_jun = "".join(title_jun).lower().translate(remove_punctuations).translate(remove_digits)
    tokenized_jun = word_tokenize(titels_jun)
    juni_titles.append(tokenized_jun)
# Juli 
for title_jul in juli_execute:
    titels_jul = "".join(title_jul).lower().translate(remove_punctuations).translate(remove_digits)
    tokenized_jul = word_tokenize(titels_jul)
    juli_titles.append(tokenized_jul)
# Augustus
for title_aug in augustus_execute:
    titels_aug = "".join(title_aug).lower().translate(remove_punctuations).translate(remove_digits)
    tokenized_aug = word_tokenize(titels_aug)
    augustus_titles.append(tokenized_aug) 
# September 
for title_sep in september_execute:
    titels_sep = "".join(title_sep).lower().translate(remove_punctuations).translate(remove_digits)
    tokenized_sep = word_tokenize(titels_sep)
    september_titles.append(tokenized_sep)
# Oktober
for title_okt in oktober_execute:
    titels_okt = "".join(title_okt).lower().translate(remove_punctuations).translate(remove_digits)
    tokenized_okt = word_tokenize(titels_okt)
    oktober_titles.append(tokenized_okt) 
# November 
for title_nov in november_execute:
    titels_nov = "".join(title_nov).lower().translate(remove_punctuations).translate(remove_digits)
    tokenized_nov = word_tokenize(titels_nov)
    november_titles.append(tokenized_nov)
# December 
for title_dec in december_execute:
    titels_dec = "".join(title_dec).lower().translate(remove_punctuations).translate(remove_digits)
    tokenized_dec = word_tokenize(titels_dec)
    december_titles.append(tokenized_dec)

jan_goed = []
feb_goed = []
mrt_goed = []
apr_goed = []
mei_goed = []
jun_goed = []
jul_goed = []
aug_goed = []
sep_goed = []
okt_goed = []
nov_goed = []
dec_goed = []
# Verwijderen van nestend listen
def removelist_jan(jan):
    for i in jan:
        if type(i) == list:
            removelist_jan(i)
        else:
            jan_goed.append(i)
def removelist_feb(feb):
    for i in feb:
        if type(i) == list:
            removelist_feb(i)
        else:
            feb_goed.append(i)
def removelist_mrt(mrt):
    for i in mrt:
        if type(i) == list:
            removelist_mrt(i)
        else:
            mrt_goed.append(i)
def removelist_apr(apr):
    for i in apr:
        if type(i) == list:
            removelist_apr(i)
        else:
            apr_goed.append(i)
def removelist_mei(mei):
    for i in mei:
        if type(i) == list:
            removelist_mei(i)
        else:
            mei_goed.append(i)
def removelist_jun(jun):
    for i in jun:
        if type(i) == list:
            removelist_jun(i)
        else:
            jun_goed.append(i)
def removelist_jul(jul):
    for i in jul:
        if type(i) == list:
            removelist_jul(i)
        else:
            jul_goed.append(i)
def removelist_aug(aug):
    for i in aug:
        if type(i) == list:
            removelist_aug(i)
        else:
            aug_goed.append(i)
def removelist_sep(sep):
    for i in sep:
        if type(i) == list:
            removelist_sep(i)
        else:
            sep_goed.append(i)
def removelist_okt(okt):
    for i in okt:
        if type(i) == list:
            removelist_okt(i)
        else:
            okt_goed.append(i)
def removelist_nov(nov):
    for i in nov:
        if type(i) == list:
            removelist_nov(i)
        else:
            nov_goed.append(i)
def removelist_dec(dec):
    for i in dec:
        if type(i) == list:
            removelist_dec(i)
        else:
            dec_goed.append(i)

removelist_jan(januari_titles)
removelist_feb(februari_titles)
removelist_mrt(maart_titles)
removelist_apr(april_titles)
removelist_mei(mei_titles)
removelist_jun(juni_titles)
removelist_jul(juli_titles)
removelist_aug(augustus_titles)
removelist_sep(september_titles)
removelist_okt(oktober_titles)
removelist_nov(november_titles)
removelist_dec(december_titles)

# Vacatures per maand
jan_frontend = 0
jan_backend = 0
jan_productowner = 0
jan_cloud_security = 0

feb_frontend = 0
feb_backend = 0
feb_productowner = 0
feb_cloud_security = 0

mrt_frontend = 0
mrt_backend = 0
mrt_productowner = 0
mrt_cloud_security = 0

apr_frontend = 0
apr_backend = 0
apr_productowner = 0
apr_cloud_security = 0

mei_frontend = 0
mei_backend = 0
mei_productowner = 0
mei_cloud_security = 0

jun_frontend = 0
jun_backend = 0
jun_productowner = 0
jun_cloud_security = 0

jul_frontend = 0
jul_backend = 0
jul_productowner = 0
jul_cloud_security = 0

aug_frontend = 0
aug_backend = 0
aug_productowner = 0
aug_cloud_security = 0

sep_frontend = 0
sep_backend = 0
sep_productowner = 0
sep_cloud_security = 0

okt_frontend = 0
okt_backend = 0
okt_productowner = 0
okt_cloud_security = 0

nov_frontend = 0
nov_backend = 0
nov_productowner = 0
nov_cloud_security = 0

dec_frontend = 0
dec_backend = 0
dec_productowner = 0
dec_cloud_security = 0
# Januari
for word in jan_goed:
    if word == "frontend":
        jan_frontend += 1
    elif word == "webdeveloper":
        jan_frontend += 1
    elif word == "backend":
        jan_backend += 1
    elif word == "business":
        jan_productowner += 1
    elif word == "cloud":
        jan_cloud_security += 1
    elif word == "security":
        jan_cloud_security += 1
# Februari
for word in feb_goed:
    if word == "frontend":
        feb_frontend += 1
    elif word == "webdeveloper":
        feb_frontend += 1
    elif word == "backend":
        feb_backend += 1
    elif word == "business":
        feb_productowner += 1
    elif word == "cloud":
        feb_cloud_security += 1
    elif word == "security":
        feb_cloud_security += 1
# Maart 
for word in mrt_goed:
    if word == "frontend":
        mrt_frontend += 1
    elif word == "webdeveloper":
        mrt_frontend += 1
    elif word == "backend":
        mrt_backend += 1
    elif word == "business":
        mrt_productowner += 1
    elif word == "cloud":
        mrt_cloud_security += 1
    elif word == "security":
        mrt_cloud_security += 1
# April 
for word in apr_goed:
    if word == "frontend":
        apr_frontend += 1
    elif word == "webdeveloper":
        apr_frontend += 1
    elif word == "backend":
        apr_backend += 1
    elif word == "business":
        apr_productowner += 1
    elif word == "cloud":
        apr_cloud_security += 1
    elif word == "security":
        apr_cloud_security += 1
# Mei 
for word in mei_goed:
    if word == "frontend":
        mei_frontend += 1
    elif word == "webdeveloper":
        mei_frontend += 1
    elif word == "backend":
        mei_backend += 1
    elif word == "business":
        mei_productowner += 1
    elif word == "cloud":
        mei_cloud_security += 1
    elif word == "security":
        mei_cloud_security += 1
# Juni 
for word in jun_goed:
    if word == "frontend":
        jun_frontend += 1
    elif word == "webdeveloper":
        jun_frontend += 1
    elif word == "backend":
        jun_backend += 1
    elif word == "business":
        jun_productowner += 1
    elif word == "cloud":
        jun_cloud_security += 1
    elif word == "security":
        jun_cloud_security += 1
# Juli 
for word in jul_goed:
    if word == "frontend":
        jul_frontend += 1
    elif word == "webdeveloper":
        jul_frontend += 1
    elif word == "backend":
        jul_backend += 1
    elif word == "business":
        jul_productowner += 1
    elif word == "cloud":
        jul_cloud_security += 1
    elif word == "security":
        jul_cloud_security += 1
# Augustus 
for word in aug_goed:
    if word == "frontend":
        aug_frontend += 1
    elif word == "webdeveloper":
        aug_frontend += 1
    elif word == "backend":
        aug_backend += 1
    elif word == "business":
        aug_productowner += 1
    elif word == "cloud":
        aug_cloud_security += 1
    elif word == "security":
        aug_cloud_security += 1
# September 
for word in sep_goed:
    if word == "frontend":
        sep_frontend += 1
    elif word == "webdeveloper":
        sep_frontend += 1
    elif word == "backend":
        sep_backend += 1
    elif word == "business":
        sep_productowner += 1
    elif word == "cloud":
        sep_cloud_security += 1
    elif word == "security":
        sep_cloud_security += 1
# Oktober 
for word in okt_goed:
    if word == "frontend":
        okt_frontend += 1
    elif word == "webdeveloper":
        okt_frontend += 1
    elif word == "backend":
        okt_backend += 1
    elif word == "business":
        okt_productowner += 1
    elif word == "cloud":
        okt_cloud_security += 1
    elif word == "security":
        okt_cloud_security += 1
# November 
for word in nov_goed:
    if word == "frontend":
        nov_frontend += 1
    elif word == "webdeveloper":
        nov_frontend += 1
    elif word == "backend":
        nov_backend += 1
    elif word == "business":
        nov_productowner += 1
    elif word == "cloud":
        nov_cloud_security += 1
    elif word == "security":
        nov_cloud_security += 1
# December 
for word in dec_goed:
    if word == "frontend":
        dec_frontend += 1
    elif word == "webdeveloper":
        dec_frontend += 1
    elif word == "backend":
        dec_backend += 1
    elif word == "business":
        dec_productowner += 1
    elif word == "cloud":
        dec_cloud_security += 1
    elif word == "security":
        dec_cloud_security += 1