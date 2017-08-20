from Info import Info 
from sys import argv
from Sentences import Sentences
import gensim, logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


DATABASE = argv[1]
HOST = argv[2]
PORT = argv[3]
USER = argv[4]
PASSWORD = argv[5]


def script():

    info = Info()
    info.database(DATABASE, HOST, PORT, USER, PASSWORD)

    sentences = Sentences()
    sentences.connectDatabase(info)
    
    print 'Query database'
    sentences.queryDatabase(limit=10000)

    print 'Word2Vec Model' 
    w2v_model = gensim.models.Word2Vec(sentences=sentences, min_count=10, window=5, workers=4, size=300)
    w2v_model.save('models/w2v')



if __name__=='__main__':
    script()


    
