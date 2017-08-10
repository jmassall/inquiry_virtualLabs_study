'''
author: sperez8
data: june 14 2017

This script cleans raw log files and splits them into individual session files stored in the log data folder
'''
import unittest
from utils import convert_unix_time


class TestUtils(unittest.TestCase):
    """
    Our basic test class for all file cleaning ans splitting functions
    """

    def test_convert_unix_time(self):
        """
        Tests conversion of time.
        """
        x = '1490049160615'
        self.assertEqual(convert_unix_time(x),'2017-03-20_15.32.40')


if __name__ == '__main__':
    unittest.main()