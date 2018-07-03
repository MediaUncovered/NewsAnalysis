import os
import newsAnalysis.config as config
from newsAnalysis.Model import Model
from newsAnalysis.createDatabase import createDatabase


def col2List(df, col):
    values = df[col].tolist()
    return [elem for elem in values if isinstance(elem, str)]

name = 'Moscow_Times_' + str(config.NO_DOCS)
data_path ='./data/' + name + '.csv'

if not os.path.exists(data_path):
    createDatabase(config.DB, config.HOST, config.PORT, config.USER, config.PASSWORD, data_path, config.NO_DOCS)

model = Model(name, 'fasttext')

if model.exists():
    model.load()
else:
    model.create(data_path)
    model.evaluate()
    model.save()

similarWords = model.word_embedding.wv.similar_by_word('apple')
print(similarWords)
