from newsAnalysis.CollectionInfo import CollectionInfo
import unittest

class testCollectionInfo(unittest.TestCase):

    def test_newspaperName(self):
        collection = CollectionInfo()

        data_path1 = '../data/Moscow_Times_1000.csv'
        newspaper1 = collection.newspaperName(data_path1)
        self.assertEqual(newspaper1, 'Moscow Times')

        data_path2 = 'Moscow_Times_1000.csv'
        newspaper2 = collection.newspaperName(data_path2)
        self.assertEqual(newspaper2, 'Moscow Times')

        data_path3 = 'MoscowTimes_1000.csv'
        newspaper3 = collection.newspaperName(data_path3)
        self.assertEqual(newspaper3, 'MoscowTimes')

    def test_toJson(self):
        info = CollectionInfo()
        info.newspaper = 'Moscow Times'
        info.nr_articles = 10
        json_target = '{"newspaper": "Moscow Times", "nr_articles": 10}'
        self.assertEqual(info.toJson(), json_target)




