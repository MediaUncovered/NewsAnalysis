from gensim.models import word2vec
from gensim.models.phrases import Phrases
from gensim import models
import numpy as np
from numpy import dot,mean
import tupleListUtils as tup


class Word2VecModel:

    def __init__(self, sentences=None, size=100, min_word_count=5, context=5):
        self.model = word2vec.Word2Vec()
        if sentences: 
            self.model = word2vec.Word2Vec(sentences, size=size, min_count= min_word_count, window=context) 
        self.setVocabulary()

    
    def load(self, path):
        self.model = models.Word2Vec.load_word2vec_format(path, binary=False)
        self.vocabulary = self.model.vocab

    
    def isString(self, elem):
        return type(elem)==str 

    
    def keywordCosSimilarity(self,vec,keywords):
        if type(vec)==str:
            vec = self.word2Vector(vec)
        if type(vec)==tuple:
            vec = self.model[vec[0]]-self.model[vec[1]]
        return [cosSimilarity(vec, self.model[word]) for word in keywords]

    
    def keywordProjection(self, vec, keywords):
        return [self.scalarProjection(word, vec) for word in keywords]


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
    
    def computeDistance(self, word1, wordList):
        return [self.model.similarity(word1,word) for word in wordList]

    def semanticSimilarity(self, word1, word2):
        vector1 = self.word2Vector(word1)
        vector2 = self.word2Vector(word2)
        difference = self.substract(vector1, vector2)
        return self.euclideanNorm(difference)


    def word2Vector(self, word):
        return self.model[word]

    def combineList(self, inputList):
        if type(inputList) is list:
            if isString(inputList[0]):
                inputList[0] = self.model[inputList[0]]
            if isString(inputList[1]):
                inputList[1] = self.model[inputList[1]]
            return inputList[0]-inputList[1] 
        return inputList


    def averageWords(self, wordList):
        vectors = [self.word2Vector(word) for word in wordList if word in self.vocabulary]
        return mean(vectors, axis=0)
        
    
    def distanceMatrix(model, vocabulary):
        distanceMatrix = np.zeros([len(vocabulary), len(vocabulary)])
    
    def getSimilarWords(self, word, topn=10):
        return self.model.most_similar(word, topn=topn)

    def getDissimilarWords(self, word, topn=10):
        vocabLength = len(self.vocabulary)
        similarWords = self.getSimilarWords(word, topn=vocabLength)
        dissimilarWords = tup.sortByScore(similarWords) 
        return dissimilarWords[:topn]

