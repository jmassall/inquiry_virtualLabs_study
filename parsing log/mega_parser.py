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

def initialize_dreamtable(studentid, header, number_of_events,first_event):
    dreamtable = np.chararray(shape=(number_of_events+1,len(header)), itemsize=100000)
    dreamtable[0,:] = header
    dreamtable[1:,header.index("User")] = studentid
    if "beersLaw" in first_event["event"]:
        sim = 'light'
        dreamtable[1:,header.index("Sim")] = sim
    start_time = first_event['timestamp']
    return sim, start_time, dreamtable

def get_data(event, verbatim = True):
    try: 
        return event['data']
    except KeyError:
        if verbatim:
            print "Error: event",event['index']," has no 'data'"
            # traceback.print_exc()
        # sys.exit()

def get_data_parameters(event, verbatim = True):
    try: 
        return get_data(event, verbatim)['parameters']
    except KeyError:
        if verbatim:
            print "Error: event",event['index']," has no 'data > parameters'"
            # traceback.print_exc()
        # sys.exit()

def get_messages(event, verbatim = True):
    try: 
        return get_data_parameters(event, verbatim)['messages']
    except KeyError:
        if verbatim:
            print "Error: event",event['index']," has no 'data > parameters > messages'"
            # traceback.print_exc()
        # sys.exit()

def get_method(event, verbatim = True):
    try: 
        return get_data_parameters(event, verbatim)['method']
    except KeyError:
        if verbatim:
            print "Error: event",event['index']," has no 'data > parameters > method'"
            # traceback.print_exc()
        # sys.exit()

def get_state(event, verbatim = True):
    try: 
        return get_data_parameters(event, verbatim)['state']
    except KeyError:
        if verbatim:
            print "Error: event",event['index']," has no 'data > parameters > state'"
            # traceback.print_exc()
        # sys.exit()

def get_args(event, verbatim = True):
    try: 
        return get_data_parameters(event, verbatim)['args']
    except KeyError:
        if verbatim:
            print "Error: event",event['index']," has no 'data > parameters > args'"
            # traceback.print_exc()
        # sys.exit()

def get_args_phetioID(event, verbatim = True):
    try: 
        return get_args(event, verbatim)[0]['phetioID']
    except KeyError:
        if verbatim:
            print "Error: event",event['index']," has no 'data > parameters > args > phetioID'"
            # traceback.print_exc()
        # sys.exit()

def get_children(event, verbatim = True):
    try: 
        return get_data(event, verbatim)['children']
    except KeyError:
        if verbatim:
            print "Error: event",event['index']," has no 'data > children'"
            # traceback.print_exc()
        # sys.exit()

def get_children_parameters(event, verbatim = True):
    try: 
        return get_children(event, verbatim)[0]['parameters']
    except KeyError:
        if verbatim:
            print "Error: event",event['index']," has no 'data > children > parameters'"
            # traceback.print_exc()
        # sys.exit()

def get_notes(event, verbatim = True):
    try:
        return get_data_parameters(event, verbatim)['text'].replace('\n','\\n')
    except KeyError:
        if verbatim:
            print "Error: event",event['index']," has no 'data > parameters > text'"
            # traceback.print_exc()
        # sys.exit()

def extract_new_datapoint(event, get_record_data_method):
    datapoint = {}
    #CHECK IN ACTUAL SIM
    #sim rounds up to 3 decimal places
    datapoint["Width"] = round(get_record_data_method(event)['state']["beersLawLab.beersLawScreen.model.cuvette.widthProperty"],2)
    datapoint["Detector location"] = {k:round(v,2) for k,v in get_record_data_method(event)['state']["beersLawLab.beersLawScreen.model.detector.probe.locationProperty"].iteritems()}
    #sim rounds up to 2 decimal places
    absorption = get_record_data_method(event)['state']["beersLawLab.beersLawScreen.model.detector.valueProperty"]
    if absorption != None:
        datapoint["Absorption"] = round(absorption,2)
    datapoint["Laser on status"] = get_record_data_method(event)['state']["beersLawLab.beersLawScreen.model.light.onProperty"]
    datapoint["Wavelength"] = get_record_data_method(event)['state']["beersLawLab.beersLawScreen.model.light.wavelengthProperty"]
    datapoint["Ruler location"] = {k:round(v,2) for k,v in get_record_data_method(event)['state']["beersLawLab.beersLawScreen.model.ruler.locationProperty"].iteritems()}
    #sim rounds up to 3 decimal places
    datapoint["Concentration"] = round(get_record_data_method(event)['state']["beersLawLab.beersLawScreen.solutions.copperSulfate.concentrationProperty"],2)
    datapoint["trialNumber"] = get_record_data_method(event)["trialNumber"]
    datapoint["inGraph"] = get_record_data_method(event)["visible"]
    return datapoint

def detect_drag_event(event):
    drag_type = event.split('.')[-1]
    return drag_type

def detect_drag_item(event):
    drag_item = event.split('.')[3]
    return drag_item

def get_drag_direction(event):
    new,old = get_new_old_values(event)
    if new > old:
        return 'increasing'
    else:
        return 'decreasing'

def get_new_old_values(event):
    values = get_children_parameters(event, verbatim = False)
    return values['newValue'],values['oldValue']

def get_checkbox_status1(event, verbatim = True):
    try: 
        return get_args(event)[0]['parameters']['checked']
    except KeyError:
        if verbatim:
            print "Error: event",event['index']," has no 'data > parameters > args > parameters > checked'"
            # traceback.print_exc()
        # sys.exit()

def get_checkbox_status2(event, verbatim = True):
    try: 
        return get_data_parameters(event)['checked']
    except KeyError:
        if verbatim:
            print "Error: event",event['index']," has no 'data > parameters > args > parameters > checked'"
            # traceback.print_exc()
        # sys.exit()


def is_checkbox_error1(event):
    try: 
        error = get_args(event)[0]['parameters']['error']
        if error == "Cannot add this data point to the plot.  Either the data is empty, you have not selected an axis feature, or the data point is not defined for the selected scale.":
            return True
    except KeyError:
        return False

def is_checkbox_error2(event):
    try: 
        error = get_data_parameters(event)['error']
        if error == "Cannot add this data point to the plot.  Either the data is empty, you have not selected an axis feature, or the data point is not defined for the selected scale.":
            return True
    except KeyError:
        return False

def update_checkstatus_in_table(current_table, trial_added, check_status):
    new_table = current_table.copy()
    new_table[trial_added]['inGraph'] = check_status
    return new_table

def remove_from_table(current_table, trial_removed):
    new_table = current_table.copy()
    del new_table[trial_removed]
    return new_table 

EVENTS_INITIALIZING = ["beersLawLab.sim.simStarted",
                        "beersLawLab.sim.barrierRectangle.fired",
                        "beersLawLab.navigationBar.phetButton.fired",
                        "beersLawLab.navigationBar.titleTextNode.textChanged"]
INITIALIZING_METHODS = ["addExpressions","launchSimulation","setText"]

def mega_parser(studentid, header, events):
    sim, first_time_stamp, dreamtable = initialize_dreamtable(studentid, header,len(events),events[0])
    table = {}
    for i,event in enumerate(events):
        parsed = False
        dreamtable[i+1,header.index("Time")] = round((event['timestamp']-first_time_stamp)/1000.0,1)
        dreamtable[i+1,header.index("Index")] = event['index']

        if event['event'] == "beersLawLab.simIFrameAPI.invoked":
            if 'messages' in get_data_parameters(event).keys():
                parsed = True
                dreamtable[i+1,header.index("User or Model?")] = 'model'
                dreamtable[i+1,header.index("Event")] = 'gettingValues'
                dreamtable[i+1,header.index("Item")] = 'sim'
            else:
                method = get_method(event)
                if method in INITIALIZING_METHODS:
                    parsed = True
                    dreamtable[i+1,header.index("User or Model?")] = 'model'
                    dreamtable[i+1,header.index("Event")] = 'initializing'
                    dreamtable[i+1,header.index("Item")] = 'sim'
                    dreamtable[i+1,header.index("Action")] = method
                else:
                    #the following are for log files after March 20th
                    phetioID = get_args_phetioID(event)
                    if phetioID == "labBook.tableExpandButton":
                        parsed = True
                        dreamtable[i+1,header.index("User or Model?")] = 'user'
                        dreamtable[i+1,header.index("Event")] = 'expanding table'
                        dreamtable[i+1,header.index("Item")] = 'table'
                    elif phetioID == "labBook.tableCollapseButton":
                        parsed = True
                        dreamtable[i+1,header.index("User or Model?")] = 'user'
                        dreamtable[i+1,header.index("Event")] = 'collapsing table'
                        dreamtable[i+1,header.index("Item")] = 'table'
                    elif phetioID == "labBook.graphExpandButton":
                        parsed = True
                        dreamtable[i+1,header.index("User or Model?")] = 'user'
                        dreamtable[i+1,header.index("Event")] = 'expanding graph'
                        dreamtable[i+1,header.index("Item")] = 'graph'
                    elif phetioID == "labBook.graphCollapseButton":
                        parsed = True
                        dreamtable[i+1,header.index("User or Model?")] = 'user'
                        dreamtable[i+1,header.index("Event")] = 'collapsing graph'
                        dreamtable[i+1,header.index("Item")] = 'graph'
                    elif "Feature" in phetioID:
                        parsed = True
                        selection = get_args(event)[0]['parameters']['feature']
                        variable_selected, axis = selection.split('_')
                        axis = axis.capitalize()
                        dreamtable[i+1,header.index("User or Model?")] = 'user'
                        dreamtable[i+1,header.index("Event")] = 'Selecting '+axis+'-axis'
                        dreamtable[i+1,header.index("Item")] = axis+'-axis dropdown menu'
                        dreamtable[i+1,header.index("Action")] = axis+'-axis changed to '+ variable_selected
                        dreamtable[i+1,header.index(axis+" axis")] = variable_selected

                    elif phetioID == "labBook.recordDataButton":
                        parsed = True
                        dreamtable[i+1,header.index("User or Model?")] = 'user'
                        dreamtable[i+1,header.index("Event")] = 'recording data'
                        new_data_point = extract_new_datapoint(event, get_children_parameters)
                        table[new_data_point['trialNumber']] = new_data_point
                        dreamtable[i+1,header.index("Table")] = json.dumps(table)
                    elif "labBook.addToGraphCheckBox" in phetioID:
                        parsed = True
                        trial_added_to_graph = int(re.search(r'\d+', phetioID).group())
                        checked = get_checkbox_status1(event)
                        if is_checkbox_error1(event):
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
                    
                    elif "labBook.deleteButton" in phetioID:
                        parsed = True
                        trial_removed_from_table = int(re.search(r'\d+', phetioID).group())
                        dreamtable[i+1,header.index("Event")] = 'Removing data from table'
                        dreamtable[i+1,header.index("Action")] = 'Data removed from from table'
                        dreamtable[i+1,header.index("User or Model?")] = 'user'
                        dreamtable[i+1,header.index("Item")] = 'trialNumber ' + str(trial_removed_from_table)
                        table = remove_from_table(table, trial_removed_from_table)
                        dreamtable[i+1,header.index("Table")] = json.dumps(table)

        #the following are for log files after March 20th
        elif event['event'] == "labBook.recordDataButton.pressed": #for log data before March 20th 2017
            parsed = True
            #THIS IS WAY #2 that RECORD DATA event looks like. See above for way # 1
            #ALWAYS update the two in the same way
            dreamtable[i+1,header.index("User or Model?")] = 'user'
            dreamtable[i+1,header.index("Event")] = 'recording data'
            new_data_point = extract_new_datapoint(event, get_data_parameters)
            table[new_data_point['trialNumber']] = new_data_point
            dreamtable[i+1,header.index("Table")] = json.dumps(table)

        elif event['event'] == "labBook.tableExpandButton.pressed":
            parsed = True
            dreamtable[i+1,header.index("User or Model?")] = 'user'
            dreamtable[i+1,header.index("Event")] = 'expanding table'
            dreamtable[i+1,header.index("Item")] = 'table'
        elif event['event'] == "labBook.tableCollapseButton.pressed":
            parsed = True
            dreamtable[i+1,header.index("User or Model?")] = 'user'
            dreamtable[i+1,header.index("Event")] = 'collapsing table'
            dreamtable[i+1,header.index("Item")] = 'table'
        elif event['event'] == "labBook.graphExpandButton.pressed":
            parsed = True
            dreamtable[i+1,header.index("User or Model?")] = 'user'
            dreamtable[i+1,header.index("Event")] = 'expanding graph'
            dreamtable[i+1,header.index("Item")] = 'graph'
        elif event['event'] == "labBook.graphCollapseButton.pressed":
            parsed = True
            dreamtable[i+1,header.index("User or Model?")] = 'user'
            dreamtable[i+1,header.index("Event")] = 'collapsing graph'
            dreamtable[i+1,header.index("Item")] = 'graph'
        elif "Feature" in event['event']:
            parsed = True
            selection = get_data_parameters(event)['feature']
            variable_selected, axis = selection.split('_')
            axis = axis.capitalize()
            dreamtable[i+1,header.index("User or Model?")] = 'user'
            dreamtable[i+1,header.index("Event")] = 'Selecting '+axis+'-axis'
            dreamtable[i+1,header.index("Item")] = axis+'-axis dropdown menu'
            dreamtable[i+1,header.index("Action")] = axis+'-axis changed to '+ variable_selected
            dreamtable[i+1,header.index(axis+" axis")] = variable_selected
        elif "Transform" in event['event']:
            parsed = True
            axis = re.search(r'\.([xy])Transform', event['event']).group(1).capitalize()
            scale = get_data_parameters(event)['feature']
            dreamtable[i+1,header.index("User or Model?")] = 'user'
            dreamtable[i+1,header.index("Event")] = 'Selecting scale of '+axis+'-axis'
            dreamtable[i+1,header.index("Item")] = axis+'-axis scale dropdown menu'
            dreamtable[i+1,header.index("Action")] = axis+'-axis scale changed to '+ scale
            dreamtable[i+1,header.index(axis+" axis scale")] = scale
        elif "labBook.addToGraphCheckBox" in event['event']:
            parsed = True
            trial_added_to_graph = int(re.search(r'\d+', event['event']).group())
            checked = get_checkbox_status2(event)
            if is_checkbox_error2(event):
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
        elif "labBook.deleteButton" in event['event']:
            parsed = True
            trial_removed_from_table = int(re.search(r'\d+', event['event']).group())
            dreamtable[i+1,header.index("Event")] = 'Removing data from table'
            dreamtable[i+1,header.index("Action")] = 'Data removed from from table'
            dreamtable[i+1,header.index("User or Model?")] = 'user'
            dreamtable[i+1,header.index("Item")] = 'trialNumber ' + str(trial_removed_from_table)
            table = remove_from_table(table, trial_removed_from_table)
            dreamtable[i+1,header.index("Table")] = json.dumps(table)
        elif "concentrationControl.slider.plusButton" in event['event']:
            parsed = True
            dreamtable[i+1,header.index("User or Model?")] = 'user'
            dreamtable[i+1,header.index("Event")] = 'Changed concentration'
            dreamtable[i+1,header.index("Action")] = 'Pressed increment button'
        elif "concentrationControl.slider.minusButton" in event['event']:
            parsed = True
            dreamtable[i+1,header.index("User or Model?")] = 'user'
            dreamtable[i+1,header.index("Event")] = 'Changed concentration'
            dreamtable[i+1,header.index("Action")] = 'Pressed decrement button'


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
            dreamtable[i+1,header.index("Width")] = round(get_state(event)["beersLawLab.beersLawScreen.model.cuvette.widthProperty"],2)
            dreamtable[i+1,header.index("Detector location")] = get_state(event)["beersLawLab.beersLawScreen.model.detector.probe.locationProperty"]
            absorption = get_state(event)["beersLawLab.beersLawScreen.model.detector.valueProperty"]
            if absorption != None:
                dreamtable[i+1,header.index("Absorption")] = round(absorption,2)
            dreamtable[i+1,header.index("Laser on status")] = get_state(event)["beersLawLab.beersLawScreen.model.light.onProperty"]
            dreamtable[i+1,header.index("Wavelength")] = get_state(event)["beersLawLab.beersLawScreen.model.light.wavelengthProperty"]
            dreamtable[i+1,header.index("Ruler location")] = get_state(event)["beersLawLab.beersLawScreen.model.ruler.locationProperty"]
            dreamtable[i+1,header.index("Concentration")] = round(get_state(event)["beersLawLab.beersLawScreen.solutions.copperSulfate.concentrationProperty"],2)
        
        elif "drag" in event['event']:
            parsed = True
            drag_event = detect_drag_event(event['event'])
            drag_item = detect_drag_item(event['event'])

            dreamtable[i+1,header.index("User or Model?")] = 'user'
            dreamtable[i+1,header.index("Event")] = drag_event
            dreamtable[i+1,header.index("Item")] = drag_item
            if drag_event == 'dragged':
                try:
                    direction = get_drag_direction(event)
                    dreamtable[i+1,header.index("Action")] = direction
                except:
                    pass

        
        elif event['event'] == "beersLawLab.beersLawScreen.view.lightNode.button.toggled":
            parsed = True
            dreamtable[i+1,header.index("User or Model?")] = 'user'
            dreamtable[i+1,header.index("Event")] = 'toggle laser'
            dreamtable[i+1,header.index("Item")] = 'laser button'

        elif event['event'] == "labBook.textArea.changed":
            parsed = True
            dreamtable[i+1,header.index("User or Model?")] = 'user'
            dreamtable[i+1,header.index("Event")] = 'editing notes'
            dreamtable[i+1,header.index("Item")] = 'notepad'
            dreamtable[i+1,header.index("Notes")] = get_notes(event)
        
        elif event['event'] == "beersLawLab.beersLawScreen.view.detectorNode.bodyNode.absorbanceRadioButton.fired":
            parsed = True
            dreamtable[i+1,header.index("User or Model?")] = 'user'
            dreamtable[i+1,header.index("Event")] = 'ignore'
            dreamtable[i+1,header.index("Item")] = 'Absorance text on'
            dreamtable[i+1,header.index("Action")] = 'user clicked on text on detector body. Ignore!'

        if not parsed:
            # print "Error: new event type encountered at event number", i, "with index", event['index']
            print '\t'+event['event'], event['index']
            # break

    np.savetxt('dream_table_{0}_{1}.txt'.format(studentid,sim), dreamtable, delimiter='\t', fmt='%s')
    print "Done parsing."  
    return None


header = ["User","Sim","Time","Index","User or Model?","Event","Item","Action","Laser on status","Wavelength","Width","Concentration","Absorption","Detector location","Ruler location","Table","X axis","Y axis","X axis scale","Y axis scale","Experiment #s included","Notes"]
# test_json = 'example_cleaned_student_data_file.json'
test_json = 'pretty_print_copy_log_lab-book-beers-law-lab_90447168_2017-01-17_11.22.45.json'
# test_json = 'pretty_print_copy_log_lab-book-beers-law-lab_83459165_2017-01-13_14.26.08.json'
studentid = re.search(r'_(\d{7,8})_', test_json).group(1)
session = Session()
session.get_session_data_from_file(test_json)
mega_parser(studentid, header, session.events)


