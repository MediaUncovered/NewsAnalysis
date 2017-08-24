from gensim.models import Word2Vec 
import pdb


def evaluateModel():

    evaluationFile = '../questions-words.txt'
    w2vPath = 'models/w2v'

    word2vec = Word2Vec.load(w2vPath)
    accuracy = word2vec.accuracy(evaluationFile, restrict_vocab=100000)


    pdb.set_trace() 


if __name__=='__main__':
    evaluateModel()
