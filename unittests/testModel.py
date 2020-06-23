from newsAnalysis.Model import Model
from newsAnalysis.Collection import Collection
import unittest

class testModel(unittest.TestCase):

    def setUp(self):
        model_path='./sampleModels/MoscowTimes_1000'
        self.model = Model().load(model_path= model_path)
        self.data_path = './sampleModels/MoscowTimes_1000.csv'

    def test_load(self):
        self.assertTrue(self.model.name, 'MoscowTimes')
        self.assertTrue(hasattr(self.model, 'word_embedding'))
        self.assertTrue(hasattr(self.model, 'modelType'))

    def test_getWordCount(self):
        self.assertGreaterEqual(self.model.getWordCount('word'), 5)
        self.assertRaises(KeyError, lambda: self.model.getWordCount('unkown_word'))

    def test_hasWord(self):
        self.assertTrue(self.model.hasWord('word'))
        self.assertFalse(self.model.hasWord('unkown_word'))

    def test_generateAnalogies(self):
        analogies = self.model.generate_analogies('moscow', 'russia')
        self.assertTrue(len(analogies) > 0)

    def test_filterNonVocabWords(self):
        word_list = ['xxxx', 'valid', 'aeease', 'word', 'yaseiw']
        self.assertListEqual(self.model.filterNonVocabWords(word_list),
                             ['valid', 'word'])
