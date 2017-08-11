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

    def test_get_args_phetioID(self):
        '''
        Grabs the information under the event's data > parameters > args > phetioID
        '''
        self.assertEqual(get_args_phetioID(logsample.record_event), logsample.record_event_PHETIOID)
        self.assertEqual(get_args_phetioID(logsample.axis_event), logsample.axis_event_PHETIOID)

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

    # def test_get_messages(self):
    #     '''
    #     Grabs the information under the event's data > parameters > messages
    #     '''
    #     get_messages(logsample.state_event, print_error = True)
    #     try: 
    #         return get_data_parameters(event, print_error)['messages']
    #     except KeyError:
    #         if print_error:
    #             print "Error: event",event['index']," has no 'data > parameters > messages'"
    #             # traceback.print_exc()


    # def test_get_args_phetioID(self):
    #     '''
    #     Grabs the information under the event's data > parameters > args > phetioID
    #     '''
    #     get_args_phetioID(logsample.state_event, print_error = True)
    #     try: 
    #         return get_data_parameters_args(event, print_error)[0]['phetioID']
    #     except KeyError:
    #         if print_error:
    #             print "Error: event",event['index']," has no 'data > parameters > args > phetioID'"
    #             # traceback.print_exc()

    # def test_get_data_children(self):
    #     '''
    #     Grabs the information under the event's data > children
    #     '''
    #     get_data_children(logsample.state_event, print_error = True)
    #     try: 
    #         return get_data(event, print_error)['children']
    #     except KeyError:
    #         if print_error:
    #             print "Error: event",event['index']," has no 'data > children'"
    #             # traceback.print_exc()

    # def test_get_data_children_parameters(self):
    #     '''
    #     Grabs the information under the event's data > children > parameters
    #     '''
    #     get_data_children_parameters(logsample.state_event, print_error = True)
    #     try: 
    #         return get_data_children(event, print_error)[0]['parameters']
    #     except KeyError:
    #         if print_error:
    #             print "Error: event",event['index']," has no 'data > children > parameters'"
    #             # traceback.print_exc()

if __name__ == '__main__':
    unittest.main()