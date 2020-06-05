# target = __import__("my_sum.py")
# sum = target.sum

import unittest 

from my_sum import sum
from my_sum.newData import mult

class TestSum(unittest.TestCase):
    def test_list_int(self):
        '''
        Test that it can sum a lsit of integers
        '''
        data = [1,2,3]
        result = sum(data)
        self.assertEqual(result, 6)

class TestSum(unittest.TestCase):
    def test_list_int(self):
        '''
        Test that it can sum a lsit of integers
        '''
        data = [1,2,3]
        result = mult(data)
        self.assertEqual(result, 6)

if __name__ == '__main__':
    unittest.main()