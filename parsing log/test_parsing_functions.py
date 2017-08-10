'''
author: sperez8
data: june 14 2017

This script cleans raw log files and splits them into individual session files stored in the log data folder
'''
import unittest
import json
from utils import convert_unix_time
from mega_parser import *


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


json_state_event = json.loads('''{
        "data": {
            "componentType": "TPhETIO", 
            "event": "state", 
            "eventType": "model", 
            "messageIndex": 4083, 
            "parameters": {
                "state": {
                    "beersLawLab.beersLawScreen.model.cuvette.widthProperty": 1.032, 
                    "beersLawLab.beersLawScreen.model.detector.body.locationProperty": {
                        "x": 6.3, 
                        "y": 0.2
                    }, 
                    "beersLawLab.beersLawScreen.model.detector.modeProperty": "absorbance", 
                    "beersLawLab.beersLawScreen.model.detector.probe.locationProperty": {
                        "x": 5.793103448275863, 
                        "y": 2
                    }, 
                    "beersLawLab.beersLawScreen.model.detector.valueProperty": 0.991752, 
                    "beersLawLab.beersLawScreen.model.light.onProperty": true, 
                    "beersLawLab.beersLawScreen.model.light.wavelengthProperty": 780, 
                    "beersLawLab.beersLawScreen.model.ruler.locationProperty": {
                        "x": 3.3, 
                        "y": 3.58
                    }, 
                    "beersLawLab.beersLawScreen.model.solutionProperty": "beersLawLab.beersLawScreen.solutions.copperSulfate", 
                    "beersLawLab.beersLawScreen.solutions.cobaltChloride.concentrationProperty": 0.1, 
                    "beersLawLab.beersLawScreen.solutions.cobaltIINitrate.concentrationProperty": 0.1, 
                    "beersLawLab.beersLawScreen.solutions.copperSulfate.concentrationProperty": 0.1, 
                    "beersLawLab.beersLawScreen.solutions.drinkMix.concentrationProperty": 0.1, 
                    "beersLawLab.beersLawScreen.solutions.nickelIIChloride.concentrationProperty": 0.1, 
                    "beersLawLab.beersLawScreen.solutions.potassiumChromate.concentrationProperty": 0.0001, 
                    "beersLawLab.beersLawScreen.solutions.potassiumDichromate.concentrationProperty": 0.0001, 
                    "beersLawLab.beersLawScreen.solutions.potassiumPermanganate.concentrationProperty": 0.0001, 
                    "beersLawLab.beersLawScreen.view.wavelengthControls.variableWavelengthProperty": true, 
                    "beersLawLab.sim.activeProperty": true, 
                    "beersLawLab.sim.screenIndexProperty": 0, 
                    "beersLawLab.sim.showHomeScreenProperty": false
                }
            }, 
            "phetioID": "phetio", 
            "time": 1490049191893
        }, 
        "event": "phetio.state", 
        "index": 3584, 
        "timestamp": 1490049191691, 
        "type": "model"
    } ''')

json_state_event_DATA = json.loads('''{
            "componentType": "TPhETIO", 
            "event": "state", 
            "eventType": "model", 
            "messageIndex": 4083, 
            "parameters": {
                "state": {
                    "beersLawLab.beersLawScreen.model.cuvette.widthProperty": 1.032, 
                    "beersLawLab.beersLawScreen.model.detector.body.locationProperty": {
                        "x": 6.3, 
                        "y": 0.2
                    }, 
                    "beersLawLab.beersLawScreen.model.detector.modeProperty": "absorbance", 
                    "beersLawLab.beersLawScreen.model.detector.probe.locationProperty": {
                        "x": 5.793103448275863, 
                        "y": 2
                    }, 
                    "beersLawLab.beersLawScreen.model.detector.valueProperty": 0.991752, 
                    "beersLawLab.beersLawScreen.model.light.onProperty": true, 
                    "beersLawLab.beersLawScreen.model.light.wavelengthProperty": 780, 
                    "beersLawLab.beersLawScreen.model.ruler.locationProperty": {
                        "x": 3.3, 
                        "y": 3.58
                    }, 
                    "beersLawLab.beersLawScreen.model.solutionProperty": "beersLawLab.beersLawScreen.solutions.copperSulfate", 
                    "beersLawLab.beersLawScreen.solutions.cobaltChloride.concentrationProperty": 0.1, 
                    "beersLawLab.beersLawScreen.solutions.cobaltIINitrate.concentrationProperty": 0.1, 
                    "beersLawLab.beersLawScreen.solutions.copperSulfate.concentrationProperty": 0.1, 
                    "beersLawLab.beersLawScreen.solutions.drinkMix.concentrationProperty": 0.1, 
                    "beersLawLab.beersLawScreen.solutions.nickelIIChloride.concentrationProperty": 0.1, 
                    "beersLawLab.beersLawScreen.solutions.potassiumChromate.concentrationProperty": 0.0001, 
                    "beersLawLab.beersLawScreen.solutions.potassiumDichromate.concentrationProperty": 0.0001, 
                    "beersLawLab.beersLawScreen.solutions.potassiumPermanganate.concentrationProperty": 0.0001, 
                    "beersLawLab.beersLawScreen.view.wavelengthControls.variableWavelengthProperty": true, 
                    "beersLawLab.sim.activeProperty": true, 
                    "beersLawLab.sim.screenIndexProperty": 0, 
                    "beersLawLab.sim.showHomeScreenProperty": false
                }
            }, 
            "phetioID": "phetio", 
            "time": 1490049191893
        }''')


class TestParsingIndividualEvents(unittest.TestCase):
    """
    Our basic test class for all file cleaning ans splitting functions
    """
    def test_get_data(self):
        '''
        Grabs the information under the first event key "data"
        '''
        self.assertEqual(get_data(json_state_event), json_state_event_DATA)


    # def test_get_data_parameters(self):
    #     '''
    #     Grabs the information under the event's data > parameters
    #     '''
    #     get_data_parameters(json_state_event, print_error = True)
    #     try: 
    #         return get_data(event, print_error)['parameters']
    #     except KeyError:
    #         if print_error:
    #             print "Error: event",event['index']," has no 'data > parameters'"
    #             # traceback.print_exc()

    # def test_get_messages(self):
    #     '''
    #     Grabs the information under the event's data > parameters > messages
    #     '''
    #     get_messages(json_state_event, print_error = True)
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
    #     get_method(json_state_event, print_error = True)
    #     try: 
    #         return get_data_parameters(event, print_error)['method']
    #     except KeyError:
    #         if print_error:
    #             print "Error: event",event['index']," has no 'data > parameters > method'"
    #             # traceback.print_exc()

    # def test_get_state(self):
    #     '''
    #     Grabs the state information under the event's data > parameters > state
    #     '''
    #     get_state(json_state_event, print_error = True)
    #     try: 
    #         return get_data_parameters(event, print_error)['state']
    #     except KeyError:
    #         if print_error:
    #             print "Error: event",event['index']," has no 'data > parameters > state'"
    #             # traceback.print_exc()

    # def test_get_data_parameters_args(self):
    #     '''
    #     Grabs the information under the event's data > parameterers > args
    #     '''
    #     get_data_parameters_args(json_state_event, print_error = True)
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
    #     get_data_parameters_args_parameters(json_state_event, print_error = True)
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
    #     get_args_phetioID(json_state_event, print_error = True)
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
    #     get_data_children(json_state_event, print_error = True)
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
    #     get_data_children_parameters(json_state_event, print_error = True)
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
    #     get_notes(json_state_event, print_error = True)
    #     try:
    #         return get_data_parameters(event, print_error)['text'].replace('\n','\\n')
    #     except KeyError:
    #         if print_error:
    #             print "Error: event",event['index']," has no 'data > parameters > text'"
    #             # traceback.print_exc()

if __name__ == '__main__':
    unittest.main()