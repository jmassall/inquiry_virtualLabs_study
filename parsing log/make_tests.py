import os
import sys
import re
# import traceback
import json
import numpy as np
import argparse
from utils import *
from mega_parser import *

def make_parser_tests(eventtypes, studentid, events, test_file):
    '''
    This function parses the log file line by line in a 1 to 1 fashion.
    First the numy array is initialized.
    Then for each event, we tests a few if statements to try to parse the event.
    the output is saved as a tab delimited file.
    '''
    # sim, first_time_stamp, header, dreamtable = initialize_dreamtable(studentid, len(events),events[0])

    #initialize all variables
    parsed = False
    user_or_model = ''
    simevent = ''
    item = ''
    action = ''
    if sim == 'light_absorbance':
        simstate = {"Laser on status":'',"Wavelength":'',"Width":'',"Concentration":'',"Absorption":'',"Detector location":'',"Ruler location":''}
    else:
        simstate = {'Charge': '', 'Connection': '', 'Battery voltage': '', 'Separation': '', 'Area': ''}
    datatable = {}
    graphstate = {"X axis":'',"Y axis":'',"X axis scale":'',"Y axis scale":'',"Experiment #s included":''}
    notes = ''

    for i,event in enumerate(events):
        row = i+1


        #reset variables for each event - makes testing easier
        parsed = False
        user_or_model = ''
        simevent = ''
        item = ''
        action = ''
        if sim == 'light_absorbance':
            simstate = {"Laser on status":'',"Wavelength":'',"Width":'',"Concentration":'',"Absorption":'',"Detector location":'',"Ruler location":''}
        else:
            simstate = {'Charge': '', 'Connection': '', 'Battery voltage': '', 'Separation': '', 'Area': ''}
        # datatable = {}
        graphstate = {"X axis":'',"Y axis":'',"X axis scale":'',"Y axis scale":'',"Experiment #s included":''}
        notes = ''
        
        #we parse events (eventually we can parse given previous state)
        try:
            parsed, user_or_model, simevent, item, action, simstate, NEWdatatable, graphstate, notes = parse_event(sim,event, simstate.copy(), datatable.copy(), graphstate.copy(), notes)

            if parsed and simevent not in eventtypes: #if we managed to parse, we update the dreamtable
                eventtypes.append(simevent)
                test_file.write(simevent.replace(" ","_")+"_event = json.loads(''' ")
                json.dump(event, test_file, indent=4, sort_keys=True)
                test_file.write("\n''') \n\n")

                test_file.write(simevent.replace(" ","_")+"_event_"+"parsed"+" = "+str(parsed) + "\n")
                test_file.write(simevent.replace(" ","_")+"_event_"+"user_or_model"+" = '"+str(user_or_model) + "'\n")
                test_file.write(simevent.replace(" ","_")+"_event_"+"simevent"+" = '"+str(simevent) + "'\n")
                test_file.write(simevent.replace(" ","_")+"_event_"+"item"+" = '"+str(item) + "'\n")
                test_file.write(simevent.replace(" ","_")+"_event_"+"action"+" = '"+str(action) + "'\n")

                test_file.write("\n#####################################################################################################################\n")
        except:
            continue

    return eventtypes


datapath = 'C:\\Users\\'+getpass.getuser()+'\\Documents\\Personal Content\\Lab_skills_study\\cleaned log data\\cleaned_and_split_'
outpath = 'C:\\Users\\'+getpass.getuser()+'\\Documents\\Personal Content\\Lab_skills_study\\parsed log data'

rawfiles = ['43abdd26-76bd-4fe9-9f7b-29500369038f']#,'38663fa4-7ac5-4868-b687-82d9aa05ab37','5a257a80-aa82-471d-b75c-f1113f314da1','241e54d6-f579-4ac5-9cbd-f37b826daea8']


test_file = open('test_log_samples_2.txt','w')
test_file.write("import json \n\n\n")

eventtypes = []
for rawfilename in rawfiles:
    in_data_path = datapath+rawfilename

    #for each cleaned log file in the folder
    for f in os.listdir(in_data_path):
        
        filepath = os.path.join(in_data_path, f)

        if filepath.endswith(".json"):
            print '\n', filepath

            studentid = re.search(r'_(\d{7,8})_', filepath).group(1)
            sim = re.search(r'log_lab-book-([a-z\-]+)', filepath).group(1)
            date = re.search(r'\d{7,8}_([\d\-\.\_]+)\.json', filepath).group(1)

            with open(filepath,'r') as f:
                session = Session()
                session.get_session_data_from_file(filepath)
                eventtypes = make_parser_tests(eventtypes, 'test',session.events, test_file)