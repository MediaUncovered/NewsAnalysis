from newsAnalysis.Model import Model
from newsAnalysis.Collection import Collection
import unittest

class testModel(unittest.TestCase):

    def setUp(self):
        self.model = Model(name='testModel', modelType='fasttext', model_path='./sampleModels/MoscowTimes_1000')
        self.model.load()
        self.data_path = './sampleModels/MoscowTimes_1000.csv'

    def test_init(self):
        self.assertTrue(self.model.modelType=='word2vec' or self.model.modelType=='fasttext')
        self.assertIsNotNone(self.model.model_path)

    def test_exists(self):
        self.assertTrue(self.model.exists())

    def test_load(self):
        self.assertTrue(hasattr(self.model, 'word_embedding'))

    def test_getWordCount(self):
        self.assertGreaterEqual(self.model.getWordCount('word'), 5)
        self.assertRaises(KeyError, lambda: self.model.getWordCount('unkown_word'))

    def test_hasWord(self):
        self.assertTrue(self.model.hasWord('word'))
        self.assertFalse(self.model.hasWord('unkown_word'))

