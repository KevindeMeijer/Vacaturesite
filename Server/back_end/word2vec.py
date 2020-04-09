import gensim
import logging
import os
from gensim.models import Word2Vec

from sklearn.decomposition import PCA
from matplotlib import pyplot

from back_end.nosql_db_connectie import divided_sentense_vacature_list, vacature_description

logging.basicConfig(format="%(asctime)s : %(levelname)s : %(message)s, level=logging.INFO")

model = gensim.models.Word2Vec(divided_sentense_vacature_list, size=120, window=5, min_count=5, workers=4, iter=15)

model = Word2Vec.load("vacature_correlatie.model")

w1 = ["frontend"]
output = model.wv.most_similar(positive=w1, topn=5)

goede = ' '.join(map(str, output))