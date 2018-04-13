from gensim.models import Word2Vec
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
import sentences
import os
import csv

class Model:

    def __init__(self, name='wordEmbedding'):
        self.name = name
        self.model_path = './models/' + name


    def create(self, data_path):
        ''' Uses Gensim to train a Word2Vec Model
        file_path points to a csv file containing articles with the text of newspaper articles in a column called body
        '''
        self.w2v_model = Word2Vec(min_count=8, window=5, workers=4, size=300, alpha=0.05, negative=10)
        self.w2v_model.build_vocab(sentences.open(data_path))
        self.w2v_model.train(sentences.open(data_path), total_examples=self.w2v_model.corpus_count, epochs=self.w2v_model.iter)


    def evaluate(self):
        ''' evaluates the semantic concepts a Word2Vec model has learned based on analogies, e.g. sister:brother :: daughter:son, in specific categories (e.g. currencies, verb forms, family, country capitals, etc.) '''
        evaluationFile = 'questions-words.txt'
        self.accuracy = self.w2v_model.wv.accuracy(evaluationFile)


    def to_tsv(self):
        self.vectors2tsv()
        self.vocab2tsv()


    def vectors2tsv(self):
        with open(self.model_path + '.tsv', 'wb') as f:
            writer = csv.writer(f, delimiter='\t', lineterminator='\n')
            writer.writerows(self.w2v_model.wv.vectors)
        f.close()


    def vocab2tsv(self):
        with open(self.model_path + '_metadata.tsv', 'wb') as f:
            f.write('\n'.join(self.w2v_model.wv.vocab.keys()))
        f.close()


    def exists(self):
        return os.path.exists(self.model_path)


    def load(self):
        self.w2v_model = Word2Vec.load(self.model_path)


    def save(self):
        self.w2v_model.save(self.model_path)
