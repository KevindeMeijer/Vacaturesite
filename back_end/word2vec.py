import gensim
import logging
import os
import sys

sys.path.append("..")
from nosql_db_connectie import vacature_lijst
# import nosql_db_connectie

logging.basicConfig(format="%(asctime)s : %(levelname)s : %(message)s, level=logging.INFO")


model = gensim.models.Word2Vec(
    vacature_lijst,
    size=150,
    window=10,
    min_count=2,
    workers=10,
    iter=4)