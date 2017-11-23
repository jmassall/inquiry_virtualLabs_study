'''
author: sperez8
data: june 14 2017

This script creates a raw log file with just the sessions desired
'''
import os
# import sys
import json
from utils import *
import getpass


# SIM = 'beers'
# IDS = ['12263156']
SIM = 'caps'
IDS = ['17931169']
# IDS = ['90447168']


datapath = 'C:\\Users\\'+getpass.getuser()+'\\Documents\\Personal Content\\Lab_study_data\\raw study data\\log data\\'
outfilename = "raw_log_{0}_{1}.json".format(SIM, '_'.join(IDS))

if SIM == 'beers':
    rawfile = '43abdd26-76bd-4fe9-9f7b-29500369038f.log' #all logs - beers
else:
    rawfile = '38663fa4-7ac5-4868-b687-82d9aa05ab37.log' #all logs caps

#open the raw data file
with open(os.path.join(datapath+rawfile),'r') as f:
    with open(outfilename, 'w') as outfile:
        #each line is a session which we load as a json element
        for line in f:
            try:
                line_json=json.loads(line) #one session is contained in here
            except:
                print "Failed to load the json data."

            #using the Session class, we extract the data and metadata from that session
            session = Session()
            session.parse_data(line_json)
            if session.student_id in IDS:
                #if you want pretty print, use print >> as below instead of just json.dump
                # print >> outfile, json.dumps(line_json, indent=4, sort_keys=True)
                # json.dump(line, outfile)
                outfile.write('{')
                outfile.write(line)
                outfile.write('}')
                break

outfile.close() 
f.close()