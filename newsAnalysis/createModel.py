import sentences
import gensim
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


def createModel(file_path, output_file_path):
    '''
    Uses Gensim to train a Word2Vec Model
    file_path
        path to a csv file containing articles with the column body
    output_file_path
        the trained model will be stored at this location
    '''

    print('Word2Vec Model - Build Vocab')
    w2v_model = gensim.models.Word2Vec(min_count=8, window=5, workers=4, size=300, alpha=0.05, negative=10)
    w2v_model.build_vocab(sentences.open(file_path))

    print('Word2Vec Model - Train Model')
    w2v_model.train(sentences.open(file_path), total_examples=w2v_model.corpus_count, epochs=w2v_model.iter)
    w2v_model.save(output_file_path)

