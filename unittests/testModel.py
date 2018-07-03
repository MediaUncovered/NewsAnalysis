from newsAnalysis.Model import Model
import unittest

class testModel(unittest.TestCase):

    def setUp(self):
        self.model = Model(name='testModel', modelType='fasttext', model_path='./sampleModels/MoscowTimes_1000')

    def test_init(self):
        self.assertTrue(self.model.modelType=='word2vec' or self.model.modelType=='fasttext')
        self.assertIsNotNone(self.model.model_path)

    def test_create(self):
        pass

    def test_exists(self):
        self.assertTrue(self.model.exists())

    def test_load(self):
        self.model.load()
        self.assertTrue(hasattr(self.model, 'word_embedding'))



