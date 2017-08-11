"""
Here is a collection of log data events (or portions of) stored as strings.
Each is structured as:

    'eventtype'_event_'portion'

so for example:

    state_event_DATA

is a string containing the contents of the key "data" in the event of type phetio.state
"""

import json

state_event = json.loads('''{
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

state_event_DATA = json.loads('''{
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

state_event_DATA_PARAMETERS = json.loads('''{
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
            }''')

state_event_STATE = json.loads('''{
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
                }''')