from gensim.models import word2vec
from gensim.models.phrases import Phrases
from gensim import models
import numpy as np
import matplotlib.pyplot as plt
from numpy import dot,sqrt,mean,subtract

class Word2VecModel:

    def __init__(self, sentences=None, size=100, min_word_count=5, context=5):
        self.model = word2vec.Word2Vec()
        if sentences: 
            self.model = word2vec.Word2Vec(sentences, size=size, min_count= min_word_count, window=context) 
        self.getVocabulary()

    
    def load(self, path):
        self.model = models.Word2Vec.load_word2vec_format(path, binary=False)
        self.vocabulary = self.model.vocab


    def filterSimilarity(self, similarities, threshold=0.25, absolutValue=True):
        if abs:
            return [(score,ind) for ind,score in enumerate(similarities) if abs(score)>threshold]   
        return [(score,ind) for ind,score in enumerate(similarities) if score>threshold]

    def getTopNWords(self, scoreList, topn=10):
        scoreList.sort()
        dissimilar = [(self.model.index2word[elem[1]], elem[0]) for elem in scoreList[0:topn] if elem<0]
        similar = [(self.model.index2word[elem[1]], elem[0]) for elem in scoreList[-topn:-1] if elem >0]
        return [similar, dissimilar]


    def keywordCosSimilarity(self,vec,keywords):
        if type(vec)==str:
            vec = self.word2Vector(vec)
        if type(vec)==tuple:
            vec = self.model[vec[0]]-self.model[vec[1]]
        return [self.cosSimilarity(vec, self.model[word]) for word in keywords]

    
    def keywordProjection(self, vec, keywords):
        return [self.scalarProjection(word, vec) for word in keywords]

    

    def getMostSimilarAndDisimilar(self, vector, threshold=0.25, restrict_vocab=3000, topn=20):
        similarities = self.model.similar_by_vector(vector, topn=False, restrict_vocab=restrict_vocab)
        filteredSimilarity = self.filterSimilarity(similarities, threshold=threshold)
        return self.getTopNWords(filteredSimilarity, topn)


    def getMostSimilar(self,vector,threshold=0.75,restrict_vocab=5000):
        if type(vector) == str:
            vector = self.word2Vector(vector)
        similarities = self.model.similar_by_vector(vector, topn=False, restrict_vocab = restrict_vocab)
        filtered = self.filterSimilarity(similarities, threshold = threshold)
        wordList = [(self.model.index2word[elem[1]], elem[0]) for elem in filtered if elem[0]<1]
        return wordList 

        
    def train(self, sentences, num_features, min_word_count, context):
        bigram_transformer = Phrases(sentences)
        self.model = word2vec.Word2Vec(bigram_transformer[sentences], size=num_features, min_count = min_word_count, window=context)

    def getVocabulary(self):
        self.vocabulary = list(self.model.vocab.keys())
        self.vocabulary.sort()

    def generateAnalogies(self, word1, word2, basis):
        vec1 = self.word2Vector(word1)
        vec2 = self.word2Vector(word2)
        diff = self.substract(vec1, vec2)
        return dot(diff,basis)/self.euclideanNorm(diff)
    
    def computeDistance(self, word1, wordList):
        return [self.model.similarity(word1,word) for word in wordList]

    def vectorRejection(self, a,b):
        scalar_a1 = dot(a,b)/self.euclideanNorm(b)
        vec_a1 = [scalar_a1*elem for elem in (b/self.euclideanNorm(b))]
        return subtract(a,vec_a1)

    def scalarProjection(self, vector, basis):
        vector = self.word2Vector(vector)
        basis = self.combineList(basis)
        return dot(vector,basis)/self.euclideanNorm(basis)

    def unNormScalarProjection(self,vector,basis):
        vector = self.word2Vector(vector)
        basis = self.combineList(basis)
        return dot(vector,basis)

    def semanticSimilarity(self, word1, word2):
        vector1 = self.word2Vector(word1)
        vector2 = self.word2Vector(word2)
        difference = self.substract(vector1, vector2)
        return self.euclideanNorm(difference)


    def word2Vector(self,word):
        if self.isString(word):
            return self.model[word]
        return word

    def combineList(self, inputList):
        if type(inputList) is list:
            if self.isString(inputList[0]):
                inputList[0] = self.model[inputList[0]]
            if self.isString(inputList[1]):
                inputList[1] = self.model[inputList[1]]
            return inputList[0]-inputList[1] 
        return inputList


    def averageWords(self, wordList):
        vectors = [self.model[word] for word in wordList if word in self.vocabulary]
        return mean(vectors, axis=0)
        

    def project(self, word, base):
        if self.isString(base):
            base = self.model[base]
        return dot(self.model[word], base)/self.euclideanNorm(base)
            

    def projectToBasis(self, word, basis1, basis2):
        return dot(self.model[word],self.basisDirection(basis1, basis2))
    
    def basisDirection(self, w1,w2):
        v1 = self.model[w1]
        v2 = self.model[w2]
        diff = self.substract(v1,v2)
        return diff/self.euclideanNorm(diff) 

    def isString(self,elem):
        return isinstance(elem, basestring)
    
    def distanceMatrix(model, vocabulary):
        distanceMatrix = np.zeros([len(vocabulary), len(vocabulary)])
    

    def doesntMatch(self, wordList): 
        return self.model.doesnt_match(wordList)
    
    def mostSimilar(self, word):
        return self.model.most_similar(word)
    
    def analogy(self):
        self.model.most_similar(['russia', 'washington'],['u.s.'], topn=3)
