'''
author: sperez8
data: july 11th 2017

This captures the recorded data from a single student's activity file
'''
import os
import sys
import json
import numpy as np
from utils import *

def detect_recordData(event):
    if event['event'] == "beersLawLab.simIFrameAPI.invoked":
        if 'children' in event['data']:
            if event['data']['children'][0]['phetioID'] == "labBook.recordDataButton":
                return True
    return False

def detect_notesActivity(event):
    if event['event'] == "beersLawLab.simIFrameAPI.invoked":
        if 'children' in event['data']:
            if event['data']['children'][0]['phetioID'] == "labBook.textArea":
                return True
    return False

def parse_recordData(event):
    data = {}
    meat = event['data']['children'][0]['parameters']
    data['Trial'] = meat['trialNumber']
    data['Wavelength'] = meat['wavelength']
    data['Width'] = meat['cuvetteWidth']
    data['Concentration'] = meat['concentration']
    data['Absorbance'] = meat['absorbance']
    data['inGraph'] = meat['visible']
    return data

def parse_notesActivity(event):
    notes = event['data']['children'][0]['parameters']['text']
    return notes

#used for testing purposes to print recordings and notes
def iterate_and_parse(events):
    state = 'increasing'
    previous_notes = ''
    print '\t'.join(['Width','inGraph?','Trial','Absorbance','Wavelength','Concentration'])
    for i,event in enumerate(events):
        if detect_recordData(event):
          data = parse_recordData(event)
          print '\t'.join([str(x) for x in data.values()])
        if detect_notesActivity(event):
            notes = parse_notesActivity(event)
            print state, len(notes),len(previous_notes), notes+'.'
            if state == 'increasing' and len(notes)<len(previous_notes):
                print 'out\t', notes
                state = 'decreasing'
            if state == 'decreasing' and len(notes)>len(previous_notes):
                print 'out\t', notes
                state = 'increasing'
            previous_notes = notes
    return None

def initialize_dreamtable(header, number_of_events,first_event):
    dreamtable = np.chararray(shape=(number_of_events+1,len(header)), itemsize=100)
    dreamtable[0,:] = header
    dreamtable[1:,header.index("User")] = 'test'
    if first_event["event"] == "beersLawLab.simIFrameAPI.invoked":
        dreamtable[1:,header.index("Sim")] = 'light'
    return dreamtable

def get_data(event):
    try: 
        return event['data']
    except KeyError:
        print "Error: event has no 'data'"
        sys.exit()

def get_data_parameters(event):
    try: 
        return get_data(event)['parameters']
    except KeyError:
        print "Error: event has no 'parameters' under 'data'"
        sys.exit()

def get_method(event):
    try: 
        return get_data_parameters(event)['method']
    except KeyError:
        print "Error: event has no 'method' under 'parameters' under 'data'"
        sys.exit()

def get_state(event):
    try: 
        return get_data_parameters(event)['state']
    except KeyError:
        print "Error: event has no 'state' under 'parameters' under 'data'"
        sys.exit()

def get_args(event):
    try: 
        return get_data_parameters(event)['args']
    except KeyError:
        print "Error: event has no 'args' under 'parameters' under 'data'"
        sys.exit()

def get_args_phetioID(event):
    try: 
        return get_args(event)[0]['phetioID']
    except KeyError:
        print "Error: event has no 'phetioID' under 'args' under 'parameters' under 'data'"
        sys.exit()

EVENTS_INITIALIZING = ["beersLawLab.sim.simStarted","beersLawLab.sim.barrierRectangle.fired","beersLawLab.navigationBar.phetButton.fired"]
INITIALIZING_METHODS = ["addExpressions","launchSimulation","setText"]

def mega_parser(header, events):
    dreamtable = initialize_dreamtable(header,len(events),events[0])

    for i,event in enumerate(events):
        print i, event['index']
        parsed = False
        method = None
        phetioID = None
        dreamtable[i+1,header.index("Timestamp")] = event['timestamp']
        dreamtable[i+1,header.index("Index")] = event['index']

        if event['event'] == "beersLawLab.simIFrameAPI.invoked":
            method = get_method(event)
            if method in INITIALIZING_METHODS:
                parsed = True
                dreamtable[i+1,header.index("User or Model?")] = 'model'
                dreamtable[i+1,header.index("Event")] = 'initializing'
                dreamtable[i+1,header.index("Item")] = 'sim'
                dreamtable[i+1,header.index("Action")] = method
            else:
                phetioID = get_args_phetioID(event)
                if phetioID == "labBook.tableExpandButton":
                    parsed = True
                    dreamtable[i+1,header.index("User or Model?")] = 'user'
                    dreamtable[i+1,header.index("Event")] = 'expanding table'
                    dreamtable[i+1,header.index("Item")] = 'table'
                    dreamtable[i+1,header.index("Action")] = 'expansion'

        elif event['event'] in EVENTS_INITIALIZING:
            parsed = True
            dreamtable[i+1,header.index("User or Model?")] = 'model'
            dreamtable[i+1,header.index("Event")] = 'initializing'
            dreamtable[i+1,header.index("Item")] = 'sim'
            dreamtable[i+1,header.index("Action")] = event['event']
        
        elif event['event'] == "phetio.state":
            parsed = True
            dreamtable[i+1,header.index("User or Model?")] = 'model'
            dreamtable[i+1,header.index("Event")] = 'updating state'
            dreamtable[i+1,header.index("Item")] = 'none'
            dreamtable[i+1,header.index("Action")] = 'none'
            dreamtable[i+1,header.index("Width")] = get_state(event)["beersLawLab.beersLawScreen.model.cuvette.widthProperty"]
            dreamtable[i+1,header.index("Detector location")] = get_state(event)["beersLawLab.beersLawScreen.model.detector.probe.locationProperty"]
            dreamtable[i+1,header.index("Absorption")] = get_state(event)["beersLawLab.beersLawScreen.model.detector.valueProperty"]
            dreamtable[i+1,header.index("laser on")] = get_state(event)["beersLawLab.beersLawScreen.model.light.onProperty"]
            dreamtable[i+1,header.index("Wavelength")] = get_state(event)["beersLawLab.beersLawScreen.model.light.wavelengthProperty"]
            dreamtable[i+1,header.index("Ruler location")] = get_state(event)["beersLawLab.beersLawScreen.model.ruler.locationProperty"]
            dreamtable[i+1,header.index("Concentration")] = get_state(event)["beersLawLab.beersLawScreen.solutions.copperSulfate.concentrationProperty"]


        if not parsed:
            print "Error: new event type encountered at event number", i, "with index", event['index']
            break
    print dreamtable[i:i+2,:]
    return None


header = ["User","Sim","Timestamp","Index","User or Model?","Event","Item","Action","laser on","Wavelength","Width","Concentration","Absorption","Detector location","Ruler location","Table","X axis","Y axis","X axis property","Y axis property","Experiment #s included","Notes"]
test_json = 'example_parsed_student_data_file.json'
session = Session()
session.get_session_data_from_file(test_json)
mega_parser(header, session.events)


