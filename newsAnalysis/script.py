from Info import Info 
from sys import argv
from Sentences import Sentences
import gensim, logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
import pdb


DATABASE = argv[1]
HOST = argv[2]
PORT = argv[3]
USER = argv[4]
PASSWORD = argv[5]

nrDocs = 5000


def script():

    info = Info()
    info.database(DATABASE, HOST, PORT, USER, PASSWORD)

    sentences = Sentences()
    sentences.connectDatabase(info)
    
    print 'Query database'
    sentences.queryDatabase(limit=nrDocs)

    print 'Word2Vec Model - Build Vocab' 
    w2v_model = gensim.models.Word2Vec(min_count=8, window=5, workers=3, size=300, alpha=0.05, negative=10)
    w2v_model.build_vocab(sentences)


    print 'Word2Vec Model - Train Model'  
    sentences.queryDatabase(limit=nrDocs, cursorname='test2')
    w2v_model.train(sentences, total_examples=w2v_model.corpus_count, epochs=w2v_model.iter)

    w2v_model.save('models/w2v_%i' % nrDocs)



if __name__=='__main__':
    script()


    
