import unittest
from newsAnalysis import vectorOperations as vecOp
from numpy import sqrt

class test_vectorOperations(unittest.TestCase):

    def test_subtract(self):
        v1 = [3,4,5]
        v2 = [1,0,6]
        self.assertEqual(vecOp.subtract(v1,v2), [2,4,-1])

    def test_square(self):
        self.assertEqual(vecOp.square([-1,0,1,10]), [1,0,1,100])
        self.assertEqual(vecOp.square([5]), [25])

    def test_euclideanNorm(self):
        v = [2,4,1,2]
        self.assertEqual(vecOp.euclideanNorm(v), 5)
        v2 = [1,-2,0,2]
        self.assertEqual(vecOp.euclideanNorm(v,v2), sqrt(38))

    def test_cosSimilarity(self):
        cosSim = vecOp.cosSimilarity
        self.assertAlmostEqual(cosSim([2,1],[-2,-1]), -1)
        self.assertAlmostEqual(cosSim([3,4],[6,8]), 1)
        self.assertAlmostEqual(cosSim([1,1,1,2,0], [1,1,1,2,1]),7/7.48331477)




if __name__ == '__main__':
    unittest.main()
