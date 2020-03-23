import gensim
import logging
import os

import nosql_db_connectie
from nosql_db_connectie import vacature_description, vacature_title, vacatures

logging.basicConfig(format="%(asctime)s : %(levelname)s : %(message)s, level=logging.INFO")

def read_input(input_file):
    with open(input_file, 'r') as f:
        for i, line in enumerate(f):

            if (i % 100 == 0):
                logging.info("read {0} vacatures".format(i))
            
            yield gensim.utils.simple_preprocess(line)

print(read_input('vacatures'))
documents = list(read_input('vacatures'))

model = gensim.models.Word2Vec(
    documents,
    size=150,
    window=10,
    min_count=2,
    workers=10,
    iter=4)