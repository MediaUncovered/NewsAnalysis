from createDatabase import createDatabase
from Model import Model
from Projector import Projector
import config
import os

def col2List(df, col):
    values = df[col].tolist()
    return [elem for elem in values if isinstance(elem, str)]

NR_DOCS=100000
name = 'Moscow_Times_' + str(NR_DOCS)
data_path ='./data/' + name + '.csv'

if not os.path.exists(data_path):
    createDatabase(config.DB, config.HOST, config.PORT, config.USER, config.PASSWORD, data_path, NR_DOCS)

model = Model(name, 'fasttext')
#model = Model(name)
if model.exists():
    model.load()
else:
    model.create(data_path)
    model.evaluate()
    model.save()

model.visualise()

maleWords = ['man', 'boy', 'brother', 'he', 'him', 'his']
femaleWords = ['woman', 'girl', 'sister', 'she', 'her', 'hers']
names = ['Kelly', 'Tracy', 'Jamie', 'Jackie', 'Taylor', 'Chris', 'Robin', 'Pat']

mapping = model.keywordMapping(names, maleWords, femaleWords)
model.plotKeywordMapping(mapping, names, 'Name Mapping')

similarWords = model.word_embedding.wv.similar_by_word('apple')



