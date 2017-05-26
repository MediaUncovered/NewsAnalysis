import unittest
from newsAnalysis import Word2VecModel
from gensim.models import word2vec
import numpy as np

sentences = [ ['human', 'interface', 'computer'],
        ['survey', 'user', 'computer', 'system', 'response', 'time'],
        ['eps', 'user', 'interface', 'system'],
        ['system', 'human', 'system', 'eps'],
        ['user', 'response', 'time'],
        ['trees'],
        ['graph', 'trees'],
        ['graph', 'minors', 'trees'],
        ['graph', 'minors', 'survey']]

vocabulary = ['human', 'user', 'response', 'trees', 'time', 'computer', 'interface', 'minors', 'graph', 'survey', 'system', 'eps']


class test_Word2VecModel(unittest.TestCase):

    def setUp(self):
        self.w2v = Word2VecModel(sentences, min_word_count=1)


    def test_init_empty(self):
        w2v = Word2VecModel()
        self.assertEqual(w2v.vocabulary, [])
        self.assertEqual(w2v.model.__str__(), word2vec.Word2Vec().__str__())

    def test_init_sentences(self):
        self.assertEqual(self.w2v.model.__str__(), word2vec.Word2Vec(sentences, min_count=1).__str__())
        self.assertItemsEqual(self.w2v.vocabulary, vocabulary)

    def test_setVocabulary(self):
        self.w2v.setVocabulary()
        self.assertItemsEqual(self.w2v.vocabulary, vocabulary)

    def test_word2Vector(self):
        vector = self.w2v.word2Vector('human')
        self.assertEqual(len(vector), 100)
        self.assertEqual(type(vector), np.ndarray)

    def test_isString(self):
        self.assertTrue(self.w2v.isString('test'))
        self.assertFalse(self.w2v.isString(9))
        self.assertFalse(self.w2v.isString(np.array(['a','b'])))
    
    def test_getSimilarWords(self):
        similarWords = self.w2v.getSimilarWords('human', 3)
        wordTuple = similarWords[0]
        self.assertTrue(len(similarWords), 3)
        self.assertTrue(isinstance(wordTuple, tuple))
        self.assertTrue(isinstance(wordTuple[0], str))
        self.assertTrue(isinstance(wordTuple[1], float))
        self.assertTrue(similarWords[0][1] > similarWords[1][1]) 
        self.assertTrue(similarWords[1][1] > similarWords[2][1]) 

    def test_getDissimilarWords(self): 
        dissimilarWords = self.w2v.getDissimilarWords('human', 3)
        print dissimilarWords
        wordTuple = dissimilarWords[0]
        self.assertTrue(len(dissimilarWords), 3)
        self.assertTrue(isinstance(wordTuple, tuple))
        self.assertTrue(isinstance(wordTuple[0], str))
        self.assertTrue(isinstance(wordTuple[1], float))
        self.assertTrue(dissimilarWords[0][1] < dissimilarWords[1][1]) 
        self.assertTrue(dissimilarWords[1][1] < dissimilarWords[2][1]) 

    
    
    
        




if __name__ == '__main__':
    unittest.main()
