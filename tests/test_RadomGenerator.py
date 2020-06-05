import unittest 
from chaos.RandomGenerator import randomGenerator

class TestSum(unittest.TestCase):
    def test_list_int(self):
        '''
        Test that it can sum a lsit of integers
        '''
        result = randomGenerator()
        self.assertIsInstance(result,generator)
