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
# rawfilename = '43abdd26-76bd-4fe9-9f7b-29500369038f'
# rawfilename = '38663fa4-7ac5-4868-b687-82d9aa05ab37'
# rawfilename = '5a257a80-aa82-471d-b75c-f1113f314da1'
# rawfilename = '241e54d6-f579-4ac5-9cbd-f37b826daea8'

# rawfiles = ['43abdd26-76bd-4fe9-9f7b-29500369038f','38663fa4-7ac5-4868-b687-82d9aa05ab37']
rawfiles = ['38663fa4-7ac5-4868-b687-82d9aa05ab37'] ##capacitors sim logs
REPARSE = False #if the parsed file already exists, we don't reparse and replace it.

IDS = ['12345678','12345678','12665164','16136159','17576140','17655165','18866165']
DATES = ['2016-11-08_14.23.13','2016-11-08_14.23.13','2017-03-21_18.25.09','2017-03-20_16.24.32','2017-03-22_16.25.06','2017-03-28_15.29.17','2017-03-20_16.24.18']


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
            print parsed_data_path
            sys.exit()

            if studentid not in IDS and date not in DATES:
                continue

            if os.path.isfile(outfilepath) and not REPARSE:
                # print  "ALREADY FOUND:", outname
                continue
            else:
                print '\n', filepath

            try:
                with open(filepath,'r') as f:
                    session = Session()
                    session.get_session_data_from_file(filepath)
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
            except:
                print "File not found.\n"
                sys.exit()
            
            with open(outfilepath, 'w') as outfile:    
                np.savetxt(outfile, dreamtable, delimiter='\t', fmt='%s')