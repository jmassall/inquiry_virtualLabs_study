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
    digits = int(math.log10(int(student_id)))+1
    return (digits == 8)

def check_id_start(student_id):
    '''check that the student id recorded 
    starts with a 1 or not''' 
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




class Session:
    ''' A class to organize and standardize the information
    contained in a single session with a PhET virtual lab
    (stored as a JSON element on a single line of a raw log
    data file.)
    '''

    def __init__(self, filename=None):
        ''' if a filename is provided  when class is declared,
        then we parse the metadata for that session there '''

        if filename:
            self.get_session_data_from_file(filename)


    def get_session_data_from_file(self,filename):
        ''' Opens file, loads element as JSON and parses 
        the data and metadata'''

        with open((filename),'r') as f:
            try:
                data=json.load(f)
                self.parse_data(data)
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
            else:
                cleaned_events.append(event)
        self.events = cleaned_events
        return None

    def create_walk(self):
        '''grabs the relevant information from each event 
        to get a rough walk of the data'''
        
        self.walk = []
        for event in self.events:
            # self.walk.append([str(event['timestamp']),
            #                     str(event['type']),
            #                     str(event['event'])])
            self.walk.append(str(event['event']))
        return None

    def export_walk(self):
        ''' exports the walk in a text file '''

        outfile = open('example_walk.txt', 'w')
        for event in self.walk:
            # outfile.write(','.join(event)+'\n')
            outfile.write(event+'\n')

        outfile.close()


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





