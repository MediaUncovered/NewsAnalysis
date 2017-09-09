from gensim.models import Word2Vec
import sys
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


def evaluateModel(nrDocs):

    evaluationFile = 'questions-words.txt'
    w2vPath = 'models/w2v_%i' % nrDocs

    word2vec = Word2Vec.load(w2vPath)
    accuracy = word2vec.wv.accuracy(evaluationFile)


if __name__=='__main__':
    nrDocs = int(sys.argv[1])
    evaluateModel(nrDocs)
