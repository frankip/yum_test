import unittest
from question_one import read_csv_data

class CsvDataManipulation(unittest.TestCase):

    def test_if_returns_the_highest(self):
        self.assertEqual(read_csv_data, 9.9 )