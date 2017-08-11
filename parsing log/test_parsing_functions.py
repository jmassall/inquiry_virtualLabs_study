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
    Our basic test class for all file cleaning ans splitting functions
    """

    def test_convert_unix_time(self):
        """
        Tests conversion of time.
        """
        x = '1490049160615'
        self.assertEqual(convert_unix_time(x),'2017-03-20_15.32.40')


class TestParsingIndividualEvents(unittest.TestCase):
    """
    Our basic test class for all file cleaning ans splitting functions
    """
    def test_get_data(self):
        '''
        Grabs the information under the first event key "data"
        '''
        self.assertEqual(get_data(logsample.state_event), logsample.state_event_DATA)

    def test_get_data_parameters(self):
        '''
        Grabs the information under the first event key "data"
        '''
        self.assertEqual(get_data_parameters(logsample.state_event), logsample.state_event_DATA_PARAMETERS)

    def test_get_state(self):
        '''
        Grabs the information under the first event key "data"
        '''
        self.assertEqual(get_state(logsample.state_event), logsample.state_event_STATE)
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

    # def test_get_method(self):
    #     '''
    #     Grabs the information under the event's data > parameters > method
    #     '''
    #     get_method(logsample.state_event, print_error = True)
    #     try: 
    #         return get_data_parameters(event, print_error)['method']
    #     except KeyError:
    #         if print_error:
    #             print "Error: event",event['index']," has no 'data > parameters > method'"
    #             # traceback.print_exc()

    # def test_get_data_parameters_args(self):
    #     '''
    #     Grabs the information under the event's data > parameterers > args
    #     '''
    #     get_data_parameters_args(logsample.state_event, print_error = True)
    #     try: 
    #         return get_data_parameters(event, print_error)['args']
    #     except KeyError:
    #         if print_error:
    #             print "Error: event",event['index']," has no 'data > parameters > args'"
    #             # traceback.print_exc()

    # def test_get_data_parameters_args_parameters(self):
    #     '''
    #     Grabs the information under the event's data > parameterers > args
    #     '''
    #     get_data_parameters_args_parameters(logsample.state_event, print_error = True)
    #     try: 
    #         return get_data_parameters_args(event, print_error)[0]['parameters']
    #     except KeyError:
    #         if print_error:
    #             print "Error: event",event['index']," has no 'data > parameters > args > parameters'"
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

    # def test_get_notes(self):
    #     '''
    #     Grabs the notes under the event's data > parameters > text
    #     '''
    #     get_notes(logsample.state_event, print_error = True)
    #     try:
    #         return get_data_parameters(event, print_error)['text'].replace('\n','\\n')
    #     except KeyError:
    #         if print_error:
    #             print "Error: event",event['index']," has no 'data > parameters > text'"
    #             # traceback.print_exc()

if __name__ == '__main__':
    unittest.main()