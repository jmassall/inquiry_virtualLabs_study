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

getting_values_event = json.loads('''{
        "data": {
            "componentType": "TSimIFrameAPI", 
            "event": "invoked", 
            "eventType": "wrapper", 
            "messageIndex": 28558, 
            "parameters": {
                "messageID": 7, 
                "messages": [
                    {
                        "messageID": 7, 
                        "method": "getValue", 
                        "phetioID": "beersLawLab.beersLawScreen.model.light.wavelengthProperty", 
                        "protocol": "phet-io-0.0.1"
                    }, 
                    {
                        "messageID": 7, 
                        "method": "getValue", 
                        "phetioID": "beersLawLab.beersLawScreen.model.cuvette.widthProperty", 
                        "protocol": "phet-io-0.0.1"
                    }, 
                    {
                        "messageID": 7, 
                        "method": "getValue", 
                        "phetioID": "beersLawLab.beersLawScreen.model.solutionProperty", 
                        "protocol": "phet-io-0.0.1"
                    }, 
                    {
                        "messageID": 7, 
                        "method": "getValue", 
                        "phetioID": "beersLawLab.beersLawScreen.model.detector.valueProperty", 
                        "protocol": "phet-io-0.0.1"
                    }, 
                    {
                        "messageID": 7, 
                        "method": "getValue", 
                        "phetioID": "beersLawLab.beersLawScreen.model.light.onProperty", 
                        "protocol": "phet-io-0.0.1"
                    }, 
                    {
                        "messageID": 7, 
                        "method": "getScreenshotDataURL", 
                        "phetioID": "beersLawLab.sim", 
                        "protocol": "phet-io-0.0.1"
                    }, 
                    {
                        "messageID": 7, 
                        "method": "getState", 
                        "phetioID": "phetio", 
                        "protocol": "phet-io-0.0.1"
                    }
                ], 
                "protocol": "phet-io-0.0.1"
            }, 
            "phetioID": "beersLawLab.simIFrameAPI", 
            "time": 1490049393192
        }, 
        "event": "beersLawLab.simIFrameAPI.invoked", 
        "index": 25378, 
        "timestamp": 1490049393045, 
        "type": "model"
    }''')

getting_values_event_DATA = json.loads('''{
        "componentType": "TSimIFrameAPI", 
        "event": "invoked", 
        "eventType": "wrapper", 
        "messageIndex": 28558, 
        "parameters": {
            "messageID": 7, 
            "messages": [
                {
                    "messageID": 7, 
                    "method": "getValue", 
                    "phetioID": "beersLawLab.beersLawScreen.model.light.wavelengthProperty", 
                    "protocol": "phet-io-0.0.1"
                }, 
                {
                    "messageID": 7, 
                    "method": "getValue", 
                    "phetioID": "beersLawLab.beersLawScreen.model.cuvette.widthProperty", 
                    "protocol": "phet-io-0.0.1"
                }, 
                {
                    "messageID": 7, 
                    "method": "getValue", 
                    "phetioID": "beersLawLab.beersLawScreen.model.solutionProperty", 
                    "protocol": "phet-io-0.0.1"
                }, 
                {
                    "messageID": 7, 
                    "method": "getValue", 
                    "phetioID": "beersLawLab.beersLawScreen.model.detector.valueProperty", 
                    "protocol": "phet-io-0.0.1"
                }, 
                {
                    "messageID": 7, 
                    "method": "getValue", 
                    "phetioID": "beersLawLab.beersLawScreen.model.light.onProperty", 
                    "protocol": "phet-io-0.0.1"
                }, 
                {
                    "messageID": 7, 
                    "method": "getScreenshotDataURL", 
                    "phetioID": "beersLawLab.sim", 
                    "protocol": "phet-io-0.0.1"
                }, 
                {
                    "messageID": 7, 
                    "method": "getState", 
                    "phetioID": "phetio", 
                    "protocol": "phet-io-0.0.1"
                }
            ], 
            "protocol": "phet-io-0.0.1"
        }, 
        "phetioID": "beersLawLab.simIFrameAPI", 
        "time": 1490049393192
    }''')

getting_values_event_DATA_PARAMETERS = json.loads('''{
            "messageID": 7, 
            "messages": [
                {
                    "messageID": 7, 
                    "method": "getValue", 
                    "phetioID": "beersLawLab.beersLawScreen.model.light.wavelengthProperty", 
                    "protocol": "phet-io-0.0.1"
                }, 
                {
                    "messageID": 7, 
                    "method": "getValue", 
                    "phetioID": "beersLawLab.beersLawScreen.model.cuvette.widthProperty", 
                    "protocol": "phet-io-0.0.1"
                }, 
                {
                    "messageID": 7, 
                    "method": "getValue", 
                    "phetioID": "beersLawLab.beersLawScreen.model.solutionProperty", 
                    "protocol": "phet-io-0.0.1"
                }, 
                {
                    "messageID": 7, 
                    "method": "getValue", 
                    "phetioID": "beersLawLab.beersLawScreen.model.detector.valueProperty", 
                    "protocol": "phet-io-0.0.1"
                }, 
                {
                    "messageID": 7, 
                    "method": "getValue", 
                    "phetioID": "beersLawLab.beersLawScreen.model.light.onProperty", 
                    "protocol": "phet-io-0.0.1"
                }, 
                {
                    "messageID": 7, 
                    "method": "getScreenshotDataURL", 
                    "phetioID": "beersLawLab.sim", 
                    "protocol": "phet-io-0.0.1"
                }, 
                {
                    "messageID": 7, 
                    "method": "getState", 
                    "phetioID": "phetio", 
                    "protocol": "phet-io-0.0.1"
                }
            ], 
            "protocol": "phet-io-0.0.1"
        }''')

initializing_event1 = json.loads('''{
        "data": {
            "componentType": "TSimIFrameAPI", 
            "event": "invoked", 
            "eventType": "wrapper", 
            "messageIndex": 0, 
            "parameters": {
                "args": [
                    [
                        {
                            "args": [
                                false
                            ], 
                            "method": "setPickable", 
                            "phetioID": "beersLawLab.beersLawScreen.view.solutionControls.comboBox"
                        }, 
                        {
                            "args": [
                                "beersLawLab.beersLawScreen.solutions.copperSulfate"
                            ], 
                            "method": "setValue", 
                            "phetioID": "beersLawLab.beersLawScreen.model.solutionProperty"
                        }, 
                        {
                            "args": [
                                false
                            ], 
                            "method": "setVisible", 
                            "phetioID": "beersLawLab.beersLawScreen.view.wavelengthControls.presetWavelengthRadioButton"
                        }, 
                        {
                            "args": [
                                false
                            ], 
                            "method": "setVisible", 
                            "phetioID": "beersLawLab.beersLawScreen.view.wavelengthControls.variableWavelengthRadioButton"
                        }, 
                        {
                            "args": [
                                true
                            ], 
                            "method": "setValue", 
                            "phetioID": "beersLawLab.beersLawScreen.view.wavelengthControls.variableWavelengthProperty"
                        }, 
                        {
                            "args": [
                                {
                                    "x": 3.3, 
                                    "y": 3.58
                                }
                            ], 
                            "method": "setValue", 
                            "phetioID": "beersLawLab.beersLawScreen.model.ruler.locationProperty"
                        }, 
                        {
                            "args": [
                                false
                            ], 
                            "method": "setVisible", 
                            "phetioID": "beersLawLab.beersLawScreen.view.wavelengthControls.valueDisplay"
                        }, 
                        {
                            "args": [
                                false
                            ], 
                            "method": "setVisible", 
                            "phetioID": "beersLawLab.beersLawScreen.view.wavelengthControls.valueBackground"
                        }, 
                        {
                            "args": [
                                "absorbance"
                            ], 
                            "method": "setValue", 
                            "phetioID": "beersLawLab.beersLawScreen.model.detector.modeProperty"
                        }, 
                        {
                            "args": [
                                false
                            ], 
                            "method": "setVisible", 
                            "phetioID": "beersLawLab.beersLawScreen.view.detectorNode.bodyNode.transmittanceRadioButton"
                        }, 
                        {
                            "args": [
                                false
                            ], 
                            "method": "setCircleButtonVisible", 
                            "phetioID": "beersLawLab.beersLawScreen.view.detectorNode.bodyNode.absorbanceRadioButton"
                        }, 
                        {
                            "args": [
                                false
                            ], 
                            "method": "setVisible", 
                            "phetioID": "beersLawLab.beersLawScreen.view.solutionControls.comboBox.arrow"
                        }, 
                        {
                            "args": [
                                false
                            ], 
                            "method": "setVisible", 
                            "phetioID": "beersLawLab.beersLawScreen.view.solutionControls.comboBox.separator"
                        }, 
                        {
                            "args": [
                                false
                            ], 
                            "method": "setVisible", 
                            "phetioID": "beersLawLab.beersLawScreen.view.resetAllButton"
                        }
                    ]
                ], 
                "messageID": 2, 
                "method": "addExpressions", 
                "phetioID": "phetio", 
                "protocol": "phet-io-0.0.1"
            }, 
            "phetioID": "beersLawLab.simIFrameAPI", 
            "time": 1490049165985
        }, 
        "event": "beersLawLab.simIFrameAPI.invoked", 
        "index": 0, 
        "timestamp": 1490049165776, 
        "type": "model"
    }''')

initializing_event2 = json.loads('''{
        "data": {
            "children": [
                {
                    "componentType": "TTandemText", 
                    "event": "textChanged", 
                    "eventType": "model", 
                    "messageIndex": 10, 
                    "parameters": {
                        "newText": "Light Absorbance Lab", 
                        "oldText": "\u202aBeer's Law Lab\u202c"
                    }, 
                    "phetioID": "beersLawLab.navigationBar.titleTextNode", 
                    "time": 1490049166782
                }
            ], 
            "componentType": "TSimIFrameAPI", 
            "event": "invoked", 
            "eventType": "wrapper", 
            "messageIndex": 9, 
            "parameters": {
                "args": [
                    "Light Absorbance Lab"
                ], 
                "messageID": 4, 
                "method": "setText", 
                "phetioID": "beersLawLab.navigationBar.titleTextNode", 
                "protocol": "phet-io-0.0.1"
            }, 
            "phetioID": "beersLawLab.simIFrameAPI", 
            "time": 1490049166780
        }, 
        "event": "beersLawLab.simIFrameAPI.invoked", 
        "index": 7, 
        "timestamp": 1490049166592, 
        "type": "model"
    }''')


initializing_event3 = json.loads('''    {
        "data": {
            "componentType": "TSimIFrameAPI", 
            "event": "invoked", 
            "eventType": "wrapper", 
            "messageIndex": 1, 
            "parameters": {
                "args": [], 
                "messageID": 3, 
                "method": "launchSimulation", 
                "phetioID": "phetio", 
                "protocol": "phet-io-0.0.1"
            }, 
            "phetioID": "beersLawLab.simIFrameAPI", 
            "time": 1490049165988
        }, 
        "event": "beersLawLab.simIFrameAPI.invoked", 
        "index": 1, 
        "timestamp": 1490049166511, 
        "type": "model"
    }''')

initializing_event1_METHOD = "addExpressions"
initializing_event2_METHOD = "setText"
initializing_event3_METHOD = "launchSimulation"


record_event = json.loads('''    {
        "data": {
            "children": [
                {
                    "componentType": "TButton", 
                    "event": "pressed", 
                    "eventType": "user", 
                    "messageIndex": 28561, 
                    "parameters": {
                        "absorbance": 0.961, 
                        "absorbance_x": 0.961, 
                        "absorbance_y": 0.961, 
                        "concentration": 200, 
                        "concentration_x": 200, 
                        "concentration_y": 200, 
                        "cuvetteWidth": 0.5, 
                        "cuvetteWidth_x": 0.5, 
                        "cuvetteWidth_y": 0.5, 
                        "image": {}, 
                        "state": {
                            "beersLawLab.beersLawScreen.model.cuvette.widthProperty": 0.5, 
                            "beersLawLab.beersLawScreen.model.detector.body.locationProperty": {
                                "x": 6.3, 
                                "y": 0.2
                            }, 
                            "beersLawLab.beersLawScreen.model.detector.modeProperty": "absorbance", 
                            "beersLawLab.beersLawScreen.model.detector.probe.locationProperty": {
                                "x": 5.793103448275863, 
                                "y": 2
                            }, 
                            "beersLawLab.beersLawScreen.model.detector.valueProperty": 0.961, 
                            "beersLawLab.beersLawScreen.model.light.onProperty": true, 
                            "beersLawLab.beersLawScreen.model.light.wavelengthProperty": 780, 
                            "beersLawLab.beersLawScreen.model.ruler.locationProperty": {
                                "x": 3.3, 
                                "y": 3.58
                            }, 
                            "beersLawLab.beersLawScreen.model.solutionProperty": "beersLawLab.beersLawScreen.solutions.copperSulfate", 
                            "beersLawLab.beersLawScreen.solutions.cobaltChloride.concentrationProperty": 0.1, 
                            "beersLawLab.beersLawScreen.solutions.cobaltIINitrate.concentrationProperty": 0.1, 
                            "beersLawLab.beersLawScreen.solutions.copperSulfate.concentrationProperty": 0.2, 
                            "beersLawLab.beersLawScreen.solutions.drinkMix.concentrationProperty": 0.1, 
                            "beersLawLab.beersLawScreen.solutions.nickelIIChloride.concentrationProperty": 0.1, 
                            "beersLawLab.beersLawScreen.solutions.potassiumChromate.concentrationProperty": 0.0001, 
                            "beersLawLab.beersLawScreen.solutions.potassiumDichromate.concentrationProperty": 0.0001, 
                            "beersLawLab.beersLawScreen.solutions.potassiumPermanganate.concentrationProperty": 0.0001, 
                            "beersLawLab.beersLawScreen.view.wavelengthControls.variableWavelengthProperty": true, 
                            "beersLawLab.sim.activeProperty": true, 
                            "beersLawLab.sim.screenIndexProperty": 0, 
                            "beersLawLab.sim.showHomeScreenProperty": false
                        }, 
                        "trialNumber": 1, 
                        "trialNumber_x": 1, 
                        "trialNumber_y": 1, 
                        "visible": false, 
                        "wavelength": 780, 
                        "wavelength_x": 780, 
                        "wavelength_y": 780
                    }, 
                    "phetioID": "labBook.recordDataButton", 
                    "time": 1490049393259
                }
            ], 
            "componentType": "TSimIFrameAPI", 
            "event": "invoked", 
            "eventType": "wrapper", 
            "messageIndex": 28560, 
            "parameters": {
                "args": [
                    {
                        "componentType": {
                            "events": [
                                "pressed"
                            ], 
                            "typeName": "TButton"
                        }, 
                        "event": "pressed", 
                        "eventType": "user", 
                        "parameters": {
                            "absorbance": 0.961, 
                            "absorbance_x": 0.961, 
                            "absorbance_y": 0.961, 
                            "concentration": 200, 
                            "concentration_x": 200, 
                            "concentration_y": 200, 
                            "cuvetteWidth": 0.5, 
                            "cuvetteWidth_x": 0.5, 
                            "cuvetteWidth_y": 0.5, 
                            "image": {}, 
                            "state": {
                                "beersLawLab.beersLawScreen.model.cuvette.widthProperty": 0.5, 
                                "beersLawLab.beersLawScreen.model.detector.body.locationProperty": {
                                    "x": 6.3, 
                                    "y": 0.2
                                }, 
                                "beersLawLab.beersLawScreen.model.detector.modeProperty": "absorbance", 
                                "beersLawLab.beersLawScreen.model.detector.probe.locationProperty": {
                                    "x": 5.793103448275863, 
                                    "y": 2
                                }, 
                                "beersLawLab.beersLawScreen.model.detector.valueProperty": 0.961, 
                                "beersLawLab.beersLawScreen.model.light.onProperty": true, 
                                "beersLawLab.beersLawScreen.model.light.wavelengthProperty": 780, 
                                "beersLawLab.beersLawScreen.model.ruler.locationProperty": {
                                    "x": 3.3, 
                                    "y": 3.58
                                }, 
                                "beersLawLab.beersLawScreen.model.solutionProperty": "beersLawLab.beersLawScreen.solutions.copperSulfate", 
                                "beersLawLab.beersLawScreen.solutions.cobaltChloride.concentrationProperty": 0.1, 
                                "beersLawLab.beersLawScreen.solutions.cobaltIINitrate.concentrationProperty": 0.1, 
                                "beersLawLab.beersLawScreen.solutions.copperSulfate.concentrationProperty": 0.2, 
                                "beersLawLab.beersLawScreen.solutions.drinkMix.concentrationProperty": 0.1, 
                                "beersLawLab.beersLawScreen.solutions.nickelIIChloride.concentrationProperty": 0.1, 
                                "beersLawLab.beersLawScreen.solutions.potassiumChromate.concentrationProperty": 0.0001, 
                                "beersLawLab.beersLawScreen.solutions.potassiumDichromate.concentrationProperty": 0.0001, 
                                "beersLawLab.beersLawScreen.solutions.potassiumPermanganate.concentrationProperty": 0.0001, 
                                "beersLawLab.beersLawScreen.view.wavelengthControls.variableWavelengthProperty": true, 
                                "beersLawLab.sim.activeProperty": true, 
                                "beersLawLab.sim.screenIndexProperty": 0, 
                                "beersLawLab.sim.showHomeScreenProperty": false
                            }, 
                            "trialNumber": 1, 
                            "trialNumber_x": 1, 
                            "trialNumber_y": 1, 
                            "visible": false, 
                            "wavelength": 780, 
                            "wavelength_x": 780, 
                            "wavelength_y": 780
                        }, 
                        "phetioID": "labBook.recordDataButton"
                    }
                ], 
                "messageID": 8, 
                "method": "triggerEvent", 
                "phetioID": "phetio", 
                "protocol": "phet-io-0.0.1"
            }, 
            "phetioID": "beersLawLab.simIFrameAPI", 
            "time": 1490049393259
        }, 
        "event": "beersLawLab.simIFrameAPI.invoked", 
        "index": 25380, 
        "timestamp": 1490049393057, 
        "type": "model"
    }''')

record_event_DATA_PARAMETERS_ARGS_PARAMETERS = json.loads('''{
                            "absorbance": 0.961, 
                            "absorbance_x": 0.961, 
                            "absorbance_y": 0.961, 
                            "concentration": 200, 
                            "concentration_x": 200, 
                            "concentration_y": 200, 
                            "cuvetteWidth": 0.5, 
                            "cuvetteWidth_x": 0.5, 
                            "cuvetteWidth_y": 0.5, 
                            "image": {}, 
                            "state": {
                                "beersLawLab.beersLawScreen.model.cuvette.widthProperty": 0.5, 
                                "beersLawLab.beersLawScreen.model.detector.body.locationProperty": {
                                    "x": 6.3, 
                                    "y": 0.2
                                }, 
                                "beersLawLab.beersLawScreen.model.detector.modeProperty": "absorbance", 
                                "beersLawLab.beersLawScreen.model.detector.probe.locationProperty": {
                                    "x": 5.793103448275863, 
                                    "y": 2
                                }, 
                                "beersLawLab.beersLawScreen.model.detector.valueProperty": 0.961, 
                                "beersLawLab.beersLawScreen.model.light.onProperty": true, 
                                "beersLawLab.beersLawScreen.model.light.wavelengthProperty": 780, 
                                "beersLawLab.beersLawScreen.model.ruler.locationProperty": {
                                    "x": 3.3, 
                                    "y": 3.58
                                }, 
                                "beersLawLab.beersLawScreen.model.solutionProperty": "beersLawLab.beersLawScreen.solutions.copperSulfate", 
                                "beersLawLab.beersLawScreen.solutions.cobaltChloride.concentrationProperty": 0.1, 
                                "beersLawLab.beersLawScreen.solutions.cobaltIINitrate.concentrationProperty": 0.1, 
                                "beersLawLab.beersLawScreen.solutions.copperSulfate.concentrationProperty": 0.2, 
                                "beersLawLab.beersLawScreen.solutions.drinkMix.concentrationProperty": 0.1, 
                                "beersLawLab.beersLawScreen.solutions.nickelIIChloride.concentrationProperty": 0.1, 
                                "beersLawLab.beersLawScreen.solutions.potassiumChromate.concentrationProperty": 0.0001, 
                                "beersLawLab.beersLawScreen.solutions.potassiumDichromate.concentrationProperty": 0.0001, 
                                "beersLawLab.beersLawScreen.solutions.potassiumPermanganate.concentrationProperty": 0.0001, 
                                "beersLawLab.beersLawScreen.view.wavelengthControls.variableWavelengthProperty": true, 
                                "beersLawLab.sim.activeProperty": true, 
                                "beersLawLab.sim.screenIndexProperty": 0, 
                                "beersLawLab.sim.showHomeScreenProperty": false
                            }, 
                            "trialNumber": 1, 
                            "trialNumber_x": 1, 
                            "trialNumber_y": 1, 
                            "visible": false, 
                            "wavelength": 780, 
                            "wavelength_x": 780, 
                            "wavelength_y": 780
                        }''')

record_event_PHETIOID = "labBook.recordDataButton"

axis_event = json.loads('''    {
        "data": {
            "children": [
                {
                    "componentType": "TDropDownSelect", 
                    "event": "changed", 
                    "eventType": "user", 
                    "messageIndex": 34192, 
                    "parameters": {
                        "feature": "cuvetteWidth_x"
                    }, 
                    "phetioID": "labBook.xFeature", 
                    "time": 1490049449026
                }
            ], 
            "componentType": "TSimIFrameAPI", 
            "event": "invoked", 
            "eventType": "wrapper", 
            "messageIndex": 34191, 
            "parameters": {
                "args": [
                    {
                        "componentType": {
                            "events": [
                                "changed"
                            ], 
                            "typeName": "TDropDownSelect"
                        }, 
                        "event": "changed", 
                        "eventType": "user", 
                        "parameters": {
                            "feature": "cuvetteWidth_x"
                        }, 
                        "phetioID": "labBook.xFeature"
                    }
                ], 
                "messageID": 24, 
                "method": "triggerEvent", 
                "phetioID": "phetio", 
                "protocol": "phet-io-0.0.1"
            }, 
            "phetioID": "beersLawLab.simIFrameAPI", 
            "time": 1490049449026
        }, 
        "event": "beersLawLab.simIFrameAPI.invoked", 
        "index": 30471, 
        "timestamp": 1490049448827, 
        "type": "model"
    }''')

axis_event_DATA_PARAMETERS_ARGS_PARAMETERS = json.loads('''{
                            "feature": "cuvetteWidth_x"
                        }''')

axis_event_PHETIOID = "labBook.xFeature"

notes_event = json.loads('''    {
        "data": {
            "componentType": "TextArea", 
            "event": "changed", 
            "eventType": "user", 
            "messageIndex": 2816, 
            "parameters": {
                "text": "Increase width = increase absorbance"
            }, 
            "phetioID": "labBook.textArea", 
            "time": 1484680992088
        }, 
        "event": "labBook.textArea.changed", 
        "index": 2592, 
        "timestamp": 1484680991929, 
        "type": "model"
    }''')

notes_event_NOTES = "Increase width = increase absorbance"