'''
author: sperez8
data: july 11th 2017

This captures the recorded data from a single student's activity file
'''
import os
import sys
import re
# import traceback
import json
import numpy as np
from utils import *

def initialize_dreamtable(studentid, header, number_of_events,first_event):
    '''
    Creates a numpy array with as many columns as the length of the header of the table
    and as many rows as the number of events (+1 for header)
    It also uses the first event to find the sim. It then populates the sim and studentid column.
    It returns the sim, the first time stamp and the initialized table.
    '''
    dreamtable = np.chararray(shape=(number_of_events+1,len(header)), itemsize=100000)
    dreamtable[0,:] = header
    dreamtable[1:,header.index("User")] = studentid
    if "beersLaw" in first_event["event"]:
        sim = 'light absorbance'
    else:
        sim = 'capacitor charge'
    dreamtable[1:,header.index("Sim")] = sim
    start_time = first_event['timestamp']
    return sim, start_time, dreamtable

def get_data(event, print_error = True):
    '''
    Grabs the information under the first event key "data"
    '''
    try: 
        return event['data']
    except KeyError:
        if print_error:
            print "Error: event",event['index']," has no 'data'"
            # traceback.print_exc()

def get_data_parameters(event, print_error = True):
    '''
    Grabs the information under the event's data > parameters
    '''
    try: 
        return get_data(event, print_error)['parameters']
    except KeyError:
        if print_error:
            print "Error: event",event['index']," has no 'data > parameters'"
            # traceback.print_exc()

def get_messages(event, print_error = True):
    '''
    Grabs the information under the event's data > parameters > messages
    '''
    try: 
        return get_data_parameters(event, print_error)['messages']
    except KeyError:
        if print_error:
            print "Error: event",event['index']," has no 'data > parameters > messages'"
            # traceback.print_exc()

def get_method(event, print_error = True):
    '''
    Grabs the information under the event's data > parameters > method
    '''
    try: 
        return get_data_parameters(event, print_error)['method']
    except KeyError:
        if print_error:
            print "Error: event",event['index']," has no 'data > parameters > method'"
            # traceback.print_exc()

def get_state(event, print_error = True):
    '''
    Grabs the state information under the event's data > parameters > state
    '''
    try: 
        return get_data_parameters(event, print_error)['state']
    except KeyError:
        if print_error:
            print "Error: event",event['index']," has no 'data > parameters > state'"
            # traceback.print_exc()

def get_data_parameters_args(event, print_error = True):
    '''
    Grabs the information under the event's data > parameterers > args
    '''
    try: 
        return get_data_parameters(event, print_error)['args']
    except KeyError:
        if print_error:
            print "Error: event",event['index']," has no 'data > parameters > args'"
            # traceback.print_exc()

def get_args_phetioID(event, print_error = True):
    '''
    Grabs the information under the event's data > parameters > args > phetioID
    '''
    try: 
        return get_data_parameters_args(event, print_error)[0]['phetioID']
    except KeyError:
        if print_error:
            print "Error: event",event['index']," has no 'data > parameters > args > phetioID'"
            # traceback.print_exc()

def get_data_children(event, print_error = True):
    '''
    Grabs the information under the event's data > children
    '''
    try: 
        return get_data(event, print_error)['children']
    except KeyError:
        if print_error:
            print "Error: event",event['index']," has no 'data > children'"
            # traceback.print_exc()

def get_data_children_parameters(event, print_error = True):
    '''
    Grabs the information under the event's data > children > parameters
    '''
    try: 
        return get_data_children(event, print_error)[0]['parameters']
    except KeyError:
        if print_error:
            print "Error: event",event['index']," has no 'data > children > parameters'"
            # traceback.print_exc()

def get_notes(event, print_error = True):
    '''
    Grabs the notes under the event's data > parameters > text
    '''
    try:
        return get_data_parameters(event, print_error)['text'].replace('\n','\\n')
    except KeyError:
        if print_error:
            print "Error: event",event['index']," has no 'data > parameters > text'"
            # traceback.print_exc()

def extract_new_datapoint(event, get_record_data_method):
    '''
    Grabs the data for the recorded datapoint. Where this data lives depends on if the log file is
    from before or after March 20th.
    Some datapoint's values are formated to match what the students sees (ie. how many decimal places)
    '''
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

def detect_drag_event(event_name):
    '''
    Detects the type of drag event
    '''
    drag_type = event_name.split('.')[-1]
    return drag_type

def detect_drag_item(event_name):
    '''
    Detects what item is being dragged.
    '''
    drag_item = event_name.split('.')[3]
    return drag_item

def get_drag_direction(event):
    '''
    Finds the drag direction given the difference between the old
    and new value of the item being dragged (when old and new value
    are available in the event's log)
    '''
    new,old = get_new_old_values(event)
    if new > old:
        return 'increasing'
    else:
        return 'decreasing'

def get_new_old_values(event):
    '''
    Detects the old and new value of the item being dragged when they
    are available in the event's log, otherwise no error is printed.
    '''
    values = get_data_children_parameters(event, print_error = False)
    return values['newValue'],values['oldValue']

def get_checkbox_status1(event, print_error = True):
    '''
    Detects the status of the checkbox that was clicked.
    This method is used when the log file is from BEFORE March 20th.
    '''
    try: 
        return get_data_parameters_args(event)[0]['parameters']['checked']
    except KeyError:
        if print_error:
            print "Error: event",event['index']," has no 'data > parameters > args > parameters > checked'"
            # traceback.print_exc()

def get_checkbox_status2(event, print_error = True):
    '''
    Detects the status of the checkbox that was clicked.
    This method is used when the log file is from AFTER March 20th.
    '''
    try: 
        return get_data_parameters(event)['checked']
    except KeyError:
        if print_error:
            print "Error: event",event['index']," has no 'data > parameters > args > parameters > checked'"
            # traceback.print_exc()

def is_checkbox_error1(event):
    '''
    Detects if clicking the checkbox outputted an error.
    This method is used when the log file is from BEFORE March 20th.
    '''
    try: 
        error = get_data_parameters_args(event)[0]['parameters']['error']
        if error == "Cannot add this data point to the plot.  Either the data is empty, you have not selected an axis feature, or the data point is not defined for the selected scale.":
            return True
    except KeyError:
        return False

def is_checkbox_error2(event):
    '''
    Detects if clicking the checkbox outputted an error.
    This method is used when the log file is from AFTER March 20th.
    '''
    try: 
        error = get_data_parameters(event)['error']
        if error == "Cannot add this data point to the plot.  Either the data is empty, you have not selected an axis feature, or the data point is not defined for the selected scale.":
            return True
    except KeyError:
        return False

def update_checkstatus_in_table(current_table, trial_added_or_removed, check_status):
    '''
    When a datapoint is added or removed from the graph, we update the "inGraph"
    status of that point. It's new status is check_status, and the dataoint's
    trial number is trial_added_or_removed
    '''
    new_table = current_table.copy()
    new_table[trial_added_or_removed]['inGraph'] = check_status
    return new_table

def remove_from_table(current_table, trial_removed):
    '''
    When a datapoint is added or removed from the table, we update our version 
    of the table. The dataoint's trial number is trial_removed
    '''
    new_table = current_table.copy()
    del new_table[trial_removed]
    return new_table 

#All of the event['event'] that relate to the sim initializing
EVENTS_INITIALIZING = ["beersLawLab.sim.simStarted",
                        "beersLawLab.sim.barrierRectangle.fired",
                        "beersLawLab.navigationBar.phetButton.fired",
                        "beersLawLab.navigationBar.titleTextNode.textChanged"]
#All of the event['data']['parameters']['method'] that relate to the sim initializing
INITIALIZING_METHODS = ["addExpressions","launchSimulation","setText"]

def mega_parser(studentid, header, events):
    '''
    This function parses the log file line by line in a 1 to 1 fashion.
    First the numy array is initialized.
    Then for each event, we tests a few if statements to try to parse the event.
    the output is saved as a tab delimited file.
    '''
    sim, first_time_stamp, dreamtable = initialize_dreamtable(studentid, header,len(events),events[0])
    table = {}
    for i,event in enumerate(events):
        parsed = False
        dreamtable[i+1,header.index("Time")] = round((event['timestamp']-first_time_stamp)/1000.0,2)
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
                        selection = get_data_parameters_args(event)[0]['parameters']['feature']
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
                        new_data_point = extract_new_datapoint(event, get_data_children_parameters)
                        table[new_data_point['trialNumber']] = new_data_point
                        dreamtable[i+1,header.index("Table")] = json.dumps(table)
                    elif "labBook.addToGraphCheckBox" in phetioID:
                        parsed = True
                        trial_added_or_removed_to_graph = int(re.search(r'\d+', phetioID).group())
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
                        dreamtable[i+1,header.index("Item")] = 'trialNumber ' + str(trial_added_or_removed_to_graph)
                        table = update_checkstatus_in_table(table, trial_added_or_removed_to_graph, checked)
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
            trial_added_or_removed_to_graph = int(re.search(r'\d+', event['event']).group())
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
            dreamtable[i+1,header.index("Item")] = 'trialNumber ' + str(trial_added_or_removed_to_graph)
            table = update_checkstatus_in_table(table, trial_added_or_removed_to_graph, checked)
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


#test sime with this link
# https://phet-io.colorado.edu/sims/beers-law-lab/1.6.3-phetio/wrappers/login/login.html?wrapper=lab-book&validationRule=validateDigits&numberOfDigits=8&sim=beers-law-lab&console&publisher_id=0c82b6bf&application_id=1d0612a8397e8b1dbf4993bc58869fa1&widget_id=lab-book-beers-law-lab&phetioEmitStates=true&phetioEmitInputEvents=false