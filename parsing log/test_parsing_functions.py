'''
author: sperez8
data: june 14 2017

This script cleans raw log files and splits them into individual session files stored in the log data folder
'''
import unittest
from utils import convert_unix_time
from mega_parser import *
import test_log_samples as logsample

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


class TestParsingIndividualEvents(unittest.TestCase):
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


# class TestFullParsing(unittest.TestCase):
#     """
#     Basic test class for all parsing functions
#     """
#     def test_mega_parser(self): #for log data after March 20th
#         '''
#         Tests the function mega parser() on frabricated log data.
#         '''
#         from frabricated_log_events import fabricated_log_data_beers_post_march_20th
#         mega_parser('00000000',HEADER,fabricated_log_data_beers_post_march_20th)

if __name__ == '__main__':
    unittest.main()