'''
author: sperez8
data: june 14 2017

This script cleans raw log files and splits them into individual session files stored in the log data folder
'''
import unittest
from utils import convert_unix_time,Session
from mega_parser import *
import test_log_samples as logsample
from test_log_events import *

class TestUtils(unittest.TestCase):
    """
    Basic test class for all file cleaning and splitting functions
    """
    def test_convert_unix_time(self):
        """
        Tests conversion of time.
        """
        x = '1490049160615'
        self.assertEqual(convert_unix_time(x),'2017-03-20_15.32.40')


class TestParsingFunctions(unittest.TestCase):
    """
    Basic test class for all parsing functions
    """
    def test_get_data(self):
        '''
        Tests the function get_data() on different events.
        '''
        self.assertEqual(get_data(logsample.state_event), logsample.state_event_DATA)
        self.assertEqual(get_data(logsample.getting_values_event), logsample.getting_values_event_DATA)

    def test_get_data_parameters(self):
        '''
        Tests the function get_data_parameters() on different events.
        '''
        self.assertEqual(get_data_parameters(logsample.state_event), logsample.state_event_DATA_PARAMETERS)
        self.assertEqual(get_data_parameters(logsample.getting_values_event), logsample.getting_values_event_DATA_PARAMETERS)

    def test_get_drag_direction(self):
        '''
        Tests the function get_data_chidlren_parameters() on different events.
        '''
        self.assertEqual(get_drag_direction(logsample.drag_event), logsample.drag_event_DIRECTION)

    def test_get_data_parameters_args(self):
        '''
        Tests the function get_data_parameters_args() on different events.
        '''
        # self.assertEqual(get_data_parameters_args(logsample.state_event), logsample.state_event_DATA_PARAMETERS_ARGS)

    def test_get_data_parameters_args_parameters(self):
        '''
        Tests the function get_data_parameters_args_parameters() on different events.
        '''
        self.assertEqual(get_data_parameters_args_parameters(logsample.record_event), logsample.record_event_DATA_PARAMETERS_ARGS_PARAMETERS)
        self.assertEqual(get_data_parameters_args_parameters(logsample.axis_event), logsample.axis_event_DATA_PARAMETERS_ARGS_PARAMETERS)

    def test_get_args_phetioID(self): #for events from log after March 20th
        '''
        Tests the function get_args_phetioID() on diffferent events.
        '''
        self.assertEqual(get_args_phetioID(logsample.record_event), logsample.record_event_PHETIOID)
        self.assertEqual(get_args_phetioID(logsample.axis_event), logsample.axis_event_PHETIOID)
        self.assertEqual(get_args_phetioID(logsample.table_collapse_event), logsample.table_collapse_event_PHETIOID)
        self.assertEqual(get_args_phetioID(logsample.delete_table_event), logsample.delete_table_event_PHETIOID)
        self.assertEqual(get_args_phetioID(logsample.graph_checkbox_event), logsample.graph_checkbox_event_PHETIOID)

    def test_get_state(self):
        '''
        Tests the function get_state() on different state events.
        '''
        self.assertEqual(get_state(logsample.state_event), logsample.state_event_STATE)

    def test_get_method(self):
        '''
        Tests the function get_method() on different events.
        '''
        self.assertEqual(get_method(logsample.initializing_event1), logsample.initializing_event1_METHOD)
        self.assertEqual(get_method(logsample.initializing_event2), logsample.initializing_event2_METHOD)
        self.assertEqual(get_method(logsample.initializing_event3), logsample.initializing_event3_METHOD)

    def test_get_notes(self):
        '''
        Tests the function get_notes()
        '''
        self.assertEqual(get_notes(logsample.notes_event), logsample.notes_event_NOTES)





class TestEventParsing(unittest.TestCase):
    """
    Basic test class for all event parsing
    """

    simstate_BEERS = {'Charge': '', 'Connection': '', 'Battery voltage': '', 'Separation': '', 'Area': ''}
    simstate_CAPS = {"Laser on status":'',"Wavelength":'',"Width":'',"Concentration":'',"Absorption":'',"Detector location":'',"Ruler location":''}
    graphstate = {"X axis":'',"Y axis":'',"X axis scale":'',"Y axis scale":'',"Experiment #s included":''}
    
    def test_parsing_initializing_event(self):
        parsed, user_or_model, simevent, item, action, simstate, datatable, graphstate, notes = parse_event("beers-law-lab",initializing_event,self.__class__.simstate_BEERS, {}, self.__class__.graphstate, '')
        self.assertEqual(initializing_event_parsed,parsed)
        self.assertEqual(initializing_event_user_or_model,user_or_model)
        self.assertEqual(initializing_event_simevent,simevent)
        self.assertEqual(initializing_event_item,item)
        self.assertEqual(initializing_event_action,action)
    
    def test_parsing_Moving_trial_in_table_event_CAPS(self):
        parsed, user_or_model, simevent, item, action, simstate, datatable, graphstate, notes = parse_event("capacitor-lab-basics",initializing_event,self.__class__.simstate_CAPS, {}, self.__class__.graphstate, '')
        self.assertEqual(initializing_event_parsed,parsed)
        self.assertEqual(initializing_event_user_or_model,user_or_model)
        self.assertEqual(initializing_event_simevent,simevent)
        self.assertEqual(initializing_event_item,item)
        self.assertEqual(initializing_event_action,action)



    def test_parsing_updating_state_event_BEERS(self):
        parsed, user_or_model, simevent, item, action, simstate, datatable, graphstate, notes = parse_event("beers-law-lab",updating_state_event,self.__class__.simstate_BEERS, {}, self.__class__.graphstate, '')
        self.assertEqual(updating_state_event_parsed,parsed)
        self.assertEqual(updating_state_event_user_or_model,user_or_model)
        self.assertEqual(updating_state_event_simevent,simevent)
        self.assertEqual(updating_state_event_item,item)
        self.assertEqual(updating_state_event_action,action)
    
    def test_parsing_Moving_trial_in_table_event_CAPS(self):
        parsed, user_or_model, simevent, item, action, simstate, datatable, graphstate, notes = parse_event("capacitor-lab-basics",updating_state_event,self.__class__.simstate_CAPS, {}, self.__class__.graphstate, '')
        self.assertEqual(updating_state_event_parsed,parsed)
        self.assertEqual(updating_state_event_user_or_model,user_or_model)
        self.assertEqual(updating_state_event_simevent,simevent)
        self.assertEqual(updating_state_event_item,item)
        self.assertEqual(updating_state_event_action,action)



    def test_parsing_toggle_laser_event_BEERS(self):
        parsed, user_or_model, simevent, item, action, simstate, datatable, graphstate, notes = parse_event("beers-law-lab",toggle_laser_event,self.__class__.simstate_BEERS, {}, self.__class__.graphstate, '')
        self.assertEqual(toggle_laser_event_parsed,parsed)
        self.assertEqual(toggle_laser_event_user_or_model,user_or_model)
        self.assertEqual(toggle_laser_event_simevent,simevent)
        self.assertEqual(toggle_laser_event_item,item)
        self.assertEqual(toggle_laser_event_action,action)
    
    def test_parsing_Moving_trial_in_table_event_CAPS(self):
        parsed, user_or_model, simevent, item, action, simstate, datatable, graphstate, notes = parse_event("capacitor-lab-basics",toggle_laser_event,self.__class__.simstate_CAPS, {}, self.__class__.graphstate, '')
        self.assertEqual(toggle_laser_event_parsed,parsed)
        self.assertEqual(toggle_laser_event_user_or_model,user_or_model)
        self.assertEqual(toggle_laser_event_simevent,simevent)
        self.assertEqual(toggle_laser_event_item,item)
        self.assertEqual(toggle_laser_event_action,action)



    def test_parsing_dragStarted_event_BEERS(self):
        parsed, user_or_model, simevent, item, action, simstate, datatable, graphstate, notes = parse_event("beers-law-lab",dragStarted_event,self.__class__.simstate_BEERS, {}, self.__class__.graphstate, '')
        self.assertEqual(dragStarted_event_parsed,parsed)
        self.assertEqual(dragStarted_event_user_or_model,user_or_model)
        self.assertEqual(dragStarted_event_simevent,simevent)
        self.assertEqual(dragStarted_event_item,item)
        self.assertEqual(dragStarted_event_action,action)
    
    def test_parsing_Moving_trial_in_table_event_CAPS(self):
        parsed, user_or_model, simevent, item, action, simstate, datatable, graphstate, notes = parse_event("capacitor-lab-basics",dragStarted_event,self.__class__.simstate_CAPS, {}, self.__class__.graphstate, '')
        self.assertEqual(dragStarted_event_parsed,parsed)
        self.assertEqual(dragStarted_event_user_or_model,user_or_model)
        self.assertEqual(dragStarted_event_simevent,simevent)
        self.assertEqual(dragStarted_event_item,item)
        self.assertEqual(dragStarted_event_action,action)



    def test_parsing_dragged_event_BEERS(self):
        parsed, user_or_model, simevent, item, action, simstate, datatable, graphstate, notes = parse_event("beers-law-lab",dragged_event,self.__class__.simstate_BEERS, {}, self.__class__.graphstate, '')
        self.assertEqual(dragged_event_parsed,parsed)
        self.assertEqual(dragged_event_user_or_model,user_or_model)
        self.assertEqual(dragged_event_simevent,simevent)
        self.assertEqual(dragged_event_item,item)
        self.assertEqual(dragged_event_action,action)
    
    def test_parsing_Moving_trial_in_table_event_CAPS(self):
        parsed, user_or_model, simevent, item, action, simstate, datatable, graphstate, notes = parse_event("capacitor-lab-basics",dragged_event,self.__class__.simstate_CAPS, {}, self.__class__.graphstate, '')
        self.assertEqual(dragged_event_parsed,parsed)
        self.assertEqual(dragged_event_user_or_model,user_or_model)
        self.assertEqual(dragged_event_simevent,simevent)
        self.assertEqual(dragged_event_item,item)
        self.assertEqual(dragged_event_action,action)



    def test_parsing_dragEnded_event_BEERS(self):
        parsed, user_or_model, simevent, item, action, simstate, datatable, graphstate, notes = parse_event("beers-law-lab",dragEnded_event,self.__class__.simstate_BEERS, {}, self.__class__.graphstate, '')
        self.assertEqual(dragEnded_event_parsed,parsed)
        self.assertEqual(dragEnded_event_user_or_model,user_or_model)
        self.assertEqual(dragEnded_event_simevent,simevent)
        self.assertEqual(dragEnded_event_item,item)
        self.assertEqual(dragEnded_event_action,action)
    
    def test_parsing_Moving_trial_in_table_event_CAPS(self):
        parsed, user_or_model, simevent, item, action, simstate, datatable, graphstate, notes = parse_event("capacitor-lab-basics",dragEnded_event,self.__class__.simstate_CAPS, {}, self.__class__.graphstate, '')
        self.assertEqual(dragEnded_event_parsed,parsed)
        self.assertEqual(dragEnded_event_user_or_model,user_or_model)
        self.assertEqual(dragEnded_event_simevent,simevent)
        self.assertEqual(dragEnded_event_item,item)
        self.assertEqual(dragEnded_event_action,action)



    def test_parsing_expanding_table_event_BEERS(self):
        parsed, user_or_model, simevent, item, action, simstate, datatable, graphstate, notes = parse_event("beers-law-lab",expanding_table_event,self.__class__.simstate_BEERS, {}, self.__class__.graphstate, '')
        self.assertEqual(expanding_table_event_parsed,parsed)
        self.assertEqual(expanding_table_event_user_or_model,user_or_model)
        self.assertEqual(expanding_table_event_simevent,simevent)
        self.assertEqual(expanding_table_event_item,item)
        self.assertEqual(expanding_table_event_action,action)
    
    def test_parsing_Moving_trial_in_table_event_CAPS(self):
        parsed, user_or_model, simevent, item, action, simstate, datatable, graphstate, notes = parse_event("capacitor-lab-basics",expanding_table_event,self.__class__.simstate_CAPS, {}, self.__class__.graphstate, '')
        self.assertEqual(expanding_table_event_parsed,parsed)
        self.assertEqual(expanding_table_event_user_or_model,user_or_model)
        self.assertEqual(expanding_table_event_simevent,simevent)
        self.assertEqual(expanding_table_event_item,item)
        self.assertEqual(expanding_table_event_action,action)



    def test_parsing_Changed_concentration_event_BEERS(self):
        parsed, user_or_model, simevent, item, action, simstate, datatable, graphstate, notes = parse_event("beers-law-lab",Changed_concentration_event,self.__class__.simstate_BEERS, {}, self.__class__.graphstate, '')
        self.assertEqual(Changed_concentration_event_parsed,parsed)
        self.assertEqual(Changed_concentration_event_user_or_model,user_or_model)
        self.assertEqual(Changed_concentration_event_simevent,simevent)
        self.assertEqual(Changed_concentration_event_item,item)
        self.assertEqual(Changed_concentration_event_action,action)
    
    def test_parsing_Moving_trial_in_table_event_CAPS(self):
        parsed, user_or_model, simevent, item, action, simstate, datatable, graphstate, notes = parse_event("capacitor-lab-basics",Changed_concentration_event,self.__class__.simstate_CAPS, {}, self.__class__.graphstate, '')
        self.assertEqual(Changed_concentration_event_parsed,parsed)
        self.assertEqual(Changed_concentration_event_user_or_model,user_or_model)
        self.assertEqual(Changed_concentration_event_simevent,simevent)
        self.assertEqual(Changed_concentration_event_item,item)
        self.assertEqual(Changed_concentration_event_action,action)



    def test_parsing_gettingValues_event_BEERS(self):
        parsed, user_or_model, simevent, item, action, simstate, datatable, graphstate, notes = parse_event("beers-law-lab",gettingValues_event,self.__class__.simstate_BEERS, {}, self.__class__.graphstate, '')
        self.assertEqual(gettingValues_event_parsed,parsed)
        self.assertEqual(gettingValues_event_user_or_model,user_or_model)
        self.assertEqual(gettingValues_event_simevent,simevent)
        self.assertEqual(gettingValues_event_item,item)
        self.assertEqual(gettingValues_event_action,action)
    
    def test_parsing_Moving_trial_in_table_event_CAPS(self):
        parsed, user_or_model, simevent, item, action, simstate, datatable, graphstate, notes = parse_event("capacitor-lab-basics",gettingValues_event,self.__class__.simstate_CAPS, {}, self.__class__.graphstate, '')
        self.assertEqual(gettingValues_event_parsed,parsed)
        self.assertEqual(gettingValues_event_user_or_model,user_or_model)
        self.assertEqual(gettingValues_event_simevent,simevent)
        self.assertEqual(gettingValues_event_item,item)
        self.assertEqual(gettingValues_event_action,action)



    def test_parsing_recording_data_event_BEERS(self):
        parsed, user_or_model, simevent, item, action, simstate, datatable, graphstate, notes = parse_event("beers-law-lab",recording_data_event,self.__class__.simstate_BEERS, {}, self.__class__.graphstate, '')
        self.assertEqual(recording_data_event_parsed,parsed)
        self.assertEqual(recording_data_event_user_or_model,user_or_model)
        self.assertEqual(recording_data_event_simevent,simevent)
        self.assertEqual(recording_data_event_item,item)
        self.assertEqual(recording_data_event_action,action)
    
    def test_parsing_Moving_trial_in_table_event_CAPS(self):
        parsed, user_or_model, simevent, item, action, simstate, datatable, graphstate, notes = parse_event("capacitor-lab-basics",recording_data_event,self.__class__.simstate_CAPS, {}, self.__class__.graphstate, '')
        self.assertEqual(recording_data_event_parsed,parsed)
        self.assertEqual(recording_data_event_user_or_model,user_or_model)
        self.assertEqual(recording_data_event_simevent,simevent)
        self.assertEqual(recording_data_event_item,item)
        self.assertEqual(recording_data_event_action,action)



    def test_parsing_expanding_graph_event_BEERS(self):
        parsed, user_or_model, simevent, item, action, simstate, datatable, graphstate, notes = parse_event("beers-law-lab",expanding_graph_event,self.__class__.simstate_BEERS, {}, self.__class__.graphstate, '')
        self.assertEqual(expanding_graph_event_parsed,parsed)
        self.assertEqual(expanding_graph_event_user_or_model,user_or_model)
        self.assertEqual(expanding_graph_event_simevent,simevent)
        self.assertEqual(expanding_graph_event_item,item)
        self.assertEqual(expanding_graph_event_action,action)
    
    def test_parsing_Moving_trial_in_table_event_CAPS(self):
        parsed, user_or_model, simevent, item, action, simstate, datatable, graphstate, notes = parse_event("capacitor-lab-basics",expanding_graph_event,self.__class__.simstate_CAPS, {}, self.__class__.graphstate, '')
        self.assertEqual(expanding_graph_event_parsed,parsed)
        self.assertEqual(expanding_graph_event_user_or_model,user_or_model)
        self.assertEqual(expanding_graph_event_simevent,simevent)
        self.assertEqual(expanding_graph_event_item,item)
        self.assertEqual(expanding_graph_event_action,action)



    def test_parsing_collapsing_graph_event_BEERS(self):
        parsed, user_or_model, simevent, item, action, simstate, datatable, graphstate, notes = parse_event("beers-law-lab",collapsing_graph_event,self.__class__.simstate_BEERS, {}, self.__class__.graphstate, '')
        self.assertEqual(collapsing_graph_event_parsed,parsed)
        self.assertEqual(collapsing_graph_event_user_or_model,user_or_model)
        self.assertEqual(collapsing_graph_event_simevent,simevent)
        self.assertEqual(collapsing_graph_event_item,item)
        self.assertEqual(collapsing_graph_event_action,action)
    
    def test_parsing_Moving_trial_in_table_event_CAPS(self):
        parsed, user_or_model, simevent, item, action, simstate, datatable, graphstate, notes = parse_event("capacitor-lab-basics",collapsing_graph_event,self.__class__.simstate_CAPS, {}, self.__class__.graphstate, '')
        self.assertEqual(collapsing_graph_event_parsed,parsed)
        self.assertEqual(collapsing_graph_event_user_or_model,user_or_model)
        self.assertEqual(collapsing_graph_event_simevent,simevent)
        self.assertEqual(collapsing_graph_event_item,item)
        self.assertEqual(collapsing_graph_event_action,action)



    def test_parsing_Restoring_sim_state_event_BEERS(self):
        parsed, user_or_model, simevent, item, action, simstate, datatable, graphstate, notes = parse_event("beers-law-lab",Restoring_sim_state_event,self.__class__.simstate_BEERS, {}, self.__class__.graphstate, '')
        self.assertEqual(Restoring_sim_state_event_parsed,parsed)
        self.assertEqual(Restoring_sim_state_event_user_or_model,user_or_model)
        self.assertEqual(Restoring_sim_state_event_simevent,simevent)
        self.assertEqual(Restoring_sim_state_event_item,item)
        self.assertEqual(Restoring_sim_state_event_action,action)
    
    def test_parsing_Moving_trial_in_table_event_CAPS(self):
        parsed, user_or_model, simevent, item, action, simstate, datatable, graphstate, notes = parse_event("capacitor-lab-basics",Restoring_sim_state_event,self.__class__.simstate_CAPS, {}, self.__class__.graphstate, '')
        self.assertEqual(Restoring_sim_state_event_parsed,parsed)
        self.assertEqual(Restoring_sim_state_event_user_or_model,user_or_model)
        self.assertEqual(Restoring_sim_state_event_simevent,simevent)
        self.assertEqual(Restoring_sim_state_event_item,item)
        self.assertEqual(Restoring_sim_state_event_action,action)



    def test_parsing_setting_sim_state_event_BEERS(self):
        parsed, user_or_model, simevent, item, action, simstate, datatable, graphstate, notes = parse_event("beers-law-lab",setting_sim_state_event,self.__class__.simstate_BEERS, {}, self.__class__.graphstate, '')
        self.assertEqual(setting_sim_state_event_parsed,parsed)
        self.assertEqual(setting_sim_state_event_user_or_model,user_or_model)
        self.assertEqual(setting_sim_state_event_simevent,simevent)
        self.assertEqual(setting_sim_state_event_item,item)
        self.assertEqual(setting_sim_state_event_action,action)
    
    def test_parsing_Moving_trial_in_table_event_CAPS(self):
        parsed, user_or_model, simevent, item, action, simstate, datatable, graphstate, notes = parse_event("capacitor-lab-basics",setting_sim_state_event,self.__class__.simstate_CAPS, {}, self.__class__.graphstate, '')
        self.assertEqual(setting_sim_state_event_parsed,parsed)
        self.assertEqual(setting_sim_state_event_user_or_model,user_or_model)
        self.assertEqual(setting_sim_state_event_simevent,simevent)
        self.assertEqual(setting_sim_state_event_item,item)
        self.assertEqual(setting_sim_state_event_action,action)



    def test_parsing_Selecting_Y_axis_event_BEERS(self):
        parsed, user_or_model, simevent, item, action, simstate, datatable, graphstate, notes = parse_event("beers-law-lab",Selecting_Y_axis_event,self.__class__.simstate_BEERS, {}, self.__class__.graphstate, '')
        self.assertEqual(Selecting_Y_axis_event_parsed,parsed)
        self.assertEqual(Selecting_Y_axis_event_user_or_model,user_or_model)
        self.assertEqual(Selecting_Y_axis_event_simevent,simevent)
        self.assertEqual(Selecting_Y_axis_event_item,item)
        self.assertEqual(Selecting_Y_axis_event_action,action)
    
    def test_parsing_Moving_trial_in_table_event_CAPS(self):
        parsed, user_or_model, simevent, item, action, simstate, datatable, graphstate, notes = parse_event("capacitor-lab-basics",Selecting_Y_axis_event,self.__class__.simstate_CAPS, {}, self.__class__.graphstate, '')
        self.assertEqual(Selecting_Y_axis_event_parsed,parsed)
        self.assertEqual(Selecting_Y_axis_event_user_or_model,user_or_model)
        self.assertEqual(Selecting_Y_axis_event_simevent,simevent)
        self.assertEqual(Selecting_Y_axis_event_item,item)
        self.assertEqual(Selecting_Y_axis_event_action,action)



    def test_parsing_Selecting_X_axis_event_BEERS(self):
        parsed, user_or_model, simevent, item, action, simstate, datatable, graphstate, notes = parse_event("beers-law-lab",Selecting_X_axis_event,self.__class__.simstate_BEERS, {}, self.__class__.graphstate, '')
        self.assertEqual(Selecting_X_axis_event_parsed,parsed)
        self.assertEqual(Selecting_X_axis_event_user_or_model,user_or_model)
        self.assertEqual(Selecting_X_axis_event_simevent,simevent)
        self.assertEqual(Selecting_X_axis_event_item,item)
        self.assertEqual(Selecting_X_axis_event_action,action)
    
    def test_parsing_Moving_trial_in_table_event_CAPS(self):
        parsed, user_or_model, simevent, item, action, simstate, datatable, graphstate, notes = parse_event("capacitor-lab-basics",Selecting_X_axis_event,self.__class__.simstate_CAPS, {}, self.__class__.graphstate, '')
        self.assertEqual(Selecting_X_axis_event_parsed,parsed)
        self.assertEqual(Selecting_X_axis_event_user_or_model,user_or_model)
        self.assertEqual(Selecting_X_axis_event_simevent,simevent)
        self.assertEqual(Selecting_X_axis_event_item,item)
        self.assertEqual(Selecting_X_axis_event_action,action)



    def test_parsing_Selecting_scale_of_Y_axis_event_BEERS(self):
        parsed, user_or_model, simevent, item, action, simstate, datatable, graphstate, notes = parse_event("beers-law-lab",Selecting_scale_of_Y_axis_event,self.__class__.simstate_BEERS, {}, self.__class__.graphstate, '')
        self.assertEqual(Selecting_scale_of_Y_axis_event_parsed,parsed)
        self.assertEqual(Selecting_scale_of_Y_axis_event_user_or_model,user_or_model)
        self.assertEqual(Selecting_scale_of_Y_axis_event_simevent,simevent)
        self.assertEqual(Selecting_scale_of_Y_axis_event_item,item)
        self.assertEqual(Selecting_scale_of_Y_axis_event_action,action)
    
    def test_parsing_Moving_trial_in_table_event_CAPS(self):
        parsed, user_or_model, simevent, item, action, simstate, datatable, graphstate, notes = parse_event("capacitor-lab-basics",Selecting_scale_of_Y_axis_event,self.__class__.simstate_CAPS, {}, self.__class__.graphstate, '')
        self.assertEqual(Selecting_scale_of_Y_axis_event_parsed,parsed)
        self.assertEqual(Selecting_scale_of_Y_axis_event_user_or_model,user_or_model)
        self.assertEqual(Selecting_scale_of_Y_axis_event_simevent,simevent)
        self.assertEqual(Selecting_scale_of_Y_axis_event_item,item)
        self.assertEqual(Selecting_scale_of_Y_axis_event_action,action)



    def test_parsing_Selecting_scale_of_X_axis_event_BEERS(self):
        parsed, user_or_model, simevent, item, action, simstate, datatable, graphstate, notes = parse_event("beers-law-lab",Selecting_scale_of_X_axis_event,self.__class__.simstate_BEERS, {}, self.__class__.graphstate, '')
        self.assertEqual(Selecting_scale_of_X_axis_event_parsed,parsed)
        self.assertEqual(Selecting_scale_of_X_axis_event_user_or_model,user_or_model)
        self.assertEqual(Selecting_scale_of_X_axis_event_simevent,simevent)
        self.assertEqual(Selecting_scale_of_X_axis_event_item,item)
        self.assertEqual(Selecting_scale_of_X_axis_event_action,action)
    
    def test_parsing_Moving_trial_in_table_event_CAPS(self):
        parsed, user_or_model, simevent, item, action, simstate, datatable, graphstate, notes = parse_event("capacitor-lab-basics",Selecting_scale_of_X_axis_event,self.__class__.simstate_CAPS, {}, self.__class__.graphstate, '')
        self.assertEqual(Selecting_scale_of_X_axis_event_parsed,parsed)
        self.assertEqual(Selecting_scale_of_X_axis_event_user_or_model,user_or_model)
        self.assertEqual(Selecting_scale_of_X_axis_event_simevent,simevent)
        self.assertEqual(Selecting_scale_of_X_axis_event_item,item)
        self.assertEqual(Selecting_scale_of_X_axis_event_action,action)



    def test_parsing_editing_notes_event_BEERS(self):
        parsed, user_or_model, simevent, item, action, simstate, datatable, graphstate, notes = parse_event("beers-law-lab",editing_notes_event,self.__class__.simstate_BEERS, {}, self.__class__.graphstate, '')
        self.assertEqual(editing_notes_event_parsed,parsed)
        self.assertEqual(editing_notes_event_user_or_model,user_or_model)
        self.assertEqual(editing_notes_event_simevent,simevent)
        self.assertEqual(editing_notes_event_item,item)
        self.assertEqual(editing_notes_event_action,action)
    
    def test_parsing_Moving_trial_in_table_event_CAPS(self):
        parsed, user_or_model, simevent, item, action, simstate, datatable, graphstate, notes = parse_event("capacitor-lab-basics",editing_notes_event,self.__class__.simstate_CAPS, {}, self.__class__.graphstate, '')
        self.assertEqual(editing_notes_event_parsed,parsed)
        self.assertEqual(editing_notes_event_user_or_model,user_or_model)
        self.assertEqual(editing_notes_event_simevent,simevent)
        self.assertEqual(editing_notes_event_item,item)
        self.assertEqual(editing_notes_event_action,action)



    def test_parsing_collapsing_table_event_BEERS(self):
        parsed, user_or_model, simevent, item, action, simstate, datatable, graphstate, notes = parse_event("beers-law-lab",collapsing_table_event,self.__class__.simstate_BEERS, {}, self.__class__.graphstate, '')
        self.assertEqual(collapsing_table_event_parsed,parsed)
        self.assertEqual(collapsing_table_event_user_or_model,user_or_model)
        self.assertEqual(collapsing_table_event_simevent,simevent)
        self.assertEqual(collapsing_table_event_item,item)
        self.assertEqual(collapsing_table_event_action,action)
    
    def test_parsing_Moving_trial_in_table_event_CAPS(self):
        parsed, user_or_model, simevent, item, action, simstate, datatable, graphstate, notes = parse_event("capacitor-lab-basics",collapsing_table_event,self.__class__.simstate_CAPS, {}, self.__class__.graphstate, '')
        self.assertEqual(collapsing_table_event_parsed,parsed)
        self.assertEqual(collapsing_table_event_user_or_model,user_or_model)
        self.assertEqual(collapsing_table_event_simevent,simevent)
        self.assertEqual(collapsing_table_event_item,item)
        self.assertEqual(collapsing_table_event_action,action)



    def test_parsing_collapsing_simulation_event_BEERS(self):
        parsed, user_or_model, simevent, item, action, simstate, datatable, graphstate, notes = parse_event("beers-law-lab",collapsing_simulation_event,self.__class__.simstate_BEERS, {}, self.__class__.graphstate, '')
        self.assertEqual(collapsing_simulation_event_parsed,parsed)
        self.assertEqual(collapsing_simulation_event_user_or_model,user_or_model)
        self.assertEqual(collapsing_simulation_event_simevent,simevent)
        self.assertEqual(collapsing_simulation_event_item,item)
        self.assertEqual(collapsing_simulation_event_action,action)
    
    def test_parsing_Moving_trial_in_table_event_CAPS(self):
        parsed, user_or_model, simevent, item, action, simstate, datatable, graphstate, notes = parse_event("capacitor-lab-basics",collapsing_simulation_event,self.__class__.simstate_CAPS, {}, self.__class__.graphstate, '')
        self.assertEqual(collapsing_simulation_event_parsed,parsed)
        self.assertEqual(collapsing_simulation_event_user_or_model,user_or_model)
        self.assertEqual(collapsing_simulation_event_simevent,simevent)
        self.assertEqual(collapsing_simulation_event_item,item)
        self.assertEqual(collapsing_simulation_event_action,action)



    def test_parsing_expanding_simulation_event_BEERS(self):
        parsed, user_or_model, simevent, item, action, simstate, datatable, graphstate, notes = parse_event("beers-law-lab",expanding_simulation_event,self.__class__.simstate_BEERS, {}, self.__class__.graphstate, '')
        self.assertEqual(expanding_simulation_event_parsed,parsed)
        self.assertEqual(expanding_simulation_event_user_or_model,user_or_model)
        self.assertEqual(expanding_simulation_event_simevent,simevent)
        self.assertEqual(expanding_simulation_event_item,item)
        self.assertEqual(expanding_simulation_event_action,action)
    
    def test_parsing_Moving_trial_in_table_event_CAPS(self):
        parsed, user_or_model, simevent, item, action, simstate, datatable, graphstate, notes = parse_event("capacitor-lab-basics",expanding_simulation_event,self.__class__.simstate_CAPS, {}, self.__class__.graphstate, '')
        self.assertEqual(expanding_simulation_event_parsed,parsed)
        self.assertEqual(expanding_simulation_event_user_or_model,user_or_model)
        self.assertEqual(expanding_simulation_event_simevent,simevent)
        self.assertEqual(expanding_simulation_event_item,item)
        self.assertEqual(expanding_simulation_event_action,action)



    def test_parsing_Moving_trial_in_table_event_BEERS(self):
        parsed, user_or_model, simevent, item, action, simstate, datatable, graphstate, notes = parse_event("beers-law-lab",Moving_trial_in_table_event,self.__class__.simstate_BEERS, {}, self.__class__.graphstate, '')
        self.assertEqual(Moving_trial_in_table_event_parsed,parsed)
        self.assertEqual(Moving_trial_in_table_event_user_or_model,user_or_model)
        self.assertEqual(Moving_trial_in_table_event_simevent,simevent)
        self.assertEqual(Moving_trial_in_table_event_item,item)
        self.assertEqual(Moving_trial_in_table_event_action,action)
    
    def test_parsing_Moving_trial_in_table_event_CAPS(self):
        parsed, user_or_model, simevent, item, action, simstate, datatable, graphstate, notes = parse_event("capacitor-lab-basics",Moving_trial_in_table_event,self.__class__.simstate_CAPS, {}, self.__class__.graphstate, '')
        self.assertEqual(Moving_trial_in_table_event_parsed,parsed)
        self.assertEqual(Moving_trial_in_table_event_user_or_model,user_or_model)
        self.assertEqual(Moving_trial_in_table_event_simevent,simevent)
        self.assertEqual(Moving_trial_in_table_event_item,item)
        self.assertEqual(Moving_trial_in_table_event_action,action)




if __name__ == '__main__':
    unittest.main()

    # def test_mega_parser(self): #for log data after March 20th
    #     '''
    #     Tests the function mega parser() on frabricated log data.
    #     '''
    #     test_table = np.genfromtxt('sample_beers_log_dreamtable.txt', delimiter='\t', dtype='string', skip_header=1)
    #     test_log_json = 'sample_beers_log.json'
    #     session = Session()
    #     session.get_session_data_from_file(test_log_json)
    #     sim,table = mega_parser('90447168',session.events)
    #     self.assertEqual(sim,'light_absorbance')
    #     np.testing.assert_array_equal(table[1:,:],test_table)