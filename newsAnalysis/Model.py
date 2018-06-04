from gensim.models import Word2Vec, FastText
import numpy as np
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
import sentences
import os
import csv
import shutil
from ImagePlotter import ImagePlotter
from Projector import Projector

class Model:

    def __init__(self, name='wordEmbedding', modelType='word2vec'):
        self.name = name
        self.modelType = modelType
        self.model_path = './models/' + name + '_' + self.modelType


    def create(self, data_path):
        ''' Uses Gensim to train a word embedding Model, either fasttext or word2vec are possible.
        file_path points to a csv file containing articles with the text of newspaper articles in a column called body
        '''
        if self.modelType=='word2vec':
            self.word_embedding = Word2Vec(min_count=8, window=5, workers=4, size=300, alpha=0.05, negative=10)
        if self.modelType=='fasttext':
            self.word_embedding = FastText(size=300)
        self.word_embedding.build_vocab(sentences.open(data_path))
        self.word_embedding.train(sentences.open(data_path), total_examples=self.word_embedding.corpus_count, epochs=self.word_embedding.iter)


    def evaluate(self):
        ''' evaluates the semantic concepts a Word2Vec model has learned based on analogies, e.g. sister:brother :: daughter:son, in specific categories (e.g. currencies, verb forms, family, country capitals, etc.) '''
        evaluationFile = 'questions-words.txt'
        self.accuracy = self.word_embedding.wv.accuracy(evaluationFile)

    def vectors2Bytes(self):
        vectors = self.word_embedding.wv.vectors
        vectors.tofile(self.model_path + '.bytes')


    def to_tsv(self):
        self.vectors2tsv()
        self.vocab2tsv()


    def vectors2tsv(self):
        with open(self.model_path + '.tsv', 'wb') as f:
            writer = csv.writer(f, delimiter='\t', lineterminator='\n')
            writer.writerows(self.word_embedding.wv.vectors)
        f.close()


    def vocab2tsv(self):
        with open(self.model_path + '_metadata.tsv', 'wb') as f:
            vocab = self.word_embedding.wv.vocab.keys()
            #vocabWithLineSeparator = [word + '\n' for ind,word in enumerate(vocab) if ind<len(vocab)-1]
            vocabWithLineSeparator = [word + '\n' for word in vocab]
            f.writelines(vocabWithLineSeparator)
        f.close()


    def exists(self):
        return os.path.exists(self.model_path)


    def load(self):
        self.word_embedding = Word2Vec.load(self.model_path)


    def save(self):
        self.word_embedding.save(self.model_path)


    def wordListSimilarity(self, w, listOfWords):
        ''' return the mean cosine similarity of a word and all words in a list '''
        similarities = [self.word_embedding.wv.similarity(w, word) for word in listOfWords]
        return np.mean(similarities)

    def mapWordOnAxis(self, word, attributes1, attributes2):
        ''' substract the mean cos distance of a word with all attributes in attributes1 with the mean cosine distance of word with all attributes in attributes2:
            s(w, A1, A2) = mean[for a1 in A1: cos(w, a1)] - mean[for a2 in A2: cos(w, a2)] '''
        return self.wordListSimilarity(word, attributes1) - self.wordListSimilarity(word, attributes2)


    def keywordMapping(self, listOfWords, attributes1, attributes2):
        wordAttributeSimTarget1 = [self.wordListSimilarity(word, attributes1) for word in listOfWords]
        wordAttributeSimTarget2 = [self.wordListSimilarity(word, attributes2) for word in listOfWords]
        return np.array(wordAttributeSimTarget1) - np.array(wordAttributeSimTarget2)


    def plotKeywordMapping(self, values, labels, title='test'):
        plotter = ImagePlotter(True)
        plotter.horizontalBarPlot(values, labels, title='Word-Axis Mapping', x_label='attribute association', path=title + '.png')


    def WEAT(self, targets1, targets2, attributes1, attributes2):
        wordAttributeSimTarget1 = [self.mapWordOnAxis(target, attributes1, attributes2) for target in targets1]
        wordAttributeSimTarget2 = [self.mapWordOnAxis(target, attributes1, attributes2) for target in targets2]
        return np.sum(wordAttributeSimTarget1) - np.sum(wordAttributeSimTarget2)


    def visualise(self):
        self.vocab2tsv()
        self.vectors2Bytes()

        projector = Projector()
        modelName = '_'.join([self.name, self.modelType])

        shutil.copy(self.model_path + '.bytes', projector.data_path + '/' + modelName + '.bytes')
        shutil.copy(self.model_path + '_metadata.tsv', projector.data_path + '/' + modelName + '_metadata.tsv')

        path = os.path.join(projector.data_path.split('/')[-1], modelName)
        projector.addModelToConfig(self.name, path + '.bytes', path + '_metadata.tsv', len(self.word_embedding.wv.vocab), self.word_embedding.vector_size)
        projector.writeConfigFile()
        projector.run()






