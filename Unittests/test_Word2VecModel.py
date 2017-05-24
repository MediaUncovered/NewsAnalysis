import unittest
from newsAnalysis import Word2VecModel
from gensim.models import word2vec

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


    def test_initEmpty(self):
        w2v = Word2VecModel()
        self.assertEqual(w2v.vocabulary, [])
        self.assertEqual(w2v.model.__str__(), word2vec.Word2Vec().__str__())

    def test_initSentences(self):
        w2v = Word2VecModel(sentences, min_word_count=1)
        self.assertEqual(w2v.model.__str__(), word2vec.Word2Vec(sentences, min_count=1).__str__())
        self.assertItemsEqual(w2v.vocabulary, vocabulary)


if __name__ == '__main__':
    unittest.main()
