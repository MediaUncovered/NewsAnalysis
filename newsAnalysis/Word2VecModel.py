from gensim.models import word2vec
from gensim.models.phrases import Phrases
from gensim import models
import numpy as np
from numpy import dot,mean
import tupleListUtils as tup
import vectorOperations as vecOp


class Word2VecModel:

    def __init__(self, sentences=None, size=100, min_word_count=5, context=5):
        self.model = word2vec.Word2Vec()
        if sentences: 
            self.model = word2vec.Word2Vec(sentences, size=size, min_count= min_word_count, window=context) 
        self.setVocabulary()
    
    def load(self, path):
        self.model = models.Word2Vec.load_word2vec_format(path, binary=False)
        self.vocabulary = self.model.vocab

    def cosSimilarity(self, elem1, elem2):
        vec1 = self.getVector(elem1)
        vec2 = self.getVector(elem2)
        return vecOp.cosSimilarity(vec1, vec2)

    def cosSimilarityList(self, word, wordList):
        return [self.cosSimilarity(word, elem) for elem in wordList]
    
    def getMostSimilar(self,vector,threshold=0.75,restrict_vocab=5000):
        similarities = self.model.similar_by_vector(vector, topn=False, restrict_vocab = restrict_vocab)
        filtered = self.filterSimilarity(similarities, threshold = threshold)
        wordList = [(self.model.index2word[elem[1]], elem[0]) for elem in filtered if elem[0]<1]
        return wordList 
        
    def train(self, sentences, num_features, min_word_count, context):
        bigram_transformer = Phrases(sentences)
        self.model = word2vec.Word2Vec(bigram_transformer[sentences], size=num_features, min_count = min_word_count, window=context)

    def setVocabulary(self):
        self.vocabulary = list(self.model.vocab.keys())
        self.vocabulary.sort()

    def generateAnalogies(self, word1, word2, basis):
        vec1 = self.word2Vector(word1)
        vec2 = self.word2Vector(word2)
        diff = self.substract(vec1, vec2)
        return dot(diff,basis)/self.euclideanNorm(diff)
    
    def averageWords(self, wordList):
        vectors = [self.word2Vector(word) for word in wordList if word in self.vocabulary]
        return mean(vectors, axis=0)
   
    def getSimilarWords(self, word, topn=10):
        return self.model.most_similar(word, topn=topn)

    def getDissimilarWords(self, word, topn=10):
        vocabLength = len(self.vocabulary)
        similarWords = self.getSimilarWords(word, topn=vocabLength)
        dissimilarWords = tup.sortByScore(similarWords) 
        return dissimilarWords[:topn]

    def isString(self, elem):
        return type(elem) == str 

    def word2Vector(self, word):
        return self.model[word]

    def getVector(self, elem):
        if self.isString(elem):
            return self.word2Vector(elem)
        return elem

