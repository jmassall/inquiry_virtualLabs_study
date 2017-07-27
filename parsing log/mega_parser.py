'''
author: sperez8
data: july 11th 2017

This captures the recorded data from a single student's activity file
'''
import os
import sys
import re
import traceback
import json
import numpy as np
from utils import *

# def detect_recordData(event):
#     if event['event'] == "beersLawLab.simIFrameAPI.invoked":
#         if 'children' in event['data']:
#             if event['data']['children'][0]['phetioID'] == "labBook.recordDataButton":
#                 return True
#     return False

# def detect_notesActivity(event):
#     if event['event'] == "beersLawLab.simIFrameAPI.invoked":
#         if 'children' in event['data']:
#             if event['data']['children'][0]['phetioID'] == "labBook.textArea":
#                 return True
#     return False

# def parse_recordData(event):
#     data = {}
#     meat = event['data']['children'][0]['parameters']
#     data['Trial'] = meat['trialNumber']
#     data['Wavelength'] = meat['wavelength']
#     data['Width'] = meat['cuvetteWidth']
#     data['Concentration'] = meat['concentration']
#     data['Absorbance'] = meat['absorbance']
#     data['inGraph'] = meat['visible']
#     return data

# def parse_notesActivity(event):
#     notes = event['data']['children'][0]['parameters']['text']
#     return notes

# #used for testing purposes to print recordings and notes
# def iterate_and_parse(events):
#     state = 'increasing'
#     previous_notes = ''
#     print '\t'.join(['Width','inGraph?','Trial','Absorbance','Wavelength','Concentration'])
#     for i,event in enumerate(events):
#         if detect_recordData(event):
#           data = parse_recordData(event)
#           print '\t'.join([str(x) for x in data.values()])
#         if detect_notesActivity(event):
#             notes = parse_notesActivity(event)
#             print state, len(notes),len(previous_notes), notes+'.'
#             if state == 'increasing' and len(notes)<len(previous_notes):
#                 print 'out\t', notes
#                 state = 'decreasing'
#             if state == 'decreasing' and len(notes)>len(previous_notes):
#                 print 'out\t', notes
#                 state = 'increasing'
#             previous_notes = notes
#     return None

def initialize_dreamtable(header, number_of_events,first_event):
    dreamtable = np.chararray(shape=(number_of_events+1,len(header)), itemsize=100000)
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
        traceback.print_exc()
        sys.exit()

def get_data_parameters(event):
    try: 
        return get_data(event)['parameters']
    except KeyError:
        print "Error: event has no 'data > parameters'"
        traceback.print_exc()
        sys.exit()

def get_messages(event):
    try: 
        return get_data_parameters(event)['messages']
    except KeyError:
        print "Error: event has no 'data > parameters > messages'"
        traceback.print_exc()
        sys.exit()

def get_method(event):
    try: 
        return get_data_parameters(event)['method']
    except KeyError:
        print "Error: event has no 'data > parameters > method'"
        traceback.print_exc()
        sys.exit()

def get_state(event):
    try: 
        return get_data_parameters(event)['state']
    except KeyError:
        print "Error: event has no 'data > parameters > state'"
        traceback.print_exc()
        sys.exit()

def get_args(event):
    try: 
        return get_data_parameters(event)['args']
    except KeyError:
        print "Error: event has no 'data > parameters > args'"
        traceback.print_exc()
        sys.exit()

def get_args_phetioID(event):
    try: 
        return get_args(event)[0]['phetioID']
    except KeyError:
        print "Error: event has no 'data > parameters > args > phetioID'"
        traceback.print_exc()
        sys.exit()

def get_children(event):
    try: 
        return get_data(event)['children']
    except KeyError:
        print "Error: event has no 'data > children'"
        traceback.print_exc()
        sys.exit()

def get_children_parameters(event):
    try: 
        return get_children(event)[0]['parameters']
    except KeyError:
        print "Error: event has no 'data > children > parameters'"
        traceback.print_exc()
        sys.exit()

def extract_new_datapoint(event):
    datapoint = {}
    datapoint["Width"] = get_children_parameters(event)['state']["beersLawLab.beersLawScreen.model.cuvette.widthProperty"]
    datapoint["Detector location"] = get_children_parameters(event)['state']["beersLawLab.beersLawScreen.model.detector.probe.locationProperty"]
    datapoint["Absorption"] = get_children_parameters(event)['state']["beersLawLab.beersLawScreen.model.detector.valueProperty"]
    datapoint["Laser on status"] = get_children_parameters(event)['state']["beersLawLab.beersLawScreen.model.light.onProperty"]
    datapoint["Wavelength"] = get_children_parameters(event)['state']["beersLawLab.beersLawScreen.model.light.wavelengthProperty"]
    datapoint["Ruler location"] = get_children_parameters(event)['state']["beersLawLab.beersLawScreen.model.ruler.locationProperty"]
    datapoint["Concentration"] = get_children_parameters(event)['state']["beersLawLab.beersLawScreen.solutions.copperSulfate.concentrationProperty"]
    datapoint["trialNumber"] = get_children_parameters(event)["trialNumber"]
    datapoint["inGraph"] = get_children_parameters(event)["visible"]
    return datapoint

def detect_drag_event(event):
    drag_type = event.split('.')[-1]
    return drag_type

def detect_drag_item(event):
    drag_item = event.split('.')[3]
    return drag_item

def get_checkbox_status(event):
    try: 
        return get_args(event)[0]['parameters']['checked']
    except KeyError:
        print "Error: event has no 'data > parameters > args > parameters > checked'"
        traceback.print_exc()
        sys.exit()

def is_checkbox_error(event):
    try: 
        error = get_args(event)[0]['parameters']['error']
        if error == "Cannot add this data point to the plot.  Either the data is empty, you have not selected an axis feature, or the data point is not defined for the selected scale.":
            return True
    except KeyError:
        return False

def update_checkstatus_in_table(current_table, trial_added, check_status):
    new_table = current_table.copy()
    new_table[trial_added]['inGraph'] = check_status
    return new_table

EVENTS_INITIALIZING = ["beersLawLab.sim.simStarted","beersLawLab.sim.barrierRectangle.fired","beersLawLab.navigationBar.phetButton.fired"]
INITIALIZING_METHODS = ["addExpressions","launchSimulation","setText"]

def mega_parser(header, events):
    dreamtable = initialize_dreamtable(header,len(events),events[0])
    table = {}
    for i,event in enumerate(events):
        parsed = False
        method = None
        phetioID = None
        drag_event = None
        drag_item = None
        dreamtable[i+1,header.index("Timestamp")] = event['timestamp']
        dreamtable[i+1,header.index("Index")] = event['index']

        if event['event'] == "beersLawLab.simIFrameAPI.invoked":
            if 'messages' in get_data_parameters(event).keys():
                parsed = True
                dreamtable[i+1,header.index("User or Model?")] = 'model'
                dreamtable[i+1,header.index("Event")] = 'gettingValues'
                dreamtable[i+1,header.index("Item")] = 'sim'
                dreamtable[i+1,header.index("Action")] = 'none'
            else:
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
                        dreamtable[i+1,header.index("Action")] = 'none'
                    if phetioID == "labBook.tableCollapseButton":
                        parsed = True
                        dreamtable[i+1,header.index("User or Model?")] = 'user'
                        dreamtable[i+1,header.index("Event")] = 'collapsing table'
                        dreamtable[i+1,header.index("Item")] = 'table'
                        dreamtable[i+1,header.index("Action")] = 'none'
                    if phetioID == "labBook.graphExpandButton":
                        parsed = True
                        dreamtable[i+1,header.index("User or Model?")] = 'user'
                        dreamtable[i+1,header.index("Event")] = 'expanding graph'
                        dreamtable[i+1,header.index("Item")] = 'graph'
                        dreamtable[i+1,header.index("Action")] = 'none'
                    if phetioID == "labBook.graphCollapseButton":
                        parsed = True
                        dreamtable[i+1,header.index("User or Model?")] = 'user'
                        dreamtable[i+1,header.index("Event")] = 'collapsing graph'
                        dreamtable[i+1,header.index("Item")] = 'graph'
                        dreamtable[i+1,header.index("Action")] = 'none'
                    if "Feature" in phetioID:
                        parsed = True
                        selection = get_args(event)[0]['parameters']['feature']
                        variable_selected, axis = selection.split('_')
                        axis = axis.capitalize()
                        dreamtable[i+1,header.index("User or Model?")] = 'user'
                        dreamtable[i+1,header.index("Event")] = 'Selecting '+axis+'-axis'
                        dreamtable[i+1,header.index("Item")] = axis+'-axis dropdown menu'
                        dreamtable[i+1,header.index("Action")] = axis+'-axis changed to '+ variable_selected
                        dreamtable[i+1,header.index(axis+" axis")] = variable_selected

                    if phetioID == "labBook.recordDataButton":
                        parsed = True
                        dreamtable[i+1,header.index("User or Model?")] = 'user'
                        dreamtable[i+1,header.index("Event")] = 'recording data'
                        dreamtable[i+1,header.index("Item")] = 'none'
                        dreamtable[i+1,header.index("Action")] = 'none'
                        new_data_point = extract_new_datapoint(event)
                        table[new_data_point['trialNumber']] = new_data_point
                        dreamtable[i+1,header.index("Table")] = json.dumps(table)
                    if "labBook.addToGraphCheckBox" in phetioID:
                        parsed = True
                        trial_added_to_graph = int(re.search(r'\d+', phetioID).group())
                        checked = get_checkbox_status(event)
                        if is_checkbox_error(event):
                            dreamtable[i+1,header.index("Event")] = 'Adding data to graph'
                            dreamtable[i+1,header.index("Action")] = 'Error: failed to add trial.'
                            checked = False
                        elif checked:
                            dreamtable[i+1,header.index("Event")] = 'Adding data to graph'
                            dreamtable[i+1,header.index("Action")] = 'Data added to graph successfully.'
                        else:
                            dreamtable[i+1,header.index("Event")] = 'Removing data from graph'
                            dreamtable[i+1,header.index("Action")] = 'Data removed from graph.'
                        dreamtable[i+1,header.index("User or Model?")] = 'user'
                        dreamtable[i+1,header.index("Item")] = 'trialNumber ' + str(trial_added_to_graph)
                        table = update_checkstatus_in_table(table, trial_added_to_graph, checked)
                        dreamtable[i+1,header.index("Table")] = json.dumps(table)



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
            dreamtable[i+1,header.index("Laser on status")] = get_state(event)["beersLawLab.beersLawScreen.model.light.onProperty"]
            dreamtable[i+1,header.index("Wavelength")] = get_state(event)["beersLawLab.beersLawScreen.model.light.wavelengthProperty"]
            dreamtable[i+1,header.index("Ruler location")] = get_state(event)["beersLawLab.beersLawScreen.model.ruler.locationProperty"]
            dreamtable[i+1,header.index("Concentration")] = get_state(event)["beersLawLab.beersLawScreen.solutions.copperSulfate.concentrationProperty"]
        
        elif "drag" in event['event']:
            parsed = True
            drag_event = detect_drag_event(event['event'])
            drag_item = detect_drag_item(event['event'])

            dreamtable[i+1,header.index("User or Model?")] = 'user'
            dreamtable[i+1,header.index("Event")] = "dragging"
            dreamtable[i+1,header.index("Item")] = drag_item
            dreamtable[i+1,header.index("Action")] = drag_event
        
        elif event['event'] == "beersLawLab.beersLawScreen.view.lightNode.button.toggled":
            parsed = True
            dreamtable[i+1,header.index("User or Model?")] = 'user'
            dreamtable[i+1,header.index("Event")] = 'toggle laser'
            dreamtable[i+1,header.index("Item")] = 'laser button'
            dreamtable[i+1,header.index("Action")] = 'none'

        if not parsed:
            print "Error: new event type encountered at event number", i, "with index", event['index']
            break

    np.savetxt('example_dream_table.txt', dreamtable, delimiter='\t', fmt='%s')
    print "Done parsing."  
    return None


header = ["User","Sim","Timestamp","Index","User or Model?","Event","Item","Action","Laser on status","Wavelength","Width","Concentration","Absorption","Detector location","Ruler location","Table","X axis","Y axis","X axis property","Y axis property","Experiment #s included","Notes"]
test_json = 'example_cleaned_student_data_file.json'
session = Session()
session.get_session_data_from_file(test_json)
mega_parser(header, session.events)


