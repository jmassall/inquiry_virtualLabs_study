'''
author: sperez8
data: june 14 2017

This file contains functions and classes used by parsers to 
extracts relevant information from log data from a PhET sim
'''
import os
import json
import getpass
import math

folder = 'C:\\Users\\'+getpass.getuser()+'\\Documents\\Personal Content\\Lab_skills_study\\raw study data\\log data\\'



samplefile = '5a257a80-aa82-471d-b75c-f1113f314da1.log'
raw_file_path = os.path.join(folder+samplefile)
output_file = "log_data_1_student_example.json"
def get_one_line(raw_file_path,output_file):
    ''' opens a raw data file, grabs the first line and outpuots
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


def check_student_id(student_id):
    '''checks that the student id recorded is valid''' 
    digits = int(math.log10(int(student_id)))+1
    if digits !=8:
        raise ValueError('This student id is not 8 digits long',student_id)

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
        check_student_id(self.student_id)
        self.session_id = data['session']['session_id']
        self.date = convert_unix_time(self.session_id.split('@')[1])
        self.sim = data['session']['widget_id']

    def clean_events(self):
        '''removes all the events related to the time counter
        and the mouse actions from the self.events object'''

        cleaned_events = []
        for event in self.events:
            if event['event'] == 'phetio.stepSimulation' or event['event'] == 'phetio.inputEvent':
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
            # self.walk.append([str(event['timestamp']),str(event['type']),str(event['event'])])
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





