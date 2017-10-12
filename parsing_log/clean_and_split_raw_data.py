'''
author: sperez8
data: june 14 2017

This script cleans raw log files and splits them into individual session files stored in the log data folder
'''
import os
# import sys
import json
from utils import *
import getpass

datapath = 'C:\\Users\\'+getpass.getuser()+'\\Documents\\Personal Content\\Lab_skills_study\\raw study data\\log data\\'
outpath =  'C:\\Users\\'+getpass.getuser()+'\\Documents\\Personal Content\\Lab_skills_study\\cleaned log data'
# rawfile = '43abdd26-76bd-4fe9-9f7b-29500369038f.log' #all logs - beers
rawfile = '38663fa4-7ac5-4868-b687-82d9aa05ab37.log' #all logs caps
##### rawfile = '5a257a80-aa82-471d-b75c-f1113f314da1.log'
##### rawfile = '241e54d6-f579-4ac5-9cbd-f37b826daea8.log'


split_data_path = os.path.join(outpath,'cleaned_and_split_' + rawfile.split('.')[0])

#create a folder for the new data files, if one doesn't already exist.
if not os.path.exists(split_data_path):
    os.makedirs(split_data_path)

report_path = os.path.join(outpath,'report_of_cleaning_of_file_' + rawfile.split('.')[0] +'.txt')
report = open(report_path, 'w')
report.write('\t'.join(['session id','student id','id has 8 digits', 'id start with 1','sim','date','number of events before cleaning','number of events after cleaning','file name']))


#open the raw data file
with open(os.path.join(datapath+rawfile),'r') as f:
    #each line is a session which we load as a json element
    for line in f:
        try:
            line_json=json.loads(line) #one session is contained in here
        except:
            print "Failed to load the json data."

        #using the Session class, we extract the data and metadata from that session
        session = Session()
        session.parse_data(line_json)
        before_cleaning = len(session.events)
        session.clean_events()  #removes all time tracking and mouse tracking events
        outname = "log_{0}_{1}_{2}.json".format(session.sim, session.student_id, session.date)
        with open(os.path.join(split_data_path,outname), 'w') as outfile:
            #if you want pretty print, use print >> as below instead of just json.dump
            # print >> outfile, json.dumps(session.events, indent=4, sort_keys=True)
            json.dump(session.events, outfile)
        #we report the metadata on all the session in a separate file.
        report.write('\n')
        report.write('\t'.join([session.session_id,session.student_id,str(check_id_length(session.student_id)), str(check_id_start(session.student_id)),session.sim, session.date,str(before_cleaning), str(len(session.events)), outname]))
        outfile.close()

f.close()
report.close()