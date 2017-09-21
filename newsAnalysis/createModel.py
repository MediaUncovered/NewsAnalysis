from sys import argv
import sentences
import gensim
import logging


logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


def createModel(file_path, output_file_path):

    print('Word2Vec Model - Build Vocab')
    w2v_model = gensim.models.Word2Vec(min_count=8, window=5, workers=4, size=300, alpha=0.05, negative=10)
    w2v_model.build_vocab(sentences)


    print 'Word2Vec Model - Train Model'
    sentences.queryDatabase(limit=nrDocs, cursorname='test2')
    w2v_model.train(sentences, total_examples=w2v_model.corpus_count, epochs=w2v_model.iter)

    path = 'models/w2v_%i' % nrDocs
    w2v_model.save(path)
    #word2vec.wv.save(path + '.bin', binary=True)

    print('Word2Vec Model - Train Model')
    w2v_model.train(sentences.open(file_path), total_examples=w2v_model.corpus_count, epochs=w2v_model.iter)
    w2v_model.save(output_file_path)


if __name__=='__main__':
    input_file_path = argv[1]
    output_file_path = argv[2]
    createModel(input_file_path, output_file_path)
