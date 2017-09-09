from Info import Info
from sys import argv
from Sentences import Sentences
import gensim, logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


DATABASE = argv[2]
HOST = argv[3]
PORT = argv[4]
USER = argv[5]
PASSWORD = argv[6]


def createModel(nrDocs):

    info = Info()
    info.database(DATABASE, HOST, PORT, USER, PASSWORD)

    sentences = Sentences()
    sentences.connectDatabase(info)

    print 'Query database'
    sentences.queryDatabase(limit=nrDocs)

    print 'Word2Vec Model - Build Vocab'
    w2v_model = gensim.models.Word2Vec(min_count=8, window=5, workers=4, size=300, alpha=0.05, negative=10)
    w2v_model.build_vocab(sentences)


    print 'Word2Vec Model - Train Model'
    sentences.queryDatabase(limit=nrDocs, cursorname='test2')
    w2v_model.train(sentences, total_examples=w2v_model.corpus_count, epochs=w2v_model.iter)

    path = 'models/w2v_%i' % nrDocs
    w2v_model.save(path)



if __name__=='__main__':
    nrDocs = int(argv[1])
    createModel(nrDocs)



