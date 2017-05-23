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
