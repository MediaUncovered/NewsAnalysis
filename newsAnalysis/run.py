from createDatabase import createDatabase
from Model import Model
import config
import os


def col2list(df, col):
    values = df[col].tolist()
    return [elem for elem in values if isinstance(elem, str)]


name = 'Moscow_Times_' + str(config.NO_DOCS)
data_path = './data/' + name + '.csv'

if not os.path.exists(data_path):
    createDatabase(config.DB, config.HOST, config.PORT, config.USER, config.PASSWORD, data_path, config.NO_DOCS)

model = Model(name, 'fasttext')
if model.exists():
    model.load()
else:
    model.create(data_path)
    model.evaluate()
    model.to_tsv()
    model.save()

maleWords = ['man', 'boy', 'brother', 'he', 'him', 'his']
femaleWords = ['woman', 'girl', 'sister', 'she', 'her', 'hers']
names = ['Kelly', 'Tracy', 'Jamie', 'Jackie', 'Taylor', 'Chris', 'Robin', 'Pat']

mapping = model.keywordMapping(names, maleWords, femaleWords)
model.plotKeywordMapping(mapping, names, 'Name Mapping')

similarWords = model.word_embedding.wv.similar_by_word('Theo')
