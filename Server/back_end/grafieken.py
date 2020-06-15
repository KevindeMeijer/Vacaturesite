import pprint
import json
import string
import re
import gensim
from gensim.parsing.preprocessing import remove_stopwords, STOPWORDS
import nltk as nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer 
from part_of_speech import get_part_of_speech
from sql_db_connectie import januari_execute, februari_execute, maart_execute, april_execute, mei_execute, juni_execute, juli_execute, augustus_execute, september_execute, oktober_execute, november_execute, december_execute

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