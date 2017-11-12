from gensim.models import Word2Vec
import sys
import pdb
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


def evaluateModel(path):

    evaluationFile = 'questions-words.txt'
    word2vec = Word2Vec.load(path)
    accuracy = word2vec.wv.accuracy(evaluationFile)



if __name__=='__main__':
    modelPath = int(sys.argv[1])
    evaluateModel(modelPath)
