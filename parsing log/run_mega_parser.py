'''
author: sperez8
data: june 14 2017

This script runs the parser on cleaned log files
'''
import os
import sys
import json
from mega_parser import *

datapath = 'C:\\Users\\'+getpass.getuser()+'\\Documents\\Personal Content\\Lab_skills_study\\cleaned log data\\cleaned_and_split_'
outpath = 'C:\\Users\\'+getpass.getuser()+'\\Documents\\Personal Content\\Lab_skills_study\\parsed log data'
# rawfilename = '43abdd26-76bd-4fe9-9f7b-29500369038f'
# rawfilename = '38663fa4-7ac5-4868-b687-82d9aa05ab37'
# rawfilename = '5a257a80-aa82-471d-b75c-f1113f314da1'
rawfilename = '241e54d6-f579-4ac5-9cbd-f37b826daea8'
in_data_path = datapath+rawfilename
parsed_data_path = os.path.join(outpath,'parsed_' + rawfilename)

#create a folder for the new data files, if one doesn't already exist.
if not os.path.exists(parsed_data_path):
    os.makedirs(parsed_data_path)

#for each cleaned log file in the folder
for f in os.listdir(in_data_path):
    
    filepath = os.path.join(in_data_path, f)

    if filepath.endswith(".json"):
        print '\n', filepath

        studentid = re.search(r'_(\d{7,8})_', filepath).group(1)
        sim = re.search(r'log_lab-book-([a-z\-]+)', filepath).group(1)
        date = re.search(r'\d{7,8}_([\d\-\.\_]+)\.json', filepath).group(1)

        outname = 'dream_table_{0}_{1}_{2}.txt'.format(sim,studentid,date)
        outfilepath = os.path.join(parsed_data_path,outname)
        if os.path.isfile(outfilepath):
            print  "ALREADY FOUND:", outname
            continue

        with open(filepath,'r') as f:
            session = Session()
            session.get_session_data_from_file(filepath)
            sim, dreamtable = mega_parser(studentid, session.events)
            f.close()
        
        with open(outfilepath, 'w') as outfile:    
            np.savetxt(outfile, dreamtable, delimiter='\t', fmt='%s')