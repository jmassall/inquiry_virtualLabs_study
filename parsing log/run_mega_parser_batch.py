'''
author: sperez8
data: june 14 2017

This script runs the parser on cleaned log files
'''
import os
import sys
import json
import traceback
from mega_parser import *

datapath = 'C:\\Users\\'+getpass.getuser()+'\\Documents\\Personal Content\\Lab_skills_study\\cleaned log data\\cleaned_and_split_'
outpath = 'C:\\Users\\'+getpass.getuser()+'\\Documents\\Personal Content\\Lab_skills_study\\parsed log data'

rawfiles = ['43abdd26-76bd-4fe9-9f7b-29500369038f','38663fa4-7ac5-4868-b687-82d9aa05ab37']
# rawfiles = ['38663fa4-7ac5-4868-b687-82d9aa05ab37'] #caps
# rawfiles = ['43abdd26-76bd-4fe9-9f7b-29500369038f'] #light

for rawfilename in rawfiles:
    in_data_path = datapath+rawfilename
    parsed_data_path = os.path.join(outpath,'parsed_' + rawfilename)

    #create a folder for the new data files, if one doesn't already exist.
    if not os.path.exists(parsed_data_path):
        os.makedirs(parsed_data_path)

    #for each cleaned log file in the folder
    for f in os.listdir(in_data_path):
        
        filepath = os.path.join(in_data_path, f)

        if filepath.endswith(".json"):

            if "student1" in filepath:
                studentid = "student1"
                date = re.search(r'student1_([\d\-\.\_]+)\.json', filepath).group(1)
            else:
                studentid = re.search(r'_(\d{7,8})_', filepath).group(1)
                date = re.search(r'\d{7,8}_([\d\-\.\_]+)\.json', filepath).group(1)
            sim = re.search(r'log_lab-book-([a-z\-]+)', filepath).group(1)

            outname = 'dream_table_{0}_{1}_{2}.txt'.format(sim,studentid,date)
            outfilepath = os.path.join(parsed_data_path,outname)
            if os.path.isfile(outfilepath):
                # print  "ALREADY FOUND:", outname
                continue
            else:
                print '\n', filepath

            with open(filepath,'r') as f:
                session = Session()
                session.get_session_data_from_file(filepath)
                if len(session.events) == 0:
                    print "Log file has no events. Parsing skipped"
                    continue
                try: 
                    sim, dreamtable = mega_parser(studentid, session.events)
                except Exception, e:
                    e = sys.exc_info()
                    print "Parsing failed:", filepath
                    print e[0]
                    print e[1]
                    print traceback.print_tb(e[2])
                    continue
                f.close()
            
            with open(outfilepath, 'w') as outfile:    
                np.savetxt(outfile, dreamtable, delimiter='\t', fmt='%s')