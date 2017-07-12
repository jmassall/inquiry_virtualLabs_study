'''
author: sperez8
data: july 11th 2017

This captures the recorded data from a single student's activity file
'''
import os
import sys
import json
from utils import *

file_to_read = 'example_parsed_student_data_file.json'
session = Session()
session.get_session_data_from_file(file_to_read)

ACTION = "labBook.recordDataButton"
for event in session.events:
	print event
	if event['data']['children']['phetioID']==ACTION:
		print event
		print event['data']['children']['parameters']
		sys.exit()

