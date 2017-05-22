import unittest
from newsAnalysis import vectorOperations as vecOp

class test_vectorOperations(unittest.TestCase):

    def test_substract(self):
        v1 = [3,4,5]
        v2 = [1,0,6]
        self.assertEqual(vecOp.substract(v1,v2), [2,4,-1])

    def test_square(self):
        v = [-1, 0, 1, 10]
        self.assertEqual(vecOp.square(v), [1,0,1,100])

    def test_euclideanNorm(self):
        v = [2,4,1,2]
        self.assertEqual(vecOp.euclideanNorm(v), 5)



if __name__ == '__main__':
    unittest.main()
