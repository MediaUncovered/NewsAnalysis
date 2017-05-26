import unittest
from newsAnalysis import tupleListUtils as tup 

class test_tupleListUtils(unittest.TestCase):

    def setUp(self):
        self.l = [('a', 0.4), ('b', -0.1), ('c', 0.7)]
    
    def test_sortByScore(self):
        target =[('b', -0.1), ('a', 0.4), ('c', 0.7)]
        self.assertListEqual(tup.sortByScore(self.l), target)

    def test_sortByScore_reverse(self):
        target = [('c', 0.7), ('a', 0.4), ('b', -0.1)]
        self.assertListEqual(tup.sortByScore(self.l, reverse=True), target)

    def test_filterList(self):
        self.assertListEqual(tup.filterList(self.l, -0.4), [('a', 0.4), ('b', -0.1), ('c', 0.7)])
        self.assertListEqual(tup.filterList(self.l, 0.2), [('a', 0.4), ('c', 0.7)])
        self.assertListEqual(tup.filterList(self.l, 0.7), [('c', 0.7)])

    def test_filterList_abs(self):
        self.assertListEqual(tup.filterList(self.l, 0.1, True), [('a', 0.4), ('b', -0.1), ('c', 0.7)])
        self.assertListEqual(tup.filterList(self.l, 0.2, True), [('a', 0.4), ('c', 0.7)])



if __name__ == '__main__':
    unittest.main()
