'''
author: sperez8
data: june 14 2017

This file contains functions and classes used by parsers to 
extracts relevant information from log data from a PhET sim
'''
import sys
import os
import json
import getpass
import math



def find_student_log_file(infolder, sim, studentid):
    for root, dirs, files in os.walk(infolder):
        for f in files:
            if sim in f and studentid in f:
                return os.path.join(root, f)
                
def get_one_line(raw_file_path,output_file):
    ''' opens a raw data file, grabs the first line and outputs
     it in pretty print format in a new file.'''

    out = open(output_file, "w") 

    data = []
    with open(raw_file_path,'r') as f:
        for line in f:
            try:
                line_json=json.loads(line)
                print >> out, json.dumps(line_json, indent=4, sort_keys=True)
            except:
                pass
            break

    f.close()
    out.close()
    return None

import datetime

def convert_unix_time(t):
    ''' Take a unix time stamp in milliseconds and convert to date and time'''
    return datetime.datetime.fromtimestamp(int(t)/1000.0).strftime('%Y-%m-%d_%H.%M.%S')


def check_id_length(student_id):
    '''check that the student id recorded 
    has the right number of digits''' 
    if student_id == 'student1': #this is only the case for really old log data
        return 'NA'
    else:
        digits = int(math.log10(int(student_id)))+1
        return (digits == 8)

def check_id_start(student_id):
    '''check that the student id recorded 
    starts with a 1 or not''' 
    if student_id == 'student1': #this is only the case for really old log data
        return 'NA'
    else:
        start  = int(student_id[0])
        return (start == 1)

STEP_EVENT_CHILDREN = set(["data","event","index","timestamp","type"])
STEP_EVENT_DATA_CHILDREN = set(["componentType","event","eventType","messageIndex","parameters","phetioID",'time'])

def check_step_event(event):
    '''check that event has correct structure, else print'''
    children = set(event.keys())
    if children != STEP_EVENT_CHILDREN:
        print "Step event has different children:"
        print json.dumps(event)
        sys.exit()
    data_children = set(event['data'].keys())
    if data_children != STEP_EVENT_DATA_CHILDREN:
        print "Step event has different 'data' children:"
        print json.dumps(event)
        sys.exit()
    if event['data']['event'] != 'stepSimulation':
        print "Step event's data['event'] item looks different:"
        print json.dumps(event)
        sys.exit()
    if event['data']['parameters'].keys() != ['dt']:
        print "Step event'd data['parameters'] looks different:"
        print json.dumps(event)
        sys.exit()
    return None

INPUT_EVENT_CHILDREN = set(["data","event","index","timestamp","type"])
INPUT_EVENT_DATA_CHILDREN = set(["componentType","event","eventType","messageIndex","parameters","phetioID","time"])
def check_input_event(event):
    '''check that event has correct structure, else print'''
    children = set(event.keys())
    if children != INPUT_EVENT_CHILDREN:
        print "Input event has different children:"
        print json.dumps(event)
        sys.exit()
    data_children = set(event['data'].keys())
    if data_children != INPUT_EVENT_DATA_CHILDREN:
        print "Input event has different 'data' children:"
        print json.dumps(event)
        sys.exit()
    if event['data']['event'] != 'inputEvent':
        print "Input event's data['event'] item looks different:"
        print json.dumps(event)
        sys.exit()
    if ("validatePointers" not in str(event['data']['parameters']['string']) and
        "mouseMove" not in str(event['data']['parameters']['string']) and
        "mouseOver" not in str(event['data']['parameters']['string']) and
        "mouseDown" not in str(event['data']['parameters']['string']) and
        "mouseUp" not in str(event['data']['parameters']['string']) and
        "wheel" not in str(event['data']['parameters']['string']) and
        "keyDown" not in str(event['data']['parameters']['string']) and
        "keyUp" not in str(event['data']['parameters']['string']) and
        "mouseOut" not in str(event['data']['parameters']['string']) ):
        print "Input event's data['parameters'] looks different:"
        print json.dumps(event)
        sys.exit()
    return None


CAP_SIM_SWITCH_HOVER_ACTIONS = ["capacitorLabBasics.lightBulbScreen.view.lightBulbCircuitNode.bottomSwitchNode.batteryConnectionAreaNode.buttonListener.down", 
                                "capacitorLabBasics.lightBulbScreen.view.lightBulbCircuitNode.bottomSwitchNode.batteryConnectionAreaNode.buttonListener.fire", 
                                "capacitorLabBasics.lightBulbScreen.view.lightBulbCircuitNode.bottomSwitchNode.batteryConnectionAreaNode.buttonListener.out", 
                                "capacitorLabBasics.lightBulbScreen.view.lightBulbCircuitNode.bottomSwitchNode.batteryConnectionAreaNode.buttonListener.over", 
                                "capacitorLabBasics.lightBulbScreen.view.lightBulbCircuitNode.bottomSwitchNode.batteryConnectionAreaNode.buttonListener.up",
                                "capacitorLabBasics.lightBulbScreen.view.lightBulbCircuitNode.bottomSwitchNode.openConnectionAreaNode.buttonListener.down", 
                                "capacitorLabBasics.lightBulbScreen.view.lightBulbCircuitNode.bottomSwitchNode.openConnectionAreaNode.buttonListener.fire", 
                                "capacitorLabBasics.lightBulbScreen.view.lightBulbCircuitNode.bottomSwitchNode.openConnectionAreaNode.buttonListener.out", 
                                "capacitorLabBasics.lightBulbScreen.view.lightBulbCircuitNode.bottomSwitchNode.openConnectionAreaNode.buttonListener.over", 
                                "capacitorLabBasics.lightBulbScreen.view.lightBulbCircuitNode.bottomSwitchNode.openConnectionAreaNode.buttonListener.up", 
                                "capacitorLabBasics.lightBulbScreen.view.lightBulbCircuitNode.bottomSwitchNode.wireSwitchListener.down", 
                                "capacitorLabBasics.lightBulbScreen.view.lightBulbCircuitNode.bottomSwitchNode.wireSwitchListener.fire", 
                                "capacitorLabBasics.lightBulbScreen.view.lightBulbCircuitNode.bottomSwitchNode.wireSwitchListener.out", 
                                "capacitorLabBasics.lightBulbScreen.view.lightBulbCircuitNode.bottomSwitchNode.wireSwitchListener.over", 
                                "capacitorLabBasics.lightBulbScreen.view.lightBulbCircuitNode.bottomSwitchNode.wireSwitchListener.up", 
                                "capacitorLabBasics.lightBulbScreen.view.lightBulbCircuitNode.topSwitchNode.batteryConnectionAreaNode.buttonListener.down", 
                                "capacitorLabBasics.lightBulbScreen.view.lightBulbCircuitNode.topSwitchNode.batteryConnectionAreaNode.buttonListener.fire", 
                                "capacitorLabBasics.lightBulbScreen.view.lightBulbCircuitNode.topSwitchNode.batteryConnectionAreaNode.buttonListener.out", 
                                "capacitorLabBasics.lightBulbScreen.view.lightBulbCircuitNode.topSwitchNode.batteryConnectionAreaNode.buttonListener.over", 
                                "capacitorLabBasics.lightBulbScreen.view.lightBulbCircuitNode.topSwitchNode.batteryConnectionAreaNode.buttonListener.up",
                                "capacitorLabBasics.lightBulbScreen.view.lightBulbCircuitNode.topSwitchNode.openConnectionAreaNode.buttonListener.down", 
                                "capacitorLabBasics.lightBulbScreen.view.lightBulbCircuitNode.topSwitchNode.openConnectionAreaNode.buttonListener.fire", 
                                "capacitorLabBasics.lightBulbScreen.view.lightBulbCircuitNode.topSwitchNode.openConnectionAreaNode.buttonListener.out", 
                                "capacitorLabBasics.lightBulbScreen.view.lightBulbCircuitNode.topSwitchNode.openConnectionAreaNode.buttonListener.over", 
                                "capacitorLabBasics.lightBulbScreen.view.lightBulbCircuitNode.topSwitchNode.openConnectionAreaNode.buttonListener.up", 
                                "capacitorLabBasics.lightBulbScreen.view.lightBulbCircuitNode.topSwitchNode.wireSwitchListener.down", 
                                "capacitorLabBasics.lightBulbScreen.view.lightBulbCircuitNode.topSwitchNode.wireSwitchListener.fire", 
                                "capacitorLabBasics.lightBulbScreen.view.lightBulbCircuitNode.topSwitchNode.wireSwitchListener.out", 
                                "capacitorLabBasics.lightBulbScreen.view.lightBulbCircuitNode.topSwitchNode.wireSwitchListener.over", 
                                "capacitorLabBasics.lightBulbScreen.view.lightBulbCircuitNode.topSwitchNode.wireSwitchListener.up"]


class Session:
    ''' A class to organize and standardize the information
    contained in a single session with a PhET virtual lab
    (stored as a JSON element on a single line of a raw log
    data file.)
    '''

    def __init__(self, single_session_file=None):
        ''' if a single_session_file is provided  when class is declared,
        then we parse the metadata for that session there '''

        if single_session_file:
            self.get_session_data_from_file(single_session_file)

        self.events =   None
        self.student_id =   None
        self.session_id =   None
        self.date = None
        self.sim =  None

        return None


    def get_session_data_from_file(self,single_session_file):
        ''' Opens file, loads element as JSON and parses 
        the data and metadata'''
        with open(single_session_file,'r') as f:
            try:
                self.events=json.load(f)
            except:
                pass
        f.close()
        return None

    def parse_data(self,data):
        ''' grab all the data (events) and metadata
        from the file and stores it as Class attributes'''

        self.events = data['events']
        self.student_id = data['session']['learner_id']
        self.session_id = data['session']['session_id']
        self.date = convert_unix_time(self.session_id.split('@')[1])
        self.sim = data['session']['widget_id']

    def clean_events(self):
        '''removes all the events related to the time counter
        and the mouse actions from the self.events object'''

        cleaned_events = []
        for event in self.events:
            if event['event'] == 'phetio.stepSimulation':
                # this was run on all events in a raw data file for testing purposes.
                # check_step_event(event) 
                pass
            elif event['event'] == 'phetio.inputEvent':
                # this was run on all events in a raw data file for testing purposes.
                # check_input_event(event)
                pass
            elif event['event'] in CAP_SIM_SWITCH_HOVER_ACTIONS:
                #These actions occur when user hovers over switch (different event than clicking on switch)
                pass
            elif event['event'] == "capacitorLabBasics.lightBulbScreen.model.circuit.switchedCapacitor.platesVoltageProperty.changed":
                #This happens when the voltage of the capacitor changes when connected to the lightbulb. This information is not useful to us.
                #All the info we need is in the update state events
                pass
            elif event['event'] == "capacitorLabBasics.lightBulbScreen.model.circuit.currentAmplitudeProperty.changed":
                #This happens when the amplitude is changed but we care about voltage which is outputted by state so we ignore this event
                pass
            elif event['event'] == "beersLawLab.beersLawScreen.view.detectorNode.bodyNode.absorbanceRadioButton.fired":
                #This happens when the user clicks on the tex on the body of the detector (no consequences to this action so we ignore)
                pass
            else:
                cleaned_events.append(event)
        self.events = cleaned_events
        return None

    # def create_walk(self):
    #     '''grabs the relevant information from each event 
    #     to get a rough walk of the data'''
        
    #     self.walk = []
    #     for event in self.events:
    #         # self.walk.append([str(event['timestamp']),
    #         #                     str(event['type']),
    #         #                     str(event['event'])])
    #         self.walk.append(str(event['event']))
    #     return None

    # def export_walk(self):
    #     ''' exports the walk in a text file '''

    #     outfile = open('example_walk.txt', 'w')
    #     for event in self.walk:
    #         # outfile.write(','.join(event)+'\n')
    #         outfile.write(event+'\n')

    #     outfile.close()


#HOW TO USE THE SESSION CLASS?

    # filename = "log_data_1_student_example.json"
    # session = Session(filename) where filename is a file with a single json element
    # or
    # session = Session()
    # session.parse_data(line_json) where line_json is a loaded json element

    # then we can do fun things:
    # print session.student_id
    # print len(session.events)
    # session.clean_events()
    # print len(session.events)
    # session.create_walk()
    # session.export_walk()



# HOW TO GET ALL FINAL NOTES FROM FILES
#let's iterate thorugh all raw files for beerslaw and capture the last note state for all students. Yeah!

# datapath = 'C:\\Users\\'+getpass.getuser()+'\\Documents\\Personal Content\\Lab_skills_study\\cleaned log data\\cleaned_and_split_5a257a80-aa82-471d-b75c-f1113f314da1'
# session_file = 'log_lab-book-beers-law-lab_12288167_2017-03-22_11.40.14.json'
# test_json =  os.path.join(datapath,session_file)


# notes_report = open('reports_on_notes.txt','w')
# notes_report.write('\t'.join(['filename','notes']))
# for file in os.listdir(datapath):
#     if file.endswith(".json"):
#         notes_report.write('\n')
#         session_file = os.path.join(datapath, file)
#         notes_report.write(file)
#         session = Session()
#         session.get_session_data_from_file(session_file)
#         notes = ''
#         for i,event in enumerate(session.events):
#             if detect_notesActivity(event):
#                 notes = parse_notesActivity(event)
#         notes_report.write('\t')
#         notes_report.write(notes)



