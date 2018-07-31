from newsAnalysis.Info import Info
import pandas as pd
import unittest

class testInfo(unittest.TestCase):

    def setUp(self):
        data_path = './sampleModels/MoscowTimes_1000.csv'
        self.data = pd.read_csv(data_path, encoding='utf8')
        self.Info = Info(data_path)

    def test_setNrArticles(self):
        self.Info.setNrArticles(self.data)
        self.assertEqual(self.Info.nr_articles, 1000)
        self.assertLessEqual(self.Info.empty_articles, 1000)
        self.assertGreaterEqual(self.Info.empty_articles, 0)

