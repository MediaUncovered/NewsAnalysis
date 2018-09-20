import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

import pickle
import numpy as np
from gensim.models import Word2Vec, FastText, KeyedVectors
from ethically.we import BiasWordsEmbedding

import os
import csv
import shutil
from newsAnalysis.CollectionInfo import CollectionInfo
from newsAnalysis.ModelInfo import ModelInfo
from newsAnalysis.Collection import Collection
from newsAnalysis.ImagePlotter import ImagePlotter
from newsAnalysis.Projector import Projector

class Model:

    def __init__(self, name=None, modelType=None):
        if name and modelType:
            self.name = name
            self.modelType = modelType
            self.model_path = self.getModelPath(name, modelType)


    def create(self, data_path, modelName='wordEmbedding', modelType='word2vec', model_path=None):
        ''' Uses Gensim to train a word embedding Model, either fasttext or word2vec are possible.
        file_path points to a csv file containing articles with the text of newspaper articles in a column called body
        '''
        self.name = modelName
        self.modelType = modelType
        if model_path is None:
            model_path = self.getModelPath(self.name, self.modelType)
        self.model_path = model_path
        if self.modelType=='word2vec':
            self.word_embedding = Word2Vec(min_count=8, window=5, workers=4, size=300, alpha=0.05, negative=10, sg=1)
        if self.modelType=='fasttext':
            self.word_embedding = FastText(size=300)


        self.collectionInfo = CollectionInfo(data_path)
        collection = Collection(data_path)

        self.word_embedding.build_vocab(collection)
        self.word_embedding.train(collection, total_examples=self.word_embedding.corpus_count, epochs=self.word_embedding.iter)

        self.modelInfo = ModelInfo(self.modelType, self.word_embedding)


    def getModelPath(self, modelName, modelType):
        return './models/' + modelName + '_' + modelType


    def evaluate(self):
        ''' evaluates the semantic concepts a Word2Vec model has learned based on analogies, e.g. sister:brother :: daughter:son, in specific categories (e.g. currencies, verb forms, family, country capitals, etc.) '''
        with open('newsAnalysis/questions-words.txt', 'r') as evaluationFile:
            self.accuracy = self.word_embedding.wv.accuracy(evaluationFile)
        correctAnalogies = [len(result['correct']) for result in self.accuracy]
        totalAnalogies = [len(result['correct'] + result['incorrect']) for result in self.accuracy]
        for ind in range(len(self.accuracy)):
            self.accuracy[ind]['nr_correct'] = correctAnalogies[ind]
            self.accuracy[ind]['nr_total'] = totalAnalogies[ind]



    def vectors2Bytes(self):
        vectors = self.word_embedding.wv.vectors
        vectors.tofile(self.model_path + '.bytes')


    def to_tsv(self):
        self.vectors2tsv()
        self.vocab2tsv()


    def vectors2tsv(self):
        with open(self.model_path + '.tsv', 'w') as f:
            writer = csv.writer(f, delimiter='\t', lineterminator='\n')
            writer.writerows(self.word_embedding.wv.vectors)
        f.close()


    def vocab2tsv(self):
        with open(self.model_path + '_metadata.tsv', 'w') as f:
            vocab = self.word_embedding.wv.vocab.keys()
            #vocabWithLineSeparator = [word + '\n' for ind,word in enumerate(vocab) if ind<len(vocab)-1]
            vocabWithLineSeparator = [word + '\n' for word in vocab]
            f.writelines(vocabWithLineSeparator)
        f.close()


    def exists(self, model_path=None):
        if hasattr(self, 'model_path'):
            return os.path.exists(self.model_path)
        elif model_path:
            return os.path.exists(model_path)
        else:
            return False


    def load(self, modelName=None, modelType=None, model_path=None):
        if hasattr(self, 'model_path'):
            model_path = self.model_path
        elif modelName and modelType:
            model_path = self.getModelPath(modelName, modelType)
        input_file = open(model_path + '.pkl', 'rb')
        self = pickle.load(input_file)
        self.word_embedding = KeyedVectors.load_word2vec_format(model_path) #, mmap='r')
        return self


    def __getstate__(self):
        return (self.modelType, self.name, self.collectionInfo, self.modelInfo, self.accuracy)


    def __setstate__(self, state):
        self.modelType, self.name, self.collectionInfo, self.modelInfo, self.accuracy = state


    def save(self):
        output = open(self.model_path + '.pkl', 'wb')
        pickle.dump(self, output)
        self.word_embedding.wv.save_word2vec_format(self.model_path)


    def hasWord(self, word):
        if self.word_embedding.wv.vocab.get(word) == None:
            return False
        else:
            return True

    def getWordCount(self, word):
        if self.hasWord(word):
            return self.word_embedding.wv.vocab.get(word).count
        else:
            raise KeyError('ERROR: WORD not in Model')

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


    def generate_analogies(self, w1, w2, restrict_vocab=5000):
        biasObject = BiasWordsEmbedding(self.word_embedding)
        biasObject._identify_direction(w1, w2, [w1, w2], method='single')
        return biasObject.generate_analogies(restrict_vocab=restrict_vocab)


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


