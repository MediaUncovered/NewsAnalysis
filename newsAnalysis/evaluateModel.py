from gensim.models import Word2Vec
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


def evaluateModel(path):
    ''' evaluates the semantic concepts a Word2Vec model has learned based on analogies, e.g. sister:brother :: daughter:son, in specific categories (e.g. currencies, verb forms, family, country capitals, etc.) '''

    evaluationFile = 'questions-words.txt'
    word2vec = Word2Vec.load(path)

    accuracy = word2vec.wv.accuracy(evaluationFile)


