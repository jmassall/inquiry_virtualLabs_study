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

LIGHT_HEADER = ["User","Sim","Time","Index","User or Model?","Event","Item","Action","Laser on status","Wavelength","Width","Concentration","Absorption","Detector location","Ruler location","Table","X axis","Y axis","X axis scale","Y axis scale","Experiment #s included","Notes"]
CHARGE_HEADER = ["User","Sim","Time","Index","User or Model?","Event","Item","Action",'Charge','Connection','Battery voltage','Separation','Area',"Table","X axis","Y axis","X axis scale","Y axis scale","Experiment #s included","Notes"]

def initialize_dreamtable(studentid, number_of_events,first_event):
    '''
    Creates a numpy array with as many columns as the length of the header of the table
    and as many rows as the number of events (+1 for header)
    It also uses the first event to find the sim. It then populates the sim and studentid column.
    It returns the sim, the first time stamp and the initialized table.
    '''
    if "beersLaw" in first_event["event"]:
        sim = 'light_absorbance'
        header = LIGHT_HEADER
    else:
        sim = 'capacitor_charge'
        header = CHARGE_HEADER
    dreamtable = np.chararray(shape=(number_of_events+1,len(header)), itemsize=100000)
    dreamtable[0,:] = header
    dreamtable[1:,header.index("User")] = studentid
    dreamtable[1:,header.index("Sim")] = sim
    start_time = first_event['timestamp']
    return sim, start_time, header, dreamtable

def get_data(event, show_error_in_console = True):
    '''
    Grabs the information under the first event key "data"
    '''
    try: 
        return event['data']
    except KeyError:
        if show_error_in_console:
            print "Error: event",event['index']," has no 'data'"
            # traceback.print_exc()

def get_data_parameters(event, show_error_in_console = True):
    '''
    Grabs the information under the event's data > parameters
    '''
    try: 
        return get_data(event, show_error_in_console)['parameters']
    except KeyError:
        if show_error_in_console:
            print "Error: event",event['index']," has no 'data > parameters'"
            # traceback.print_exc()

def get_messages(event, show_error_in_console = True):
    '''
    Grabs the information under the event's data > parameters > messages
    '''
    try: 
        return get_data_parameters(event, show_error_in_console)['messages']
    except KeyError:
        if show_error_in_console:
            print "Error: event",event['index']," has no 'data > parameters > messages'"
            # traceback.print_exc()

def get_method(event, show_error_in_console = True):
    '''
    Grabs the information under the event's data > parameters > method
    '''
    try: 
        return get_data_parameters(event, show_error_in_console)['method']
    except KeyError:
        if show_error_in_console:
            print "Error: event",event['index']," has no 'data > parameters > method'"
            # traceback.print_exc()

def get_state(event, show_error_in_console = True):
    '''
    Grabs the state information under the event's data > parameters > state
    '''
    try: 
        return get_data_parameters(event, show_error_in_console)['state']
    except KeyError:
        if show_error_in_console:
            print "Error: event",event['index']," has no 'data > parameters > state'"
            # traceback.print_exc()

def get_data_parameters_args(event, show_error_in_console = True):
    '''
    Grabs the information under the event's data > parameterers > args
    '''
    try: 
        return get_data_parameters(event, show_error_in_console)['args']
    except KeyError:
        if show_error_in_console:
            print "Error: event",event['index']," has no 'data > parameters > args'"
            # traceback.print_exc()

def get_data_parameters_args_parameters(event, show_error_in_console = True):
    '''
    Grabs the information under the event's data > parameterers > args
    '''
    try: 
        return get_data_parameters_args(event, show_error_in_console)[0]['parameters']
    except KeyError:
        if show_error_in_console:
            print "Error: event",event['index']," has no 'data > parameters > args > parameters'"
            # traceback.print_exc()

def get_args_phetioID(event, show_error_in_console = True):
    '''
    Grabs the information under the event's data > parameters > args > phetioID
    '''
    try: 
        return get_data_parameters_args(event, show_error_in_console)[0]['phetioID']
    except KeyError:
        if show_error_in_console:
            print "Error: event",event['index']," has no 'data > parameters > args > phetioID'"
            # traceback.print_exc()

def get_data_children(event, show_error_in_console = True):
    '''
    Grabs the information under the event's data > children
    '''
    try: 
        return get_data(event, show_error_in_console)['children']
    except KeyError:
        if show_error_in_console:
            print "Error: event",event['index']," has no 'data > children'"
            # traceback.print_exc()

def get_data_children_parameters(event, show_error_in_console = True):
    '''
    Grabs the information under the event's data > children > parameters
    '''
    try: 
        return get_data_children(event, show_error_in_console)[0]['parameters']
    except KeyError:
        if show_error_in_console:
            print "Error: event",event['index']," has no 'data > children > parameters'"
            # traceback.print_exc()

def get_notes(event, show_error_in_console = True):
    '''
    Grabs the notes under the event's data > parameters > text
    '''
    try:
        return get_data_parameters(event, show_error_in_console)['text'].replace('\n','\\n')
    except KeyError:
        if show_error_in_console:
            print "Error: event",event['index']," has no 'data > parameters > text'"
            # traceback.print_exc()

def extract_new_datapoint(sim, event, get_record_data_method):
    '''
    Grabs the data for the recorded datapoint. Where this data lives depends on if the log file is
    from before or after March 20th.
    Some datapoint's values are formated to match what the students sees (ie. how many decimal places)
    '''
    datapoint = {}
    if sim == 'light_absorbance':
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
        datapoint["visible"] = get_record_data_method(event)["visible"]
    elif sim == 'capacitor_charge':
        datapoint["Battery voltage"] = round(get_record_data_method(event)['state']["capacitorLabBasics.lightBulbScreen.model.circuit.battery.voltageProperty"],4)
        datapoint["Capacitor voltage"] = round(get_record_data_method(event)['state']["capacitorLabBasics.lightBulbScreen.model.circuit.switchedCapacitor.platesVoltageProperty"],4)
        datapoint["Connection"] = get_record_data_method(event)['state']["capacitorLabBasics.lightBulbScreen.model.circuit.circuitConnectionProperty"]
        datapoint["Separation"] = get_record_data_method(event)['state']["capacitorLabBasics.lightBulbScreen.model.circuit.switchedCapacitor.plateSeparationProperty"]*1000
        datapoint["Area"] = get_record_data_method(event)['state']["capacitorLabBasics.lightBulbScreen.model.circuit.switchedCapacitor.plateSizeProperty"]["maxX"]**2*1000000
        datapoint["Charge"] = round(get_record_data_method(event)['state']["capacitorLabBasics.lightBulbScreen.model.plateChargeMeter.valueProperty"]*1000000000000,2)
        datapoint["trialNumber"] = get_record_data_method(event)["trialNumber"]
        datapoint["visible"] = get_record_data_method(event)["visible"]
    return datapoint

def detect_drag_event(event_name):
    '''
    Detects the type of drag event
    '''
    drag_type = event_name.split('.')[-1]
    return drag_type

def detect_drag_item(sim,event_name):
    '''
    Detects what item is being dragged.
    '''
    if sim == 'light_absorbance':
        drag_item = event_name.split('.')[3]
    elif sim == 'capacitor_charge':
        drag_item = event_name.split('.')[4]
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
    values = get_data_children_parameters(event, show_error_in_console = False)
    return values['newValue'],values['oldValue']

def get_checkbox_status1(event, show_error_in_console = True):
    '''
    Detects the status of the checkbox that was clicked.
    This method is used when the log file is from BEFORE March 20th.
    '''
    try: 
        return get_data_parameters_args(event)[0]['parameters']['checked']
    except KeyError:
        if show_error_in_console:
            print "Error: event",event['index']," has no 'data > parameters > args > parameters > checked'"
            # traceback.print_exc()

def get_checkbox_status2(event, show_error_in_console = True):
    '''
    Detects the status of the checkbox that was clicked.
    This method is used when the log file is from AFTER March 20th.
    '''
    try: 
        return get_data_parameters(event)['checked']
    except KeyError:
        if show_error_in_console:
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
    When a datapoint is added or removed from the graph, we update the "visible"
    status of that point. It's new status is check_status, and the dataoint's
    trial number is trial_added_or_removed
    '''
    new_table = current_table.copy()
    new_table[trial_added_or_removed]['visible'] = check_status
    return new_table

def remove_from_table(current_table, trial_removed):
    '''
    When a datapoint is added or removed from the table, we update our version 
    of the table. The dataoint's trial number is trial_removed
    '''
    new_table = current_table.copy()
    del new_table[trial_removed]
    return new_table 

def update_state(sim,event):
    simstate = {}
    if sim == 'light_absorbance':
        simstate["Width"] = round(get_state(event)["beersLawLab.beersLawScreen.model.cuvette.widthProperty"],2)
        simstate["Detector location"] = get_state(event)["beersLawLab.beersLawScreen.model.detector.probe.locationProperty"]
        absorption = get_state(event)["beersLawLab.beersLawScreen.model.detector.valueProperty"]
        if absorption != None:
            simstate["Absorption"] = round(absorption,2)
        simstate["Laser on status"] = get_state(event)["beersLawLab.beersLawScreen.model.light.onProperty"]
        simstate["Wavelength"] = get_state(event)["beersLawLab.beersLawScreen.model.light.wavelengthProperty"]
        simstate["Ruler location"] = get_state(event)["beersLawLab.beersLawScreen.model.ruler.locationProperty"]
        simstate["Concentration"] = round(get_state(event)["beersLawLab.beersLawScreen.solutions.copperSulfate.concentrationProperty"],2)
    elif sim == 'capacitor_charge':
        simstate["Battery voltage"] = round(get_state(event)["capacitorLabBasics.lightBulbScreen.model.circuit.battery.voltageProperty"],4)
        simstate["Connection"] = get_state(event)["capacitorLabBasics.lightBulbScreen.model.circuit.circuitConnectionProperty"]
        simstate["Separation"] = get_state(event)["capacitorLabBasics.lightBulbScreen.model.circuit.switchedCapacitor.plateSeparationProperty"]*1000
        simstate["Area"] = get_state(event)["capacitorLabBasics.lightBulbScreen.model.circuit.switchedCapacitor.plateSizeProperty"]["maxX"]**2*1000000
        simstate["Charge"] = round(get_state(event)["capacitorLabBasics.lightBulbScreen.model.plateChargeMeter.valueProperty"]*1000000000000,2)
    return simstate

#All of the event['event'] that relate to the sim initializing
EVENTS_INITIALIZING = ["beersLawLab.sim.simStarted",
                        "capacitorLabBasics.sim.simStarted",
                        "beersLawLab.sim.barrierRectangle.fired",
                        "capacitorLabBasics.sim.barrierRectangle.fired",
                        "beersLawLab.navigationBar.phetButton.fired",
                        "capacitorLabBasics.navigationBar.phetButton.fired",
                        "beersLawLab.navigationBar.titleTextNode.textChanged",
                        ]
#All of the event['data']['parameters']['method'] that relate to the sim initializing
INITIALIZING_METHODS = ["addExpressions","launchSimulation","setText"]

def parse_event(sim, event, simstate, table, graphstate, notes):
    parsed = False

    if "simIFrameAPI.invoked" in event['event']:
        if 'messages' in get_data_parameters(event).keys():
            parsed = True
            user_or_model = 'model'
            simevent = 'gettingValues'
            item = 'sim'
            action = ''
        else:
            method = get_method(event)
            if method in INITIALIZING_METHODS:
                parsed = True
                user_or_model = 'model'
                simevent = 'initializing'
                item = 'sim'
                action = method
            elif method == 'setState': #this happens when sim is restored from trial
                parsed = True
                user_or_model = 'model'
                simevent = 'setting sim state'
                item = 'sim'
                action = ''
            else:
                #the following are for log files after March 20th
                phetioID = get_args_phetioID(event)
                if phetioID == "labBook.tableExpandButton":
                    parsed = True
                    user_or_model = 'user'
                    simevent = 'expanding table'
                    item = 'table'
                    action = ''
                elif phetioID == "labBook.tableCollapseButton":
                    parsed = True
                    user_or_model = 'user'
                    simevent = 'collapsing table'
                    item = 'table'
                    action = ''
                elif phetioID == "labBook.graphExpandButton":
                    parsed = True
                    user_or_model = 'user'
                    simevent = 'expanding graph'
                    item = 'graph'
                    action = ''
                elif phetioID == "labBook.graphCollapseButton":
                    parsed = True
                    user_or_model = 'user'
                    simevent = 'collapsing graph'
                    item = 'graph'
                    action = ''
                elif phetioID == "labBook.simulationExpandButton":
                    parsed = True
                    user_or_model = 'user'
                    simevent = 'expanding simulation'
                    item = 'simulation'
                    action = ''
                elif phetioID == "labBook.simulationCollapseButton":
                    parsed = True
                    user_or_model = 'user'
                    simevent = 'collapsing simulation'
                    item = 'simulation'
                    action = ''
                elif "Feature" in phetioID:
                    parsed = True
                    selection = get_data_parameters_args(event)[0]['parameters']['feature']
                    variable_selected, axis = selection.split('_')
                    axis = axis.capitalize()
                    user_or_model = 'user'
                    simevent = 'Selecting '+axis+'-axis'
                    item = axis+'-axis dropdown menu'
                    action = axis+'-axis changed to '+ variable_selected
                    graphstate[axis+" axis"] = variable_selected
                elif "Transform" in phetioID:
                    parsed = True
                    axis = re.search(r'\.([xy])Transform', phetioID).group(1).capitalize()
                    scale = get_data_parameters_args_parameters(event)['feature']
                    user_or_model = 'user'
                    simevent = 'Selecting scale of '+axis+'-axis'
                    item = axis+'-axis scale dropdown menu'
                    action = axis+'-axis scale changed to '+ scale
                    graphstate[axis+" axis scale"] = scale
                elif phetioID == "labBook.recordDataButton": #for log data after March 20th 2017
                    parsed = True
                    user_or_model = 'user'
                    simevent = 'recording data'
                    item = ''
                    action = ''
                    new_data_point = extract_new_datapoint(sim, event, get_data_parameters_args_parameters)
                    table[new_data_point['trialNumber']] = new_data_point
                elif "labBook.addToGraphCheckBox" in phetioID:
                    parsed = True
                    trial_added_or_removed_to_graph = int(re.search(r'\d+', phetioID).group())
                    checked = get_checkbox_status1(event)
                    if is_checkbox_error1(event):
                        simevent = 'Adding data to graph'
                        action = 'Error: failed to add trial.'
                        checked = False
                    elif checked:
                        simevent = 'Adding data to graph'
                        action = 'Data added to graph successfully.'
                    else:
                        simevent = 'Removing data from graph'
                        action = 'Data removed from graph.'
                    user_or_model = 'user'
                    item = 'trialNumber ' + str(trial_added_or_removed_to_graph)
                    table = update_checkstatus_in_table(table.copy(), trial_added_or_removed_to_graph, checked)
                elif "labBook.deleteButton" in phetioID:
                    parsed = True
                    trial_removed_from_table = int(re.search(r'\d+', phetioID).group())
                    user_or_model = 'user'
                    simevent = 'Removing data from table'
                    item = 'trialNumber ' + str(trial_removed_from_table)
                    action = 'Data removed from from table'
                    table = remove_from_table(table.copy(), trial_removed_from_table)
                elif "labBook.restoreButton" in phetioID:
                    parsed = True
                    trial_restored = int(re.search(r'\d+', phetioID).group())
                    user_or_model = 'user'
                    simevent = 'Restoring sim state'
                    item = 'trialNumber ' + str(trial_restored)
                    action = ''
                elif "labBook.incrementButton" in phetioID:
                    parsed = True
                    trial_moved_down = int(re.search(r'\d+', phetioID).group())
                    user_or_model = 'user'
                    simevent = 'Moving trial in table'
                    item = 'trialNumber ' + str(trial_moved_down)
                    action = 'Moved trial down'
                elif "labBook.decrementButton" in phetioID:
                    parsed = True
                    trial_moved_down = int(re.search(r'\d+', phetioID).group())
                    user_or_model = 'user'
                    simevent = 'Moving trial in table'
                    item = 'trialNumber ' + str(trial_moved_down)
                    action = 'Moved trial up'

    #the following are for log files after March 20th
    elif event['event'] == "labBook.recordDataButton.pressed":
        parsed = True
        user_or_model = 'user'
        simevent = 'recording data'
        item = ''
        action = ''
        new_data_point = extract_new_datapoint(sim, event, get_data_parameters)
        table[new_data_point['trialNumber']] = new_data_point
    elif event['event'] == "labBook.tableExpandButton.pressed":
        parsed = True
        user_or_model = 'user'
        simevent = 'expanding table'
        item = 'table'
        action = ''
    elif event['event'] == "labBook.tableCollapseButton.pressed":
        parsed = True
        user_or_model = 'user'
        simevent = 'collapsing table'
        item = 'table'
        action = ''
    elif event['event'] == "labBook.graphExpandButton.pressed":
        parsed = True
        user_or_model = 'user'
        simevent = 'expanding graph'
        item = 'graph'
        action = ''
    elif event['event'] == "labBook.graphCollapseButton.pressed":
        parsed = True
        user_or_model = 'user'
        simevent = 'collapsing graph'
        item = 'graph'
        action = ''
    elif event['event'] == "labBook.simulationExpandButton.pressed":
        parsed = True
        user_or_model = 'user'
        simevent = 'expanding simulation'
        item = 'simulation'
        action = ''
    elif event['event'] == "labBook.simulationCollapseButton.pressed":
        parsed = True
        user_or_model = 'user'
        simevent = 'collapsing simulation'
        item = 'simulation'
        action = ''
    elif "Feature" in event['event']:
        parsed = True
        selection = get_data_parameters(event)['feature']
        variable_selected, axis = selection.split('_')
        axis = axis.capitalize()
        user_or_model = 'user'
        simevent = 'Selecting '+axis+'-axis'
        item = axis+'-axis dropdown menu'
        action = axis+'-axis changed to '+ variable_selected
        graphstate[axis+" axis"] = variable_selected
    elif "Transform" in event['event']:
        parsed = True
        axis = re.search(r'\.([xy])Transform', event['event']).group(1).capitalize()
        scale = get_data_parameters(event)['feature']
        user_or_model = 'user'
        simevent = 'Selecting scale of '+axis+'-axis'
        item = axis+'-axis scale dropdown menu'
        action = axis+'-axis scale changed to '+ scale
        graphstate[axis+" axis scale"] = scale
    elif "labBook.addToGraphCheckBox" in event['event']:
        parsed = True
        trial_added_or_removed_to_graph = int(re.search(r'\d+', event['event']).group())
        checked = get_checkbox_status2(event)
        if is_checkbox_error2(event):
            simevent = 'Adding data to graph'
            action = 'Error: failed to add trial.'
            checked = False
        elif checked:
            simevent = 'Adding data to graph'
            action = 'Data added to graph successfully.'
        else:
            simevent = 'Removing data from graph'
            action = 'Data removed from graph.'
        user_or_model = 'user'
        item = 'trialNumber ' + str(trial_added_or_removed_to_graph)
        table = update_checkstatus_in_table(table.copy(), trial_added_or_removed_to_graph, checked)
    elif "labBook.deleteButton" in event['event']:
        parsed = True
        trial_removed_from_table = int(re.search(r'\d+', event['event']).group())
        user_or_model = 'user'
        simevent = 'Removing data from table'
        item = 'trialNumber ' + str(trial_removed_from_table)
        action = 'Data removed from from table'
        table = remove_from_table(table.copy(), trial_removed_from_table)


    elif event['event'] == "capacitorLabBasics.lightBulbScreen.model.circuit.circuitConnectionProperty.changed":
        parsed = True
        user_or_model = 'user'
        simevent = 'changed connection'
        item = "switch"
        action = "Changed connection to "+ get_data_parameters(event)['newValue'].split('_')[0]
    elif "concentrationControl.slider.plusButton" in event['event']:
        parsed = True
        user_or_model = 'user'
        simevent = 'Changed concentration'
        item = "concentration slider"
        action = 'Pressed increment button'
    elif "concentrationControl.slider.minusButton" in event['event']:
        parsed = True
        user_or_model = 'user'
        simevent = 'Changed concentration'
        item = "concentration slider"
        action = 'Pressed decrement button'
    elif event['event'] in EVENTS_INITIALIZING:
        parsed = True
        user_or_model = 'model'
        simevent = 'initializing'
        item = 'sim'
        action = event['event']
    elif event['event'] == "phetio.state":
        parsed = True
        user_or_model = 'model'
        simevent = 'updating state'
        item = ''
        action = ''
        simstate = update_state(sim,event)
    elif "drag" in event['event']:
        parsed = True
        drag_event = detect_drag_event(event['event'])
        drag_item = detect_drag_item(sim,event['event'])
        user_or_model = 'user'
        simevent = drag_event
        item = drag_item
        action = ''
        if drag_event == 'dragged':
            try:
                direction = get_drag_direction(event)
                action = direction
            except:
                pass
    elif event['event'] == "beersLawLab.beersLawScreen.view.lightNode.button.toggled":
        parsed = True
        user_or_model = 'user'
        simevent = 'toggle laser'
        item = 'laser button'
        action = ''
    elif event['event'] == "labBook.textArea.changed":
        parsed = True
        user_or_model = 'user'
        simevent = 'editing notes'
        item = 'notepad'
        action = ''
        notes = get_notes(event)
    
    if not parsed:
        #Didn't detect any kind of event
        print "Error: new event type encountered."
        print '\t'+event['event'], event['index']
        sys.exit()

    # print event['index'],parsed, user_or_model, simevent, item, action

    return parsed, user_or_model, simevent, item, action, simstate, table, graphstate, notes

def mega_parser(studentid, events):
    '''
    This function parses the log file line by line in a 1 to 1 fashion.
    First the numy array is initialized.
    Then for each event, we tests a few if statements to try to parse the event.
    the output is saved as a tab delimited file.
    '''
    sim, first_time_stamp, header, dreamtable = initialize_dreamtable(studentid, len(events),events[0])

    eventypes = []
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
        parsed, user_or_model, simevent, item, action, simstate, NEWdatatable, graphstate, notes = parse_event(sim,event, simstate.copy(), datatable.copy(), graphstate.copy(), notes)

        if parsed: #if we managed to parse, we update the dreamtable
            dreamtable[row,header.index("Time")] = round((event['timestamp']-first_time_stamp)/1000.0,2)
            dreamtable[row,header.index("Index")] = event['index']
            dreamtable[row,header.index("User or Model?")] = user_or_model
            dreamtable[row,header.index("Event")] = simevent
            dreamtable[row,header.index("Item")] = item
            dreamtable[row,header.index("Action")] = action

            for variable in simstate:
                dreamtable[row,header.index(variable)] = simstate[variable]

            if NEWdatatable != datatable:
                dreamtable[row,header.index("Table")] = json.dumps(NEWdatatable)
                datatable = NEWdatatable.copy()

            for variable in graphstate:
                dreamtable[row,header.index(variable)] = graphstate[variable]

            dreamtable[row,header.index("Notes")] = notes

    return sim, dreamtable

if __name__ == '__main__':
    # test_json = 'example_cleaned_student_11111111_data_file.json'
    # test_json = 'pretty_print_copy_log_lab-book-beers-law-lab_90447168_2017-01-17_11.22.45.json'
    # test_json = 'pretty_print_copy_log_lab-book-beers-law-lab_83459165_2017-01-13_14.26.08.json'
    # test_json = 'pretty_print_copy_log_lab-book-capacitor-lab-basics_10708152_2017-03-20_15.32.50.json'
    test_json = 'pretty_print_copy_log_lab-book-capacitor-lab-basics_12816168_2017-03-21_17.28.40.json'
    
    studentid = re.search(r'_(\d{7,8})_', test_json).group(1)
    session = Session()
    session.get_session_data_from_file(test_json)
    print studentid
    sim, dreamtable = mega_parser(studentid, session.events)
    np.savetxt('dream_table_{0}_{1}.txt'.format(studentid,sim), dreamtable, delimiter='\t', fmt='%s')

#test sim with this link
# https://phet-io.colorado.edu/sims/beers-law-lab/1.6.3-phetio/wrappers/login/login.html?wrapper=lab-book&validationRule=validateDigits&numberOfDigits=8&sim=beers-law-lab&console&publisher_id=0c82b6bf&application_id=1d0612a8397e8b1dbf4993bc58869fa1&widget_id=lab-book-beers-law-lab&phetioEmitStates=true&phetioEmitInputEvents=false
# https://phet-io.colorado.edu/sims/capacitor-lab-basics/1.4.2-phetio/wrappers/login/login.html?wrapper=lab-book&validationRule=validateDigits&numberOfDigits=8&sim=capacitor-lab-basics&console&publisher_id=0c82b6bf&application_id=1d0612a8397e8b1dbf4993bc58869fa1&widget_id=lab-book-capacitor-lab-basics&phet-io.emitStates


# TODO
#     make test function per event to see if parsed correctly.
#     finish parsing capacitors.