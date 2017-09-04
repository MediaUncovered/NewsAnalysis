from gensim.models import Word2Vec 
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
import pdb


def evaluateModel():

    evaluationFile = '../questions-words.txt'
    w2vPath = 'models/w2v_5000'

    word2vec = Word2Vec.load(w2vPath)
    accuracy = word2vec.wv.accuracy(evaluationFile, restrict_vocab=300000)


    pdb.set_trace() 


if __name__=='__main__':
    evaluateModel()
