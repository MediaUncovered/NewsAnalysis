from numpy import dot,sqrt

def euclideanNorm(v):
    return sqrt(sum(square(v)))

def l2norm(v1,v2):
    return sqrt(sum(square(substract(v1,v2))))

def substract(v1,v2):
    return [i-j for i,j in zip(v1,v2)]

def square(v):
    return [i**2 for i in v]

def cosSimilarity(vec1,vec2):
    return dot(vec1,vec2)/(euclideanNorm(vec1)*euclideanNorm(vec2))
