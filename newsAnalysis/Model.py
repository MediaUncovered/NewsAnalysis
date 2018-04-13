from gensim.models import Word2Vec
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
import sentences
import os

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


    def exists(self):
        return os.path.exists(self.model_path)


    def load(self):
        self.w2v_model = Word2Vec.load(self.model_path)


    def save(self):
        self.w2v_model.save(self.model_path)
