'''
author: sperez8
data: june 14 2017

This script cleans raw log files and splits them into individual session files stored in the log data folder
'''
import os
import json
from utils import Session
import getpass
datapath = 'C:\\Users\\'+getpass.getuser()+'\\Documents\\Personal Content\\Lab_skills_study\\raw study data\\log data\\'
rawfile = '5a257a80-aa82-471d-b75c-f1113f314da1.log'
split_data_path = os.path.join(datapath,'cleaned_and_split_' + rawfile.split('.')[0])

if not os.path.exists(split_data_path):
    os.makedirs(split_data_path)


with open(os.path.join(datapath+rawfile),'r') as f:
    for line in f:
        try:
            line_json=json.loads(line) #one session is contained in here
        except:
            print "Failed to load the json data."

        session = Session()
        session.parse_data(line_json)
        session.clean_events()
        outname = "log_{0}_{1}_{2}.json".format(session.sim, session.student_id, session.session_id)
        with open(os.path.join(split_data_path,outname), 'w') as outfile:
            #if you want pretty print, use print >> as below
            # print >> outfile, json.dumps(sesion.events, indent=4, sort_keys=True)
            #else this works:
            json.dump(session.events, outfile)

        outfile.close()
f.close()

# TO DO!!
# Move the files to a better location (right now it's in the raw data file)
# Add a README in that folder
# check that all the stepSimulations and inputEvent look the same to make sure we are removing what we think we are removing
# run for all raw data files? or maybe just the two biggest ones
# check that Session(filename) still works
# start with table events? start findout out all the type of events related to the table and documenting where the relevant info is stored
