'''
author: sperez8
data: june 14 2017

This script cleans raw log files and splits them into individual session files stored in the log data folder
'''
from utils import convert_unix_time

# content of test_sample.py
def test_convert_unix_time():
	x = '1490049160615'
	assert convert_unix_time(x) == '2017-03-20_15.32.40'