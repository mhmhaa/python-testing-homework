import unittest
from main import AverageCalculating


class AverageCalculatingTestCase(unittest.TestCase):
    def test_integers(self):
        self.test = AverageCalculating()
        self.test.numbers = [-7, 3, 90, -49, 15]
        res = self.test.calculate_average()
        self.assertEqual(res, 10)
        print('Tested by Ann Mikhailova')

    def test_fractiional_nums(self):
        self.test = AverageCalculating()
        self.test.numbers = [1.7, 2.0056, -35.0421, 31.49, -7.5]
        res = self.test.calculate_average()
        self.assertEqual(res, -2)
        print('Tested by Ann Mikhailova')

    def test_different_nums(self):
        self.test = AverageCalculating()
        self.test.numbers = [10, -2.007, -35, 78.54, -75]
        res = self.test.calculate_average()
        self.assertEqual(res, -5)
        print('Tested by Ann Mikhailova')

    def test_empty_list(self):
        self.test = AverageCalculating()
        self.test.numbers = []
        res = self.test.calculate_average()
        self.assertEqual(res, None)
        print('Tested by Ann Mikhailova')
