'''
author: sperez8
data: june 14 2017

This script extracts relevant information from log data from a PhET sim
'''
import os
import json
import getpass
from utils import Session

folder = 'C:\\Users\\'+getpass.getuser()+'\\Documents\\Personal Content\\Lab_skills_study\\raw study data\\log data\\'
samplefile = '5a257a80-aa82-471d-b75c-f1113f314da1.log'


# this function graphs the first line of a raw data file and outputs it.
def get_one_line():
    outfile = open("log_data_1_student_example.txt", "w") 

    data = []
    with open(os.path.join(folder+samplefile),'r') as f:
        for line in f:
    		try:
    			line_json=json.loads(line)
    			print >> outfile, json.dumps(line_json, indent=4, sort_keys=True)
    		except:
    			pass
    		break

    f.close()
    outfile.close()
    return None


#demo of how Session class works
filename = "log_data_1_student_example.json"
session = Session(filename)
print session.student_id
print len(session.all_events)
session.clean_events()
print len(session.events)
session.create_walk()
session.export_walk()


