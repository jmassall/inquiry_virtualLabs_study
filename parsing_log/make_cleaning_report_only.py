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

datapath = 'C:\\Users\\'+getpass.getuser()+'\\Documents\\Personal Content\\Lab_study_data\\cleaned log data'
# rawfile = "e92af660-e970-4c28-b3e2-e09ad0fe3963.log" #redownloaded beers logs
rawfile = "7a95ceca-40b6-4d54-99f4-6bec8f161524.log" #redownloaded beers logs

report_path = os.path.join('C:\\Users\\'+getpass.getuser()+'\\Desktop','report_of_cleaning_of_file_' + rawfile.split('.')[0] +'.txt')
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

        report.write('\n')
        report.write('\t'.join([session.session_id,session.student_id,str(check_id_length(session.student_id)), str(check_id_start(session.student_id)),session.sim, session.date,str(before_cleaning), str(len(session.events)), outname]))


f.close()
report.close()