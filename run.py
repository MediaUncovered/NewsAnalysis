import os
import newsAnalysis.config as config
from newsAnalysis.Model import Model
from newsAnalysis.createDatabase import createDatabase

name = 'Moscow_Times_' + str(config.NO_DOCS)
model_type = 'word2vec'

data_path ='./data/' + name + '.csv'


if not os.path.exists(data_path):
    createDatabase(config.DB, config.HOST, config.PORT, config.USER, config.PASSWORD, data_path, config.NO_DOCS)

model = Model(name, model_type)

if model.exists():
    model_path = model.model_path
    model = model.load(model_path=model_path)
else:
    model.create(data_path, modelName=name, modelType=model_type)
    model.evaluate()
    model.save()

    model_path = model.model_path
    model = model.load(model_path=model_path)


similarWords = model.word_embedding.wv.similar_by_word('negative')
print(similarWords)

analogies = model.generate_analogies('she', 'he', 1000)
