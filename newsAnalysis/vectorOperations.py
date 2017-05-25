from __future__ import division
from numpy import dot,sqrt

def euclideanNorm(v,v2=None):
    if v2:
        v = subtract(v,v2)
    return sqrt(sum(square(v)))

def subtract(v1,v2):
    return [i-j for i,j in zip(v1,v2)]

def square(v):
    return [i**2 for i in v]

def cosSimilarity(v1,v2):
    return dot(v1,v2)/(euclideanNorm(v1)*euclideanNorm(v2))

#def scalarProjection(self, vector, basis):
#    vector = self.word2Vector(vector)
#    basis = self.combineList(basis)
#    return dot(vector,basis)/self.euclideanNorm(basis)
#                                                       
#def unNormScalarProjection(self,vector,basis):
#    vector = self.word2Vector(vector)
#    basis = self.combineList(basis)
#    return dot(vector,basis)
#
#def vectorRejection(self, a,b):
#    scalar_a1 = dot(a,b)/self.euclideanNorm(b)
#    vec_a1 = [scalar_a1*elem for elem in (b/self.euclideanNorm(b))]
#    return subtract(a,vec_a1)
#
#def projectToBasis(self, word, basis1, basis2):
#    return dot(self.model[word],self.basisDirection(basis1, basis2))
#
#def basisDirection(self, w1,w2):
#    v1 = self.model[w1]
#    v2 = self.model[w2]
#    diff = self.substract(v1,v2)
#    return diff/self.euclideanNorm(diff) 
#
#def project(self, word, base):
#    if isString(base):
#        base = self.model[base]
#    return dot(self.model[word], base)/self.euclideanNorm(base)
