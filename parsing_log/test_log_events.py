import json 


initializing_event = json.loads(''' {
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
        "time": 1490208079815
    }, 
    "event": "beersLawLab.simIFrameAPI.invoked", 
    "index": 0, 
    "timestamp": 1490208079592, 
    "type": "model"
}
''') 

initializing_event_parsed = True
initializing_event_user_or_model = 'model'
initializing_event_simevent = 'initializing'
initializing_event_item = 'sim'
initializing_event_action = 'addExpressions'

#####################################################################################################################
updating_state_event = json.loads(''' {
    "data": {
        "componentType": "TPhETIO", 
        "event": "state", 
        "eventType": "model", 
        "messageIndex": 6, 
        "parameters": {
            "state": {
                "beersLawLab.beersLawScreen.model.cuvette.widthProperty": 1, 
                "beersLawLab.beersLawScreen.model.detector.body.locationProperty": {
                    "x": 6.3, 
                    "y": 0.2
                }, 
                "beersLawLab.beersLawScreen.model.detector.modeProperty": "absorbance", 
                "beersLawLab.beersLawScreen.model.detector.probe.locationProperty": {
                    "x": 6.3, 
                    "y": 2
                }, 
                "beersLawLab.beersLawScreen.model.detector.valueProperty": null, 
                "beersLawLab.beersLawScreen.model.light.onProperty": false, 
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
        "time": 1490208080496
    }, 
    "event": "phetio.state", 
    "index": 4, 
    "timestamp": 1490208080304, 
    "type": "model"
}
''') 

updating_state_event_parsed = True
updating_state_event_user_or_model = 'model'
updating_state_event_simevent = 'updating state'
updating_state_event_item = ''
updating_state_event_action = ''

#####################################################################################################################
toggle_laser_event = json.loads(''' {
    "data": {
        "children": [
            {
                "children": [
                    {
                        "children": [
                            {
                                "componentType": "TTandemText", 
                                "event": "textChanged", 
                                "eventType": "model", 
                                "messageIndex": 2172, 
                                "parameters": {
                                    "newText": "0.96", 
                                    "oldText": "-"
                                }, 
                                "phetioID": "beersLawLab.beersLawScreen.view.detectorNode.bodyNode.valueNode", 
                                "time": 1490208110314
                            }
                        ], 
                        "componentType": "TDerivedProperty", 
                        "event": "changed", 
                        "eventType": "model", 
                        "messageIndex": 2171, 
                        "parameters": {
                            "newValue": 0.961, 
                            "oldValue": null
                        }, 
                        "phetioID": "beersLawLab.beersLawScreen.model.detector.valueProperty", 
                        "time": 1490208110314
                    }
                ], 
                "componentType": "TProperty", 
                "event": "changed", 
                "eventType": "model", 
                "messageIndex": 2170, 
                "parameters": {
                    "newValue": true, 
                    "oldValue": false
                }, 
                "phetioID": "beersLawLab.beersLawScreen.model.light.onProperty", 
                "time": 1490208110312
            }
        ], 
        "componentType": "TToggleButton", 
        "event": "toggled", 
        "eventType": "user", 
        "messageIndex": 2169, 
        "parameters": {
            "newValue": true, 
            "oldValue": false
        }, 
        "phetioID": "beersLawLab.beersLawScreen.view.lightNode.button", 
        "time": 1490208110312
    }, 
    "event": "beersLawLab.beersLawScreen.view.lightNode.button.toggled", 
    "index": 2166, 
    "timestamp": 1490208110112, 
    "type": "model"
}
''') 

toggle_laser_event_parsed = True
toggle_laser_event_user_or_model = 'user'
toggle_laser_event_simevent = 'toggle laser'
toggle_laser_event_item = 'laser button'
toggle_laser_event_action = ''

#####################################################################################################################
dragStarted_event = json.loads(''' {
    "data": {
        "componentType": "TTandemDragHandler", 
        "event": "dragStarted", 
        "eventType": "user", 
        "messageIndex": 3316, 
        "parameters": {
            "x": 454, 
            "y": 174
        }, 
        "phetioID": "beersLawLab.beersLawScreen.view.detectorNode.probeNode.movableDragHandler", 
        "time": 1490208116663
    }, 
    "event": "beersLawLab.beersLawScreen.view.detectorNode.probeNode.movableDragHandler.dragStarted", 
    "index": 3310, 
    "timestamp": 1490208116439, 
    "type": "model"
}
''') 

dragStarted_event_parsed = True
dragStarted_event_user_or_model = 'user'
dragStarted_event_simevent = 'dragStarted'
dragStarted_event_item = 'detectorNode'
dragStarted_event_action = ''

#####################################################################################################################
dragged_event = json.loads(''' {
    "data": {
        "children": [
            {
                "componentType": "TProperty", 
                "event": "changed", 
                "eventType": "model", 
                "messageIndex": 3326, 
                "parameters": {
                    "newValue": {
                        "x": 6.271034482758621, 
                        "y": 2
                    }, 
                    "oldValue": {
                        "x": 6.3, 
                        "y": 2
                    }
                }, 
                "phetioID": "beersLawLab.beersLawScreen.model.detector.probe.locationProperty", 
                "time": 1490208116768
            }
        ], 
        "componentType": "TTandemDragHandler", 
        "event": "dragged", 
        "eventType": "user", 
        "messageIndex": 3325, 
        "parameters": {
            "x": 452, 
            "y": 174
        }, 
        "phetioID": "beersLawLab.beersLawScreen.view.detectorNode.probeNode.movableDragHandler", 
        "time": 1490208116767
    }, 
    "event": "beersLawLab.beersLawScreen.view.detectorNode.probeNode.movableDragHandler.dragged", 
    "index": 3319, 
    "timestamp": 1490208116547, 
    "type": "model"
}
''') 

dragged_event_parsed = True
dragged_event_user_or_model = 'user'
dragged_event_simevent = 'dragged'
dragged_event_item = 'detectorNode'
dragged_event_action = 'decreasing'

#####################################################################################################################
dragEnded_event = json.loads(''' {
    "data": {
        "children": [
            {
                "children": [
                    {
                        "children": [
                            {
                                "componentType": "TTandemText", 
                                "event": "textChanged", 
                                "eventType": "model", 
                                "messageIndex": 4950, 
                                "parameters": {
                                    "newText": "0.96", 
                                    "oldText": "-"
                                }, 
                                "phetioID": "beersLawLab.beersLawScreen.view.detectorNode.bodyNode.valueNode", 
                                "time": 1490208123774
                            }
                        ], 
                        "componentType": "TDerivedProperty", 
                        "event": "changed", 
                        "eventType": "model", 
                        "messageIndex": 4949, 
                        "parameters": {
                            "newValue": 0.961, 
                            "oldValue": null
                        }, 
                        "phetioID": "beersLawLab.beersLawScreen.model.detector.valueProperty", 
                        "time": 1490208123774
                    }
                ], 
                "componentType": "TProperty", 
                "event": "changed", 
                "eventType": "model", 
                "messageIndex": 4948, 
                "parameters": {
                    "newValue": {
                        "x": 5.083448275862069, 
                        "y": 2
                    }, 
                    "oldValue": {
                        "x": 5.083448275862069, 
                        "y": 2.1448275862068966
                    }
                }, 
                "phetioID": "beersLawLab.beersLawScreen.model.detector.probe.locationProperty", 
                "time": 1490208123774
            }
        ], 
        "componentType": "TTandemDragHandler", 
        "event": "dragEnded", 
        "eventType": "user", 
        "messageIndex": 4947, 
        "phetioID": "beersLawLab.beersLawScreen.view.detectorNode.probeNode.movableDragHandler", 
        "time": 1490208123774
    }, 
    "event": "beersLawLab.beersLawScreen.view.detectorNode.probeNode.movableDragHandler.dragEnded", 
    "index": 4660, 
    "timestamp": 1490208123553, 
    "type": "model"
}
''') 

dragEnded_event_parsed = True
dragEnded_event_user_or_model = 'user'
dragEnded_event_simevent = 'dragEnded'
dragEnded_event_item = 'detectorNode'
dragEnded_event_action = ''

#####################################################################################################################
expanding_table_event = json.loads(''' {
    "data": {
        "children": [
            {
                "componentType": "TButton", 
                "event": "pressed", 
                "eventType": "user", 
                "messageIndex": 22262, 
                "phetioID": "labBook.tableExpandButton", 
                "time": 1490208332454
            }
        ], 
        "componentType": "TSimIFrameAPI", 
        "event": "invoked", 
        "eventType": "wrapper", 
        "messageIndex": 22261, 
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
                    "phetioID": "labBook.tableExpandButton"
                }
            ], 
            "messageID": 5, 
            "method": "triggerEvent", 
            "phetioID": "phetio", 
            "protocol": "phet-io-0.0.1"
        }, 
        "phetioID": "beersLawLab.simIFrameAPI", 
        "time": 1490208332454
    }, 
    "event": "beersLawLab.simIFrameAPI.invoked", 
    "index": 20967, 
    "timestamp": 1490208332230, 
    "type": "model"
}
''') 

expanding_table_event_parsed = True
expanding_table_event_user_or_model = 'user'
expanding_table_event_simevent = 'expanding table'
expanding_table_event_item = 'table'
expanding_table_event_action = ''

#####################################################################################################################
Changed_concentration_event = json.loads(''' {
    "data": {
        "children": [
            {
                "children": [
                    {
                        "children": [
                            {
                                "componentType": "TTandemText", 
                                "event": "textChanged", 
                                "eventType": "model", 
                                "messageIndex": 25203, 
                                "parameters": {
                                    "newText": "0.96", 
                                    "oldText": "0.95"
                                }, 
                                "phetioID": "beersLawLab.beersLawScreen.view.detectorNode.bodyNode.valueNode", 
                                "time": 1490208357158
                            }
                        ], 
                        "componentType": "TDerivedProperty", 
                        "event": "changed", 
                        "eventType": "model", 
                        "messageIndex": 25202, 
                        "parameters": {
                            "newValue": 0.9637397752721223, 
                            "oldValue": 0.9538991352721223
                        }, 
                        "phetioID": "beersLawLab.beersLawScreen.model.detector.valueProperty", 
                        "time": 1490208357158
                    }
                ], 
                "componentType": "TProperty", 
                "event": "changed", 
                "eventType": "model", 
                "messageIndex": 25201, 
                "parameters": {
                    "newValue": 0.09793466433810426, 
                    "oldValue": 0.09693466433810426
                }, 
                "phetioID": "beersLawLab.beersLawScreen.solutions.copperSulfate.concentrationProperty", 
                "time": 1490208357158
            }
        ], 
        "componentType": "TPushButton", 
        "event": "fired", 
        "eventType": "user", 
        "messageIndex": 25200, 
        "phetioID": "beersLawLab.beersLawScreen.view.solutionControls.concentrationControl.slider.plusButton", 
        "time": 1490208357158
    }, 
    "event": "beersLawLab.beersLawScreen.view.solutionControls.concentrationControl.slider.plusButton.fired", 
    "index": 23701, 
    "timestamp": 1490208356948, 
    "type": "model"
}
''') 

Changed_concentration_event_parsed = True
Changed_concentration_event_user_or_model = 'user'
Changed_concentration_event_simevent = 'Changed concentration'
Changed_concentration_event_item = 'concentration slider'
Changed_concentration_event_action = 'Pressed increment button'

#####################################################################################################################
gettingValues_event = json.loads(''' {
    "data": {
        "componentType": "TSimIFrameAPI", 
        "event": "invoked", 
        "eventType": "wrapper", 
        "messageIndex": 27349, 
        "parameters": {
            "messageID": 6, 
            "messages": [
                {
                    "messageID": 6, 
                    "method": "getValue", 
                    "phetioID": "beersLawLab.beersLawScreen.model.light.wavelengthProperty", 
                    "protocol": "phet-io-0.0.1"
                }, 
                {
                    "messageID": 6, 
                    "method": "getValue", 
                    "phetioID": "beersLawLab.beersLawScreen.model.cuvette.widthProperty", 
                    "protocol": "phet-io-0.0.1"
                }, 
                {
                    "messageID": 6, 
                    "method": "getValue", 
                    "phetioID": "beersLawLab.beersLawScreen.model.solutionProperty", 
                    "protocol": "phet-io-0.0.1"
                }, 
                {
                    "messageID": 6, 
                    "method": "getValue", 
                    "phetioID": "beersLawLab.beersLawScreen.model.detector.valueProperty", 
                    "protocol": "phet-io-0.0.1"
                }, 
                {
                    "messageID": 6, 
                    "method": "getValue", 
                    "phetioID": "beersLawLab.beersLawScreen.model.light.onProperty", 
                    "protocol": "phet-io-0.0.1"
                }, 
                {
                    "messageID": 6, 
                    "method": "getScreenshotDataURL", 
                    "phetioID": "beersLawLab.sim", 
                    "protocol": "phet-io-0.0.1"
                }, 
                {
                    "messageID": 6, 
                    "method": "getState", 
                    "phetioID": "phetio", 
                    "protocol": "phet-io-0.0.1"
                }
            ], 
            "protocol": "phet-io-0.0.1"
        }, 
        "phetioID": "beersLawLab.simIFrameAPI", 
        "time": 1490208371506
    }, 
    "event": "beersLawLab.simIFrameAPI.invoked", 
    "index": 25629, 
    "timestamp": 1490208371345, 
    "type": "model"
}
''') 

gettingValues_event_parsed = True
gettingValues_event_user_or_model = 'model'
gettingValues_event_simevent = 'gettingValues'
gettingValues_event_item = 'sim'
gettingValues_event_action = ''

#####################################################################################################################
recording_data_event = json.loads(''' {
    "data": {
        "children": [
            {
                "componentType": "TButton", 
                "event": "pressed", 
                "eventType": "user", 
                "messageIndex": 27353, 
                "parameters": {
                    "absorbance": 0.14428966575792845, 
                    "absorbance_x": 0.14428966575792845, 
                    "absorbance_y": 0.14428966575792845, 
                    "concentration": 99.93466433810426, 
                    "concentration_x": 99.93466433810426, 
                    "concentration_y": 99.93466433810426, 
                    "cuvetteWidth": 1.024, 
                    "cuvetteWidth_x": 1.024, 
                    "cuvetteWidth_y": 1.024, 
                    "image": {}, 
                    "state": {
                        "beersLawLab.beersLawScreen.model.cuvette.widthProperty": 1.024, 
                        "beersLawLab.beersLawScreen.model.detector.body.locationProperty": {
                            "x": 6.3, 
                            "y": 0.2
                        }, 
                        "beersLawLab.beersLawScreen.model.detector.modeProperty": "absorbance", 
                        "beersLawLab.beersLawScreen.model.detector.probe.locationProperty": {
                            "x": 6.633103448275862, 
                            "y": 2
                        }, 
                        "beersLawLab.beersLawScreen.model.detector.valueProperty": 0.14428966575792845, 
                        "beersLawLab.beersLawScreen.model.light.onProperty": true, 
                        "beersLawLab.beersLawScreen.model.light.wavelengthProperty": 659, 
                        "beersLawLab.beersLawScreen.model.ruler.locationProperty": {
                            "x": 3.3, 
                            "y": 3.58
                        }, 
                        "beersLawLab.beersLawScreen.model.solutionProperty": "beersLawLab.beersLawScreen.solutions.copperSulfate", 
                        "beersLawLab.beersLawScreen.solutions.cobaltChloride.concentrationProperty": 0.1, 
                        "beersLawLab.beersLawScreen.solutions.cobaltIINitrate.concentrationProperty": 0.1, 
                        "beersLawLab.beersLawScreen.solutions.copperSulfate.concentrationProperty": 0.09993466433810426, 
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
                    "wavelength": 659, 
                    "wavelength_x": 659, 
                    "wavelength_y": 659
                }, 
                "phetioID": "labBook.recordDataButton", 
                "time": 1490208371584
            }
        ], 
        "componentType": "TSimIFrameAPI", 
        "event": "invoked", 
        "eventType": "wrapper", 
        "messageIndex": 27352, 
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
                        "absorbance": 0.14428966575792845, 
                        "absorbance_x": 0.14428966575792845, 
                        "absorbance_y": 0.14428966575792845, 
                        "concentration": 99.93466433810426, 
                        "concentration_x": 99.93466433810426, 
                        "concentration_y": 99.93466433810426, 
                        "cuvetteWidth": 1.024, 
                        "cuvetteWidth_x": 1.024, 
                        "cuvetteWidth_y": 1.024, 
                        "image": {}, 
                        "state": {
                            "beersLawLab.beersLawScreen.model.cuvette.widthProperty": 1.024, 
                            "beersLawLab.beersLawScreen.model.detector.body.locationProperty": {
                                "x": 6.3, 
                                "y": 0.2
                            }, 
                            "beersLawLab.beersLawScreen.model.detector.modeProperty": "absorbance", 
                            "beersLawLab.beersLawScreen.model.detector.probe.locationProperty": {
                                "x": 6.633103448275862, 
                                "y": 2
                            }, 
                            "beersLawLab.beersLawScreen.model.detector.valueProperty": 0.14428966575792845, 
                            "beersLawLab.beersLawScreen.model.light.onProperty": true, 
                            "beersLawLab.beersLawScreen.model.light.wavelengthProperty": 659, 
                            "beersLawLab.beersLawScreen.model.ruler.locationProperty": {
                                "x": 3.3, 
                                "y": 3.58
                            }, 
                            "beersLawLab.beersLawScreen.model.solutionProperty": "beersLawLab.beersLawScreen.solutions.copperSulfate", 
                            "beersLawLab.beersLawScreen.solutions.cobaltChloride.concentrationProperty": 0.1, 
                            "beersLawLab.beersLawScreen.solutions.cobaltIINitrate.concentrationProperty": 0.1, 
                            "beersLawLab.beersLawScreen.solutions.copperSulfate.concentrationProperty": 0.09993466433810426, 
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
                        "wavelength": 659, 
                        "wavelength_x": 659, 
                        "wavelength_y": 659
                    }, 
                    "phetioID": "labBook.recordDataButton"
                }
            ], 
            "messageID": 7, 
            "method": "triggerEvent", 
            "phetioID": "phetio", 
            "protocol": "phet-io-0.0.1"
        }, 
        "phetioID": "beersLawLab.simIFrameAPI", 
        "time": 1490208371583
    }, 
    "event": "beersLawLab.simIFrameAPI.invoked", 
    "index": 25632, 
    "timestamp": 1490208371371, 
    "type": "model"
}
''') 

recording_data_event_parsed = True
recording_data_event_user_or_model = 'user'
recording_data_event_simevent = 'recording data'
recording_data_event_item = ''
recording_data_event_action = ''

#####################################################################################################################
expanding_graph_event = json.loads(''' {
    "data": {
        "children": [
            {
                "componentType": "TButton", 
                "event": "pressed", 
                "eventType": "user", 
                "messageIndex": 42258, 
                "phetioID": "labBook.graphExpandButton", 
                "time": 1490208578689
            }
        ], 
        "componentType": "TSimIFrameAPI", 
        "event": "invoked", 
        "eventType": "wrapper", 
        "messageIndex": 42257, 
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
                    "phetioID": "labBook.graphExpandButton"
                }
            ], 
            "messageID": 448, 
            "method": "triggerEvent", 
            "phetioID": "phetio", 
            "protocol": "phet-io-0.0.1"
        }, 
        "phetioID": "beersLawLab.simIFrameAPI", 
        "time": 1490208578688
    }, 
    "event": "beersLawLab.simIFrameAPI.invoked", 
    "index": 39874, 
    "timestamp": 1490208578464, 
    "type": "model"
}
''') 

expanding_graph_event_parsed = True
expanding_graph_event_user_or_model = 'user'
expanding_graph_event_simevent = 'expanding graph'
expanding_graph_event_item = 'graph'
expanding_graph_event_action = ''

#####################################################################################################################
collapsing_graph_event = json.loads(''' {
    "data": {
        "children": [
            {
                "componentType": "TButton", 
                "event": "pressed", 
                "eventType": "user", 
                "messageIndex": 48448, 
                "phetioID": "labBook.graphCollapseButton", 
                "time": 1490208628155
            }
        ], 
        "componentType": "TSimIFrameAPI", 
        "event": "invoked", 
        "eventType": "wrapper", 
        "messageIndex": 48447, 
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
                    "phetioID": "labBook.graphCollapseButton"
                }
            ], 
            "messageID": 458, 
            "method": "triggerEvent", 
            "phetioID": "phetio", 
            "protocol": "phet-io-0.0.1"
        }, 
        "phetioID": "beersLawLab.simIFrameAPI", 
        "time": 1490208628154
    }, 
    "event": "beersLawLab.simIFrameAPI.invoked", 
    "index": 45500, 
    "timestamp": 1490208627930, 
    "type": "model"
}
''') 

collapsing_graph_event_parsed = True
collapsing_graph_event_user_or_model = 'user'
collapsing_graph_event_simevent = 'collapsing graph'
collapsing_graph_event_item = 'graph'
collapsing_graph_event_action = ''

#####################################################################################################################
Restoring_sim_state_event = json.loads(''' {
    "data": {
        "children": [
            {
                "componentType": "TButton", 
                "event": "pressed", 
                "eventType": "user", 
                "messageIndex": 51191, 
                "parameters": {
                    "userData": [
                        {
                            "absorbance": 0.14428966575792845, 
                            "absorbance_x": 0.14428966575792845, 
                            "absorbance_y": 0.14428966575792845, 
                            "concentration": 99.93466433810426, 
                            "concentration_x": 99.93466433810426, 
                            "concentration_y": 99.93466433810426, 
                            "cuvetteWidth": 1.024, 
                            "cuvetteWidth_x": 1.024, 
                            "cuvetteWidth_y": 1.024, 
                            "image": {}, 
                            "state": {
                                "beersLawLab.beersLawScreen.model.cuvette.widthProperty": 1.024, 
                                "beersLawLab.beersLawScreen.model.detector.body.locationProperty": {
                                    "x": 6.3, 
                                    "y": 0.2
                                }, 
                                "beersLawLab.beersLawScreen.model.detector.modeProperty": "absorbance", 
                                "beersLawLab.beersLawScreen.model.detector.probe.locationProperty": {
                                    "x": 6.633103448275862, 
                                    "y": 2
                                }, 
                                "beersLawLab.beersLawScreen.model.detector.valueProperty": 0.14428966575792845, 
                                "beersLawLab.beersLawScreen.model.light.onProperty": true, 
                                "beersLawLab.beersLawScreen.model.light.wavelengthProperty": 659, 
                                "beersLawLab.beersLawScreen.model.ruler.locationProperty": {
                                    "x": 3.3, 
                                    "y": 3.58
                                }, 
                                "beersLawLab.beersLawScreen.model.solutionProperty": "beersLawLab.beersLawScreen.solutions.copperSulfate", 
                                "beersLawLab.beersLawScreen.solutions.cobaltChloride.concentrationProperty": 0.1, 
                                "beersLawLab.beersLawScreen.solutions.cobaltIINitrate.concentrationProperty": 0.1, 
                                "beersLawLab.beersLawScreen.solutions.copperSulfate.concentrationProperty": 0.09993466433810426, 
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
                            "wavelength": 659, 
                            "wavelength_x": 659, 
                            "wavelength_y": 659
                        }, 
                        {
                            "absorbance": 0.281815753433454, 
                            "absorbance_x": 0.281815753433454, 
                            "absorbance_y": 0.281815753433454, 
                            "concentration": 99.93466433810426, 
                            "concentration_x": 99.93466433810426, 
                            "concentration_y": 99.93466433810426, 
                            "cuvetteWidth": 2, 
                            "cuvetteWidth_x": 2, 
                            "cuvetteWidth_y": 2, 
                            "image": {}, 
                            "state": {
                                "beersLawLab.beersLawScreen.model.cuvette.widthProperty": 2, 
                                "beersLawLab.beersLawScreen.model.detector.body.locationProperty": {
                                    "x": 6.3, 
                                    "y": 0.2
                                }, 
                                "beersLawLab.beersLawScreen.model.detector.modeProperty": "absorbance", 
                                "beersLawLab.beersLawScreen.model.detector.probe.locationProperty": {
                                    "x": 6.633103448275862, 
                                    "y": 2
                                }, 
                                "beersLawLab.beersLawScreen.model.detector.valueProperty": 0.281815753433454, 
                                "beersLawLab.beersLawScreen.model.light.onProperty": true, 
                                "beersLawLab.beersLawScreen.model.light.wavelengthProperty": 659, 
                                "beersLawLab.beersLawScreen.model.ruler.locationProperty": {
                                    "x": 3.3, 
                                    "y": 3.58
                                }, 
                                "beersLawLab.beersLawScreen.model.solutionProperty": "beersLawLab.beersLawScreen.solutions.copperSulfate", 
                                "beersLawLab.beersLawScreen.solutions.cobaltChloride.concentrationProperty": 0.1, 
                                "beersLawLab.beersLawScreen.solutions.cobaltIINitrate.concentrationProperty": 0.1, 
                                "beersLawLab.beersLawScreen.solutions.copperSulfate.concentrationProperty": 0.09993466433810426, 
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
                            "trialNumber": 2, 
                            "trialNumber_x": 2, 
                            "trialNumber_y": 2, 
                            "visible": false, 
                            "wavelength": 659, 
                            "wavelength_x": 659, 
                            "wavelength_y": 659
                        }, 
                        {
                            "absorbance": 0.564, 
                            "absorbance_x": 0.564, 
                            "absorbance_y": 0.564, 
                            "concentration": 200, 
                            "concentration_x": 200, 
                            "concentration_y": 200, 
                            "cuvetteWidth": 2, 
                            "cuvetteWidth_x": 2, 
                            "cuvetteWidth_y": 2, 
                            "image": {}, 
                            "state": {
                                "beersLawLab.beersLawScreen.model.cuvette.widthProperty": 2, 
                                "beersLawLab.beersLawScreen.model.detector.body.locationProperty": {
                                    "x": 6.3, 
                                    "y": 0.2
                                }, 
                                "beersLawLab.beersLawScreen.model.detector.modeProperty": "absorbance", 
                                "beersLawLab.beersLawScreen.model.detector.probe.locationProperty": {
                                    "x": 6.633103448275862, 
                                    "y": 2
                                }, 
                                "beersLawLab.beersLawScreen.model.detector.valueProperty": 0.564, 
                                "beersLawLab.beersLawScreen.model.light.onProperty": true, 
                                "beersLawLab.beersLawScreen.model.light.wavelengthProperty": 659, 
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
                            "trialNumber": 3, 
                            "trialNumber_x": 3, 
                            "trialNumber_y": 3, 
                            "visible": false, 
                            "wavelength": 659, 
                            "wavelength_x": 659, 
                            "wavelength_y": 659
                        }, 
                        {
                            "absorbance": 0.07080387931034482, 
                            "absorbance_x": 0.07080387931034482, 
                            "absorbance_y": 0.07080387931034482, 
                            "concentration": 100.43103448275862, 
                            "concentration_x": 100.43103448275862, 
                            "concentration_y": 100.43103448275862, 
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
                                    "x": 6.633103448275862, 
                                    "y": 2
                                }, 
                                "beersLawLab.beersLawScreen.model.detector.valueProperty": 0.07080387931034482, 
                                "beersLawLab.beersLawScreen.model.light.onProperty": true, 
                                "beersLawLab.beersLawScreen.model.light.wavelengthProperty": 659, 
                                "beersLawLab.beersLawScreen.model.ruler.locationProperty": {
                                    "x": 3.2920000000000003, 
                                    "y": 3.596
                                }, 
                                "beersLawLab.beersLawScreen.model.solutionProperty": "beersLawLab.beersLawScreen.solutions.copperSulfate", 
                                "beersLawLab.beersLawScreen.solutions.cobaltChloride.concentrationProperty": 0.1, 
                                "beersLawLab.beersLawScreen.solutions.cobaltIINitrate.concentrationProperty": 0.1, 
                                "beersLawLab.beersLawScreen.solutions.copperSulfate.concentrationProperty": 0.10043103448275861, 
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
                            "trialNumber": 4, 
                            "trialNumber_x": 4, 
                            "trialNumber_y": 4, 
                            "visible": false, 
                            "wavelength": 659, 
                            "wavelength_x": 659, 
                            "wavelength_y": 659
                        }, 
                        {
                            "absorbance": 0.1421741896551724, 
                            "absorbance_x": 0.1421741896551724, 
                            "absorbance_y": 0.1421741896551724, 
                            "concentration": 100.43103448275862, 
                            "concentration_x": 100.43103448275862, 
                            "concentration_y": 100.43103448275862, 
                            "cuvetteWidth": 1.004, 
                            "cuvetteWidth_x": 1.004, 
                            "cuvetteWidth_y": 1.004, 
                            "image": {}, 
                            "state": {
                                "beersLawLab.beersLawScreen.model.cuvette.widthProperty": 1.004, 
                                "beersLawLab.beersLawScreen.model.detector.body.locationProperty": {
                                    "x": 6.3, 
                                    "y": 0.2
                                }, 
                                "beersLawLab.beersLawScreen.model.detector.modeProperty": "absorbance", 
                                "beersLawLab.beersLawScreen.model.detector.probe.locationProperty": {
                                    "x": 6.633103448275862, 
                                    "y": 2
                                }, 
                                "beersLawLab.beersLawScreen.model.detector.valueProperty": 0.1421741896551724, 
                                "beersLawLab.beersLawScreen.model.light.onProperty": true, 
                                "beersLawLab.beersLawScreen.model.light.wavelengthProperty": 659, 
                                "beersLawLab.beersLawScreen.model.ruler.locationProperty": {
                                    "x": 3.2920000000000003, 
                                    "y": 3.596
                                }, 
                                "beersLawLab.beersLawScreen.model.solutionProperty": "beersLawLab.beersLawScreen.solutions.copperSulfate", 
                                "beersLawLab.beersLawScreen.solutions.cobaltChloride.concentrationProperty": 0.1, 
                                "beersLawLab.beersLawScreen.solutions.cobaltIINitrate.concentrationProperty": 0.1, 
                                "beersLawLab.beersLawScreen.solutions.copperSulfate.concentrationProperty": 0.10043103448275861, 
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
                            "trialNumber": 5, 
                            "trialNumber_x": 5, 
                            "trialNumber_y": 5, 
                            "visible": false, 
                            "wavelength": 659, 
                            "wavelength_x": 659, 
                            "wavelength_y": 659
                        }, 
                        {
                            "absorbance": 0.2101459137931034, 
                            "absorbance_x": 0.2101459137931034, 
                            "absorbance_y": 0.2101459137931034, 
                            "concentration": 100.43103448275862, 
                            "concentration_x": 100.43103448275862, 
                            "concentration_y": 100.43103448275862, 
                            "cuvetteWidth": 1.484, 
                            "cuvetteWidth_x": 1.484, 
                            "cuvetteWidth_y": 1.484, 
                            "image": {}, 
                            "state": {
                                "beersLawLab.beersLawScreen.model.cuvette.widthProperty": 1.484, 
                                "beersLawLab.beersLawScreen.model.detector.body.locationProperty": {
                                    "x": 6.3, 
                                    "y": 0.2
                                }, 
                                "beersLawLab.beersLawScreen.model.detector.modeProperty": "absorbance", 
                                "beersLawLab.beersLawScreen.model.detector.probe.locationProperty": {
                                    "x": 6.633103448275862, 
                                    "y": 2
                                }, 
                                "beersLawLab.beersLawScreen.model.detector.valueProperty": 0.2101459137931034, 
                                "beersLawLab.beersLawScreen.model.light.onProperty": true, 
                                "beersLawLab.beersLawScreen.model.light.wavelengthProperty": 659, 
                                "beersLawLab.beersLawScreen.model.ruler.locationProperty": {
                                    "x": 3.2920000000000003, 
                                    "y": 3.596
                                }, 
                                "beersLawLab.beersLawScreen.model.solutionProperty": "beersLawLab.beersLawScreen.solutions.copperSulfate", 
                                "beersLawLab.beersLawScreen.solutions.cobaltChloride.concentrationProperty": 0.1, 
                                "beersLawLab.beersLawScreen.solutions.cobaltIINitrate.concentrationProperty": 0.1, 
                                "beersLawLab.beersLawScreen.solutions.copperSulfate.concentrationProperty": 0.10043103448275861, 
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
                            "trialNumber": 6, 
                            "trialNumber_x": 6, 
                            "trialNumber_y": 6, 
                            "visible": false, 
                            "wavelength": 659, 
                            "wavelength_x": 659, 
                            "wavelength_y": 659
                        }, 
                        {
                            "absorbance": 0.2832155172413793, 
                            "absorbance_x": 0.2832155172413793, 
                            "absorbance_y": 0.2832155172413793, 
                            "concentration": 100.43103448275862, 
                            "concentration_x": 100.43103448275862, 
                            "concentration_y": 100.43103448275862, 
                            "cuvetteWidth": 2, 
                            "cuvetteWidth_x": 2, 
                            "cuvetteWidth_y": 2, 
                            "image": {}, 
                            "state": {
                                "beersLawLab.beersLawScreen.model.cuvette.widthProperty": 2, 
                                "beersLawLab.beersLawScreen.model.detector.body.locationProperty": {
                                    "x": 6.3, 
                                    "y": 0.2
                                }, 
                                "beersLawLab.beersLawScreen.model.detector.modeProperty": "absorbance", 
                                "beersLawLab.beersLawScreen.model.detector.probe.locationProperty": {
                                    "x": 6.633103448275862, 
                                    "y": 2
                                }, 
                                "beersLawLab.beersLawScreen.model.detector.valueProperty": 0.2832155172413793, 
                                "beersLawLab.beersLawScreen.model.light.onProperty": true, 
                                "beersLawLab.beersLawScreen.model.light.wavelengthProperty": 659, 
                                "beersLawLab.beersLawScreen.model.ruler.locationProperty": {
                                    "x": 3.2920000000000003, 
                                    "y": 3.596
                                }, 
                                "beersLawLab.beersLawScreen.model.solutionProperty": "beersLawLab.beersLawScreen.solutions.copperSulfate", 
                                "beersLawLab.beersLawScreen.solutions.cobaltChloride.concentrationProperty": 0.1, 
                                "beersLawLab.beersLawScreen.solutions.cobaltIINitrate.concentrationProperty": 0.1, 
                                "beersLawLab.beersLawScreen.solutions.copperSulfate.concentrationProperty": 0.10043103448275861, 
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
                            "trialNumber": 7, 
                            "trialNumber_x": 7, 
                            "trialNumber_y": 7, 
                            "visible": false, 
                            "wavelength": 659, 
                            "wavelength_x": 659, 
                            "wavelength_y": 659
                        }
                    ]
                }, 
                "phetioID": "labBook.restoreButton4", 
                "time": 1490208674091
            }
        ], 
        "componentType": "TSimIFrameAPI", 
        "event": "invoked", 
        "eventType": "wrapper", 
        "messageIndex": 51190, 
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
                        "userData": [
                            {
                                "absorbance": 0.14428966575792845, 
                                "absorbance_x": 0.14428966575792845, 
                                "absorbance_y": 0.14428966575792845, 
                                "concentration": 99.93466433810426, 
                                "concentration_x": 99.93466433810426, 
                                "concentration_y": 99.93466433810426, 
                                "cuvetteWidth": 1.024, 
                                "cuvetteWidth_x": 1.024, 
                                "cuvetteWidth_y": 1.024, 
                                "image": {}, 
                                "state": {
                                    "beersLawLab.beersLawScreen.model.cuvette.widthProperty": 1.024, 
                                    "beersLawLab.beersLawScreen.model.detector.body.locationProperty": {
                                        "x": 6.3, 
                                        "y": 0.2
                                    }, 
                                    "beersLawLab.beersLawScreen.model.detector.modeProperty": "absorbance", 
                                    "beersLawLab.beersLawScreen.model.detector.probe.locationProperty": {
                                        "x": 6.633103448275862, 
                                        "y": 2
                                    }, 
                                    "beersLawLab.beersLawScreen.model.detector.valueProperty": 0.14428966575792845, 
                                    "beersLawLab.beersLawScreen.model.light.onProperty": true, 
                                    "beersLawLab.beersLawScreen.model.light.wavelengthProperty": 659, 
                                    "beersLawLab.beersLawScreen.model.ruler.locationProperty": {
                                        "x": 3.3, 
                                        "y": 3.58
                                    }, 
                                    "beersLawLab.beersLawScreen.model.solutionProperty": "beersLawLab.beersLawScreen.solutions.copperSulfate", 
                                    "beersLawLab.beersLawScreen.solutions.cobaltChloride.concentrationProperty": 0.1, 
                                    "beersLawLab.beersLawScreen.solutions.cobaltIINitrate.concentrationProperty": 0.1, 
                                    "beersLawLab.beersLawScreen.solutions.copperSulfate.concentrationProperty": 0.09993466433810426, 
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
                                "wavelength": 659, 
                                "wavelength_x": 659, 
                                "wavelength_y": 659
                            }, 
                            {
                                "absorbance": 0.281815753433454, 
                                "absorbance_x": 0.281815753433454, 
                                "absorbance_y": 0.281815753433454, 
                                "concentration": 99.93466433810426, 
                                "concentration_x": 99.93466433810426, 
                                "concentration_y": 99.93466433810426, 
                                "cuvetteWidth": 2, 
                                "cuvetteWidth_x": 2, 
                                "cuvetteWidth_y": 2, 
                                "image": {}, 
                                "state": {
                                    "beersLawLab.beersLawScreen.model.cuvette.widthProperty": 2, 
                                    "beersLawLab.beersLawScreen.model.detector.body.locationProperty": {
                                        "x": 6.3, 
                                        "y": 0.2
                                    }, 
                                    "beersLawLab.beersLawScreen.model.detector.modeProperty": "absorbance", 
                                    "beersLawLab.beersLawScreen.model.detector.probe.locationProperty": {
                                        "x": 6.633103448275862, 
                                        "y": 2
                                    }, 
                                    "beersLawLab.beersLawScreen.model.detector.valueProperty": 0.281815753433454, 
                                    "beersLawLab.beersLawScreen.model.light.onProperty": true, 
                                    "beersLawLab.beersLawScreen.model.light.wavelengthProperty": 659, 
                                    "beersLawLab.beersLawScreen.model.ruler.locationProperty": {
                                        "x": 3.3, 
                                        "y": 3.58
                                    }, 
                                    "beersLawLab.beersLawScreen.model.solutionProperty": "beersLawLab.beersLawScreen.solutions.copperSulfate", 
                                    "beersLawLab.beersLawScreen.solutions.cobaltChloride.concentrationProperty": 0.1, 
                                    "beersLawLab.beersLawScreen.solutions.cobaltIINitrate.concentrationProperty": 0.1, 
                                    "beersLawLab.beersLawScreen.solutions.copperSulfate.concentrationProperty": 0.09993466433810426, 
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
                                "trialNumber": 2, 
                                "trialNumber_x": 2, 
                                "trialNumber_y": 2, 
                                "visible": false, 
                                "wavelength": 659, 
                                "wavelength_x": 659, 
                                "wavelength_y": 659
                            }, 
                            {
                                "absorbance": 0.564, 
                                "absorbance_x": 0.564, 
                                "absorbance_y": 0.564, 
                                "concentration": 200, 
                                "concentration_x": 200, 
                                "concentration_y": 200, 
                                "cuvetteWidth": 2, 
                                "cuvetteWidth_x": 2, 
                                "cuvetteWidth_y": 2, 
                                "image": {}, 
                                "state": {
                                    "beersLawLab.beersLawScreen.model.cuvette.widthProperty": 2, 
                                    "beersLawLab.beersLawScreen.model.detector.body.locationProperty": {
                                        "x": 6.3, 
                                        "y": 0.2
                                    }, 
                                    "beersLawLab.beersLawScreen.model.detector.modeProperty": "absorbance", 
                                    "beersLawLab.beersLawScreen.model.detector.probe.locationProperty": {
                                        "x": 6.633103448275862, 
                                        "y": 2
                                    }, 
                                    "beersLawLab.beersLawScreen.model.detector.valueProperty": 0.564, 
                                    "beersLawLab.beersLawScreen.model.light.onProperty": true, 
                                    "beersLawLab.beersLawScreen.model.light.wavelengthProperty": 659, 
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
                                "trialNumber": 3, 
                                "trialNumber_x": 3, 
                                "trialNumber_y": 3, 
                                "visible": false, 
                                "wavelength": 659, 
                                "wavelength_x": 659, 
                                "wavelength_y": 659
                            }, 
                            {
                                "absorbance": 0.07080387931034482, 
                                "absorbance_x": 0.07080387931034482, 
                                "absorbance_y": 0.07080387931034482, 
                                "concentration": 100.43103448275862, 
                                "concentration_x": 100.43103448275862, 
                                "concentration_y": 100.43103448275862, 
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
                                        "x": 6.633103448275862, 
                                        "y": 2
                                    }, 
                                    "beersLawLab.beersLawScreen.model.detector.valueProperty": 0.07080387931034482, 
                                    "beersLawLab.beersLawScreen.model.light.onProperty": true, 
                                    "beersLawLab.beersLawScreen.model.light.wavelengthProperty": 659, 
                                    "beersLawLab.beersLawScreen.model.ruler.locationProperty": {
                                        "x": 3.2920000000000003, 
                                        "y": 3.596
                                    }, 
                                    "beersLawLab.beersLawScreen.model.solutionProperty": "beersLawLab.beersLawScreen.solutions.copperSulfate", 
                                    "beersLawLab.beersLawScreen.solutions.cobaltChloride.concentrationProperty": 0.1, 
                                    "beersLawLab.beersLawScreen.solutions.cobaltIINitrate.concentrationProperty": 0.1, 
                                    "beersLawLab.beersLawScreen.solutions.copperSulfate.concentrationProperty": 0.10043103448275861, 
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
                                "trialNumber": 4, 
                                "trialNumber_x": 4, 
                                "trialNumber_y": 4, 
                                "visible": false, 
                                "wavelength": 659, 
                                "wavelength_x": 659, 
                                "wavelength_y": 659
                            }, 
                            {
                                "absorbance": 0.1421741896551724, 
                                "absorbance_x": 0.1421741896551724, 
                                "absorbance_y": 0.1421741896551724, 
                                "concentration": 100.43103448275862, 
                                "concentration_x": 100.43103448275862, 
                                "concentration_y": 100.43103448275862, 
                                "cuvetteWidth": 1.004, 
                                "cuvetteWidth_x": 1.004, 
                                "cuvetteWidth_y": 1.004, 
                                "image": {}, 
                                "state": {
                                    "beersLawLab.beersLawScreen.model.cuvette.widthProperty": 1.004, 
                                    "beersLawLab.beersLawScreen.model.detector.body.locationProperty": {
                                        "x": 6.3, 
                                        "y": 0.2
                                    }, 
                                    "beersLawLab.beersLawScreen.model.detector.modeProperty": "absorbance", 
                                    "beersLawLab.beersLawScreen.model.detector.probe.locationProperty": {
                                        "x": 6.633103448275862, 
                                        "y": 2
                                    }, 
                                    "beersLawLab.beersLawScreen.model.detector.valueProperty": 0.1421741896551724, 
                                    "beersLawLab.beersLawScreen.model.light.onProperty": true, 
                                    "beersLawLab.beersLawScreen.model.light.wavelengthProperty": 659, 
                                    "beersLawLab.beersLawScreen.model.ruler.locationProperty": {
                                        "x": 3.2920000000000003, 
                                        "y": 3.596
                                    }, 
                                    "beersLawLab.beersLawScreen.model.solutionProperty": "beersLawLab.beersLawScreen.solutions.copperSulfate", 
                                    "beersLawLab.beersLawScreen.solutions.cobaltChloride.concentrationProperty": 0.1, 
                                    "beersLawLab.beersLawScreen.solutions.cobaltIINitrate.concentrationProperty": 0.1, 
                                    "beersLawLab.beersLawScreen.solutions.copperSulfate.concentrationProperty": 0.10043103448275861, 
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
                                "trialNumber": 5, 
                                "trialNumber_x": 5, 
                                "trialNumber_y": 5, 
                                "visible": false, 
                                "wavelength": 659, 
                                "wavelength_x": 659, 
                                "wavelength_y": 659
                            }, 
                            {
                                "absorbance": 0.2101459137931034, 
                                "absorbance_x": 0.2101459137931034, 
                                "absorbance_y": 0.2101459137931034, 
                                "concentration": 100.43103448275862, 
                                "concentration_x": 100.43103448275862, 
                                "concentration_y": 100.43103448275862, 
                                "cuvetteWidth": 1.484, 
                                "cuvetteWidth_x": 1.484, 
                                "cuvetteWidth_y": 1.484, 
                                "image": {}, 
                                "state": {
                                    "beersLawLab.beersLawScreen.model.cuvette.widthProperty": 1.484, 
                                    "beersLawLab.beersLawScreen.model.detector.body.locationProperty": {
                                        "x": 6.3, 
                                        "y": 0.2
                                    }, 
                                    "beersLawLab.beersLawScreen.model.detector.modeProperty": "absorbance", 
                                    "beersLawLab.beersLawScreen.model.detector.probe.locationProperty": {
                                        "x": 6.633103448275862, 
                                        "y": 2
                                    }, 
                                    "beersLawLab.beersLawScreen.model.detector.valueProperty": 0.2101459137931034, 
                                    "beersLawLab.beersLawScreen.model.light.onProperty": true, 
                                    "beersLawLab.beersLawScreen.model.light.wavelengthProperty": 659, 
                                    "beersLawLab.beersLawScreen.model.ruler.locationProperty": {
                                        "x": 3.2920000000000003, 
                                        "y": 3.596
                                    }, 
                                    "beersLawLab.beersLawScreen.model.solutionProperty": "beersLawLab.beersLawScreen.solutions.copperSulfate", 
                                    "beersLawLab.beersLawScreen.solutions.cobaltChloride.concentrationProperty": 0.1, 
                                    "beersLawLab.beersLawScreen.solutions.cobaltIINitrate.concentrationProperty": 0.1, 
                                    "beersLawLab.beersLawScreen.solutions.copperSulfate.concentrationProperty": 0.10043103448275861, 
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
                                "trialNumber": 6, 
                                "trialNumber_x": 6, 
                                "trialNumber_y": 6, 
                                "visible": false, 
                                "wavelength": 659, 
                                "wavelength_x": 659, 
                                "wavelength_y": 659
                            }, 
                            {
                                "absorbance": 0.2832155172413793, 
                                "absorbance_x": 0.2832155172413793, 
                                "absorbance_y": 0.2832155172413793, 
                                "concentration": 100.43103448275862, 
                                "concentration_x": 100.43103448275862, 
                                "concentration_y": 100.43103448275862, 
                                "cuvetteWidth": 2, 
                                "cuvetteWidth_x": 2, 
                                "cuvetteWidth_y": 2, 
                                "image": {}, 
                                "state": {
                                    "beersLawLab.beersLawScreen.model.cuvette.widthProperty": 2, 
                                    "beersLawLab.beersLawScreen.model.detector.body.locationProperty": {
                                        "x": 6.3, 
                                        "y": 0.2
                                    }, 
                                    "beersLawLab.beersLawScreen.model.detector.modeProperty": "absorbance", 
                                    "beersLawLab.beersLawScreen.model.detector.probe.locationProperty": {
                                        "x": 6.633103448275862, 
                                        "y": 2
                                    }, 
                                    "beersLawLab.beersLawScreen.model.detector.valueProperty": 0.2832155172413793, 
                                    "beersLawLab.beersLawScreen.model.light.onProperty": true, 
                                    "beersLawLab.beersLawScreen.model.light.wavelengthProperty": 659, 
                                    "beersLawLab.beersLawScreen.model.ruler.locationProperty": {
                                        "x": 3.2920000000000003, 
                                        "y": 3.596
                                    }, 
                                    "beersLawLab.beersLawScreen.model.solutionProperty": "beersLawLab.beersLawScreen.solutions.copperSulfate", 
                                    "beersLawLab.beersLawScreen.solutions.cobaltChloride.concentrationProperty": 0.1, 
                                    "beersLawLab.beersLawScreen.solutions.cobaltIINitrate.concentrationProperty": 0.1, 
                                    "beersLawLab.beersLawScreen.solutions.copperSulfate.concentrationProperty": 0.10043103448275861, 
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
                                "trialNumber": 7, 
                                "trialNumber_x": 7, 
                                "trialNumber_y": 7, 
                                "visible": false, 
                                "wavelength": 659, 
                                "wavelength_x": 659, 
                                "wavelength_y": 659
                            }
                        ]
                    }, 
                    "phetioID": "labBook.restoreButton4"
                }
            ], 
            "messageID": 462, 
            "method": "triggerEvent", 
            "phetioID": "phetio", 
            "protocol": "phet-io-0.0.1"
        }, 
        "phetioID": "beersLawLab.simIFrameAPI", 
        "time": 1490208674091
    }, 
    "event": "beersLawLab.simIFrameAPI.invoked", 
    "index": 48239, 
    "timestamp": 1490208673911, 
    "type": "model"
}
''') 

Restoring_sim_state_event_parsed = True
Restoring_sim_state_event_user_or_model = 'user'
Restoring_sim_state_event_simevent = 'Restoring sim state'
Restoring_sim_state_event_item = 'trialNumber 4'
Restoring_sim_state_event_action = ''

#####################################################################################################################
setting_sim_state_event = json.loads(''' {
    "data": {
        "children": [
            {
                "children": [
                    {
                        "children": [
                            {
                                "componentType": "TTandemText", 
                                "event": "textChanged", 
                                "eventType": "model", 
                                "messageIndex": 51195, 
                                "parameters": {
                                    "newText": "0.07", 
                                    "oldText": "0.28"
                                }, 
                                "phetioID": "beersLawLab.beersLawScreen.view.detectorNode.bodyNode.valueNode", 
                                "time": 1490208674102
                            }
                        ], 
                        "componentType": "TDerivedProperty", 
                        "event": "changed", 
                        "eventType": "model", 
                        "messageIndex": 51194, 
                        "parameters": {
                            "newValue": 0.07080387931034482, 
                            "oldValue": 0.2832155172413793
                        }, 
                        "phetioID": "beersLawLab.beersLawScreen.model.detector.valueProperty", 
                        "time": 1490208674102
                    }
                ], 
                "componentType": "TProperty", 
                "event": "changed", 
                "eventType": "model", 
                "messageIndex": 51193, 
                "parameters": {
                    "newValue": 0.5, 
                    "oldValue": 2
                }, 
                "phetioID": "beersLawLab.beersLawScreen.model.cuvette.widthProperty", 
                "time": 1490208674101
            }, 
            {
                "componentType": "TProperty", 
                "event": "changed", 
                "eventType": "model", 
                "messageIndex": 51196, 
                "parameters": {
                    "newValue": {
                        "x": 3.2920000000000003, 
                        "y": 3.596
                    }, 
                    "oldValue": {
                        "x": 3.2920000000000003, 
                        "y": 3.596
                    }
                }, 
                "phetioID": "beersLawLab.beersLawScreen.model.ruler.locationProperty", 
                "time": 1490208674112
            }, 
            {
                "componentType": "TProperty", 
                "event": "changed", 
                "eventType": "model", 
                "messageIndex": 51197, 
                "parameters": {
                    "newValue": {
                        "x": 6.3, 
                        "y": 0.2
                    }, 
                    "oldValue": {
                        "x": 6.3, 
                        "y": 0.2
                    }
                }, 
                "phetioID": "beersLawLab.beersLawScreen.model.detector.body.locationProperty", 
                "time": 1490208674112
            }, 
            {
                "componentType": "TProperty", 
                "event": "changed", 
                "eventType": "model", 
                "messageIndex": 51198, 
                "parameters": {
                    "newValue": {
                        "x": 6.633103448275862, 
                        "y": 2
                    }, 
                    "oldValue": {
                        "x": 6.633103448275862, 
                        "y": 2
                    }
                }, 
                "phetioID": "beersLawLab.beersLawScreen.model.detector.probe.locationProperty", 
                "time": 1490208674114
            }
        ], 
        "componentType": "TSimIFrameAPI", 
        "event": "invoked", 
        "eventType": "wrapper", 
        "messageIndex": 51192, 
        "parameters": {
            "args": [
                {
                    "beersLawLab.beersLawScreen.model.cuvette.widthProperty": 0.5, 
                    "beersLawLab.beersLawScreen.model.detector.body.locationProperty": {
                        "x": 6.3, 
                        "y": 0.2
                    }, 
                    "beersLawLab.beersLawScreen.model.detector.modeProperty": "absorbance", 
                    "beersLawLab.beersLawScreen.model.detector.probe.locationProperty": {
                        "x": 6.633103448275862, 
                        "y": 2
                    }, 
                    "beersLawLab.beersLawScreen.model.detector.valueProperty": 0.07080387931034482, 
                    "beersLawLab.beersLawScreen.model.light.onProperty": true, 
                    "beersLawLab.beersLawScreen.model.light.wavelengthProperty": 659, 
                    "beersLawLab.beersLawScreen.model.ruler.locationProperty": {
                        "x": 3.2920000000000003, 
                        "y": 3.596
                    }, 
                    "beersLawLab.beersLawScreen.model.solutionProperty": "beersLawLab.beersLawScreen.solutions.copperSulfate", 
                    "beersLawLab.beersLawScreen.solutions.cobaltChloride.concentrationProperty": 0.1, 
                    "beersLawLab.beersLawScreen.solutions.cobaltIINitrate.concentrationProperty": 0.1, 
                    "beersLawLab.beersLawScreen.solutions.copperSulfate.concentrationProperty": 0.10043103448275861, 
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
            ], 
            "messageID": 463, 
            "method": "setState", 
            "phetioID": "phetio", 
            "protocol": "phet-io-0.0.1"
        }, 
        "phetioID": "beersLawLab.simIFrameAPI", 
        "time": 1490208674095
    }, 
    "event": "beersLawLab.simIFrameAPI.invoked", 
    "index": 48240, 
    "timestamp": 1490208673912, 
    "type": "model"
}
''') 

setting_sim_state_event_parsed = True
setting_sim_state_event_user_or_model = 'model'
setting_sim_state_event_simevent = 'setting sim state'
setting_sim_state_event_item = 'sim'
setting_sim_state_event_action = ''

#####################################################################################################################
Selecting_Y_axis_event = json.loads(''' {
    "data": {
        "children": [
            {
                "componentType": "TDropDownSelect", 
                "event": "changed", 
                "eventType": "user", 
                "messageIndex": 54232, 
                "parameters": {
                    "feature": "absorbance_y"
                }, 
                "phetioID": "labBook.yFeature", 
                "time": 1490208716512
            }
        ], 
        "componentType": "TSimIFrameAPI", 
        "event": "invoked", 
        "eventType": "wrapper", 
        "messageIndex": 54231, 
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
                        "feature": "absorbance_y"
                    }, 
                    "phetioID": "labBook.yFeature"
                }
            ], 
            "messageID": 473, 
            "method": "triggerEvent", 
            "phetioID": "phetio", 
            "protocol": "phet-io-0.0.1"
        }, 
        "phetioID": "beersLawLab.simIFrameAPI", 
        "time": 1490208716512
    }, 
    "event": "beersLawLab.simIFrameAPI.invoked", 
    "index": 51264, 
    "timestamp": 1490208716296, 
    "type": "model"
}
''') 

Selecting_Y_axis_event_parsed = True
Selecting_Y_axis_event_user_or_model = 'user'
Selecting_Y_axis_event_simevent = 'Selecting Y-axis'
Selecting_Y_axis_event_item = 'Y-axis dropdown menu'
Selecting_Y_axis_event_action = 'Y-axis changed to absorbance'

#####################################################################################################################
Selecting_X_axis_event = json.loads(''' {
    "data": {
        "children": [
            {
                "componentType": "TDropDownSelect", 
                "event": "changed", 
                "eventType": "user", 
                "messageIndex": 54352, 
                "parameters": {
                    "feature": "concentration_x"
                }, 
                "phetioID": "labBook.xFeature", 
                "time": 1490208718481
            }
        ], 
        "componentType": "TSimIFrameAPI", 
        "event": "invoked", 
        "eventType": "wrapper", 
        "messageIndex": 54351, 
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
                        "feature": "concentration_x"
                    }, 
                    "phetioID": "labBook.xFeature"
                }
            ], 
            "messageID": 474, 
            "method": "triggerEvent", 
            "phetioID": "phetio", 
            "protocol": "phet-io-0.0.1"
        }, 
        "phetioID": "beersLawLab.simIFrameAPI", 
        "time": 1490208718481
    }, 
    "event": "beersLawLab.simIFrameAPI.invoked", 
    "index": 51383, 
    "timestamp": 1490208718264, 
    "type": "model"
}
''') 

Selecting_X_axis_event_parsed = True
Selecting_X_axis_event_user_or_model = 'user'
Selecting_X_axis_event_simevent = 'Selecting X-axis'
Selecting_X_axis_event_item = 'X-axis dropdown menu'
Selecting_X_axis_event_action = 'X-axis changed to concentration'

#####################################################################################################################
Selecting_scale_of_Y_axis_event = json.loads(''' {
    "data": {
        "children": [
            {
                "componentType": "TRadioButton", 
                "event": "changed", 
                "eventType": "user", 
                "messageIndex": 61637, 
                "parameters": {
                    "feature": "log"
                }, 
                "phetioID": "labBook.yTransform", 
                "time": 1490208796747
            }
        ], 
        "componentType": "TSimIFrameAPI", 
        "event": "invoked", 
        "eventType": "wrapper", 
        "messageIndex": 61636, 
        "parameters": {
            "args": [
                {
                    "componentType": {
                        "events": [
                            "changed"
                        ], 
                        "typeName": "TRadioButton"
                    }, 
                    "event": "changed", 
                    "eventType": "user", 
                    "parameters": {
                        "feature": "log"
                    }, 
                    "phetioID": "labBook.yTransform"
                }
            ], 
            "messageID": 504, 
            "method": "triggerEvent", 
            "phetioID": "phetio", 
            "protocol": "phet-io-0.0.1"
        }, 
        "phetioID": "beersLawLab.simIFrameAPI", 
        "time": 1490208796747
    }, 
    "event": "beersLawLab.simIFrameAPI.invoked", 
    "index": 58277, 
    "timestamp": 1490208796523, 
    "type": "model"
}
''') 

Selecting_scale_of_Y_axis_event_parsed = True
Selecting_scale_of_Y_axis_event_user_or_model = 'user'
Selecting_scale_of_Y_axis_event_simevent = 'Selecting scale of Y-axis'
Selecting_scale_of_Y_axis_event_item = 'Y-axis scale dropdown menu'
Selecting_scale_of_Y_axis_event_action = 'Y-axis scale changed to log'

#####################################################################################################################
Selecting_scale_of_X_axis_event = json.loads(''' {
    "data": {
        "children": [
            {
                "componentType": "TRadioButton", 
                "event": "changed", 
                "eventType": "user", 
                "messageIndex": 61899, 
                "parameters": {
                    "feature": "log"
                }, 
                "phetioID": "labBook.xTransform", 
                "time": 1490208801037
            }
        ], 
        "componentType": "TSimIFrameAPI", 
        "event": "invoked", 
        "eventType": "wrapper", 
        "messageIndex": 61898, 
        "parameters": {
            "args": [
                {
                    "componentType": {
                        "events": [
                            "changed"
                        ], 
                        "typeName": "TRadioButton"
                    }, 
                    "event": "changed", 
                    "eventType": "user", 
                    "parameters": {
                        "feature": "log"
                    }, 
                    "phetioID": "labBook.xTransform"
                }
            ], 
            "messageID": 507, 
            "method": "triggerEvent", 
            "phetioID": "phetio", 
            "protocol": "phet-io-0.0.1"
        }, 
        "phetioID": "beersLawLab.simIFrameAPI", 
        "time": 1490208801037
    }, 
    "event": "beersLawLab.simIFrameAPI.invoked", 
    "index": 58536, 
    "timestamp": 1490208800812, 
    "type": "model"
}
''') 

Selecting_scale_of_X_axis_event_parsed = True
Selecting_scale_of_X_axis_event_user_or_model = 'user'
Selecting_scale_of_X_axis_event_simevent = 'Selecting scale of X-axis'
Selecting_scale_of_X_axis_event_item = 'X-axis scale dropdown menu'
Selecting_scale_of_X_axis_event_action = 'X-axis scale changed to log'

#####################################################################################################################
editing_notes_event = json.loads(''' {
    "data": {
        "componentType": "TextArea", 
        "event": "changed", 
        "eventType": "user", 
        "messageIndex": 5285, 
        "parameters": {
            "text": "o"
        }, 
        "phetioID": "labBook.textArea", 
        "time": 1484958224610
    }, 
    "event": "labBook.textArea.changed", 
    "index": 4326, 
    "timestamp": 1484958224448, 
    "type": "model"
}
''') 

editing_notes_event_parsed = True
editing_notes_event_user_or_model = 'user'
editing_notes_event_simevent = 'editing notes'
editing_notes_event_item = 'notepad'
editing_notes_event_action = ''

#####################################################################################################################
collapsing_table_event = json.loads(''' {
    "data": {
        "componentType": "TButton", 
        "event": "pressed", 
        "eventType": "user", 
        "messageIndex": 53557, 
        "phetioID": "labBook.tableCollapseButton", 
        "time": 1484940820639
    }, 
    "event": "labBook.tableCollapseButton.pressed", 
    "index": 50991, 
    "timestamp": 1484940820484, 
    "type": "model"
}
''') 

collapsing_table_event_parsed = True
collapsing_table_event_user_or_model = 'user'
collapsing_table_event_simevent = 'collapsing table'
collapsing_table_event_item = 'table'
collapsing_table_event_action = ''

#####################################################################################################################
collapsing_simulation_event = json.loads(''' {
    "data": {
        "componentType": "TButton", 
        "event": "pressed", 
        "eventType": "user", 
        "messageIndex": 55867, 
        "phetioID": "labBook.simulationCollapseButton", 
        "time": 1484940859118
    }, 
    "event": "labBook.simulationCollapseButton.pressed", 
    "index": 53301, 
    "timestamp": 1484940858957, 
    "type": "model"
}
''') 

collapsing_simulation_event_parsed = True
collapsing_simulation_event_user_or_model = 'user'
collapsing_simulation_event_simevent = 'collapsing simulation'
collapsing_simulation_event_item = 'simulation'
collapsing_simulation_event_action = ''

#####################################################################################################################
expanding_simulation_event = json.loads(''' {
    "data": {
        "componentType": "TButton", 
        "event": "pressed", 
        "eventType": "user", 
        "messageIndex": 64261, 
        "phetioID": "labBook.simulationExpandButton", 
        "time": 1484343740876
    }, 
    "event": "labBook.simulationExpandButton.pressed", 
    "index": 58854, 
    "timestamp": 1484343740729, 
    "type": "model"
}
''') 

expanding_simulation_event_parsed = True
expanding_simulation_event_user_or_model = 'user'
expanding_simulation_event_simevent = 'expanding simulation'
expanding_simulation_event_item = 'simulation'
expanding_simulation_event_action = ''

#####################################################################################################################
Moving_trial_in_table_event = json.loads(''' {
    "data": {
        "children": [
            {
                "componentType": "TButton", 
                "event": "pressed", 
                "eventType": "user", 
                "messageIndex": 66668, 
                "parameters": {
                    "userData": [
                        {
                            "absorbance": 3.844, 
                            "absorbance_x": 3.844, 
                            "absorbance_y": 3.844, 
                            "concentration": 200, 
                            "concentration_x": 200, 
                            "concentration_y": 200, 
                            "cuvetteWidth": 2, 
                            "cuvetteWidth_x": 2, 
                            "cuvetteWidth_y": 2, 
                            "image": {}, 
                            "state": {
                                "beersLawLab.beersLawScreen.model.cuvette.widthProperty": 2, 
                                "beersLawLab.beersLawScreen.model.detector.body.locationProperty": {
                                    "x": 6.3, 
                                    "y": 0.2
                                }, 
                                "beersLawLab.beersLawScreen.model.detector.modeProperty": "absorbance", 
                                "beersLawLab.beersLawScreen.model.detector.probe.locationProperty": {
                                    "x": 6.3, 
                                    "y": 2
                                }, 
                                "beersLawLab.beersLawScreen.model.detector.valueProperty": 3.844, 
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
                        {
                            "absorbance": 0, 
                            "absorbance_x": 0, 
                            "absorbance_y": 0, 
                            "concentration": 0, 
                            "concentration_x": 0, 
                            "concentration_y": 0, 
                            "cuvetteWidth": 2, 
                            "cuvetteWidth_x": 2, 
                            "cuvetteWidth_y": 2, 
                            "image": {}, 
                            "state": {
                                "beersLawLab.beersLawScreen.model.cuvette.widthProperty": 2, 
                                "beersLawLab.beersLawScreen.model.detector.body.locationProperty": {
                                    "x": 6.3, 
                                    "y": 0.2
                                }, 
                                "beersLawLab.beersLawScreen.model.detector.modeProperty": "absorbance", 
                                "beersLawLab.beersLawScreen.model.detector.probe.locationProperty": {
                                    "x": 6.3, 
                                    "y": 2
                                }, 
                                "beersLawLab.beersLawScreen.model.detector.valueProperty": 0, 
                                "beersLawLab.beersLawScreen.model.light.onProperty": true, 
                                "beersLawLab.beersLawScreen.model.light.wavelengthProperty": 780, 
                                "beersLawLab.beersLawScreen.model.ruler.locationProperty": {
                                    "x": 3.3, 
                                    "y": 3.58
                                }, 
                                "beersLawLab.beersLawScreen.model.solutionProperty": "beersLawLab.beersLawScreen.solutions.copperSulfate", 
                                "beersLawLab.beersLawScreen.solutions.cobaltChloride.concentrationProperty": 0.1, 
                                "beersLawLab.beersLawScreen.solutions.cobaltIINitrate.concentrationProperty": 0.1, 
                                "beersLawLab.beersLawScreen.solutions.copperSulfate.concentrationProperty": 0, 
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
                            "trialNumber": 2, 
                            "trialNumber_x": 2, 
                            "trialNumber_y": 2, 
                            "visible": false, 
                            "wavelength": 780, 
                            "wavelength_x": 780, 
                            "wavelength_y": 780
                        }, 
                        {
                            "absorbance": 0.09200000000000001, 
                            "absorbance_x": 0.09200000000000001, 
                            "absorbance_y": 0.09200000000000001, 
                            "concentration": 200, 
                            "concentration_x": 200, 
                            "concentration_y": 200, 
                            "cuvetteWidth": 2, 
                            "cuvetteWidth_x": 2, 
                            "cuvetteWidth_y": 2, 
                            "image": {}, 
                            "state": {
                                "beersLawLab.beersLawScreen.model.cuvette.widthProperty": 2, 
                                "beersLawLab.beersLawScreen.model.detector.body.locationProperty": {
                                    "x": 6.3, 
                                    "y": 0.2
                                }, 
                                "beersLawLab.beersLawScreen.model.detector.modeProperty": "absorbance", 
                                "beersLawLab.beersLawScreen.model.detector.probe.locationProperty": {
                                    "x": 6.3, 
                                    "y": 2
                                }, 
                                "beersLawLab.beersLawScreen.model.detector.valueProperty": 0.09200000000000001, 
                                "beersLawLab.beersLawScreen.model.light.onProperty": true, 
                                "beersLawLab.beersLawScreen.model.light.wavelengthProperty": 380, 
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
                            "trialNumber": 3, 
                            "trialNumber_x": 3, 
                            "trialNumber_y": 3, 
                            "visible": false, 
                            "wavelength": 380, 
                            "wavelength_x": 380, 
                            "wavelength_y": 380
                        }, 
                        {
                            "absorbance": 0, 
                            "absorbance_x": 0, 
                            "absorbance_y": 0, 
                            "concentration": 0, 
                            "concentration_x": 0, 
                            "concentration_y": 0, 
                            "cuvetteWidth": 2, 
                            "cuvetteWidth_x": 2, 
                            "cuvetteWidth_y": 2, 
                            "image": {}, 
                            "state": {
                                "beersLawLab.beersLawScreen.model.cuvette.widthProperty": 2, 
                                "beersLawLab.beersLawScreen.model.detector.body.locationProperty": {
                                    "x": 6.3, 
                                    "y": 0.2
                                }, 
                                "beersLawLab.beersLawScreen.model.detector.modeProperty": "absorbance", 
                                "beersLawLab.beersLawScreen.model.detector.probe.locationProperty": {
                                    "x": 6.3, 
                                    "y": 2
                                }, 
                                "beersLawLab.beersLawScreen.model.detector.valueProperty": 0, 
                                "beersLawLab.beersLawScreen.model.light.onProperty": true, 
                                "beersLawLab.beersLawScreen.model.light.wavelengthProperty": 380, 
                                "beersLawLab.beersLawScreen.model.ruler.locationProperty": {
                                    "x": 3.3, 
                                    "y": 3.58
                                }, 
                                "beersLawLab.beersLawScreen.model.solutionProperty": "beersLawLab.beersLawScreen.solutions.copperSulfate", 
                                "beersLawLab.beersLawScreen.solutions.cobaltChloride.concentrationProperty": 0.1, 
                                "beersLawLab.beersLawScreen.solutions.cobaltIINitrate.concentrationProperty": 0.1, 
                                "beersLawLab.beersLawScreen.solutions.copperSulfate.concentrationProperty": 0, 
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
                            "trialNumber": 4, 
                            "trialNumber_x": 4, 
                            "trialNumber_y": 4, 
                            "visible": false, 
                            "wavelength": 380, 
                            "wavelength_x": 380, 
                            "wavelength_y": 380
                        }, 
                        {
                            "absorbance": 0.09200000000000001, 
                            "absorbance_x": 0.09200000000000001, 
                            "absorbance_y": 0.09200000000000001, 
                            "concentration": 200, 
                            "concentration_x": 200, 
                            "concentration_y": 200, 
                            "cuvetteWidth": 2, 
                            "cuvetteWidth_x": 2, 
                            "cuvetteWidth_y": 2, 
                            "image": {}, 
                            "state": {
                                "beersLawLab.beersLawScreen.model.cuvette.widthProperty": 2, 
                                "beersLawLab.beersLawScreen.model.detector.body.locationProperty": {
                                    "x": 6.3, 
                                    "y": 0.2
                                }, 
                                "beersLawLab.beersLawScreen.model.detector.modeProperty": "absorbance", 
                                "beersLawLab.beersLawScreen.model.detector.probe.locationProperty": {
                                    "x": 6.3, 
                                    "y": 2
                                }, 
                                "beersLawLab.beersLawScreen.model.detector.valueProperty": 0.09200000000000001, 
                                "beersLawLab.beersLawScreen.model.light.onProperty": true, 
                                "beersLawLab.beersLawScreen.model.light.wavelengthProperty": 380, 
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
                            "trialNumber": 5, 
                            "trialNumber_x": 5, 
                            "trialNumber_y": 5, 
                            "visible": false, 
                            "wavelength": 380, 
                            "wavelength_x": 380, 
                            "wavelength_y": 380
                        }
                    ]
                }, 
                "phetioID": "labBook.incrementButton1", 
                "time": 1490143357435
            }
        ], 
        "componentType": "TSimIFrameAPI", 
        "event": "invoked", 
        "eventType": "wrapper", 
        "messageIndex": 66667, 
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
                        "userData": [
                            {
                                "absorbance": 3.844, 
                                "absorbance_x": 3.844, 
                                "absorbance_y": 3.844, 
                                "concentration": 200, 
                                "concentration_x": 200, 
                                "concentration_y": 200, 
                                "cuvetteWidth": 2, 
                                "cuvetteWidth_x": 2, 
                                "cuvetteWidth_y": 2, 
                                "image": {}, 
                                "state": {
                                    "beersLawLab.beersLawScreen.model.cuvette.widthProperty": 2, 
                                    "beersLawLab.beersLawScreen.model.detector.body.locationProperty": {
                                        "x": 6.3, 
                                        "y": 0.2
                                    }, 
                                    "beersLawLab.beersLawScreen.model.detector.modeProperty": "absorbance", 
                                    "beersLawLab.beersLawScreen.model.detector.probe.locationProperty": {
                                        "x": 6.3, 
                                        "y": 2
                                    }, 
                                    "beersLawLab.beersLawScreen.model.detector.valueProperty": 3.844, 
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
                            {
                                "absorbance": 0, 
                                "absorbance_x": 0, 
                                "absorbance_y": 0, 
                                "concentration": 0, 
                                "concentration_x": 0, 
                                "concentration_y": 0, 
                                "cuvetteWidth": 2, 
                                "cuvetteWidth_x": 2, 
                                "cuvetteWidth_y": 2, 
                                "image": {}, 
                                "state": {
                                    "beersLawLab.beersLawScreen.model.cuvette.widthProperty": 2, 
                                    "beersLawLab.beersLawScreen.model.detector.body.locationProperty": {
                                        "x": 6.3, 
                                        "y": 0.2
                                    }, 
                                    "beersLawLab.beersLawScreen.model.detector.modeProperty": "absorbance", 
                                    "beersLawLab.beersLawScreen.model.detector.probe.locationProperty": {
                                        "x": 6.3, 
                                        "y": 2
                                    }, 
                                    "beersLawLab.beersLawScreen.model.detector.valueProperty": 0, 
                                    "beersLawLab.beersLawScreen.model.light.onProperty": true, 
                                    "beersLawLab.beersLawScreen.model.light.wavelengthProperty": 780, 
                                    "beersLawLab.beersLawScreen.model.ruler.locationProperty": {
                                        "x": 3.3, 
                                        "y": 3.58
                                    }, 
                                    "beersLawLab.beersLawScreen.model.solutionProperty": "beersLawLab.beersLawScreen.solutions.copperSulfate", 
                                    "beersLawLab.beersLawScreen.solutions.cobaltChloride.concentrationProperty": 0.1, 
                                    "beersLawLab.beersLawScreen.solutions.cobaltIINitrate.concentrationProperty": 0.1, 
                                    "beersLawLab.beersLawScreen.solutions.copperSulfate.concentrationProperty": 0, 
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
                                "trialNumber": 2, 
                                "trialNumber_x": 2, 
                                "trialNumber_y": 2, 
                                "visible": false, 
                                "wavelength": 780, 
                                "wavelength_x": 780, 
                                "wavelength_y": 780
                            }, 
                            {
                                "absorbance": 0.09200000000000001, 
                                "absorbance_x": 0.09200000000000001, 
                                "absorbance_y": 0.09200000000000001, 
                                "concentration": 200, 
                                "concentration_x": 200, 
                                "concentration_y": 200, 
                                "cuvetteWidth": 2, 
                                "cuvetteWidth_x": 2, 
                                "cuvetteWidth_y": 2, 
                                "image": {}, 
                                "state": {
                                    "beersLawLab.beersLawScreen.model.cuvette.widthProperty": 2, 
                                    "beersLawLab.beersLawScreen.model.detector.body.locationProperty": {
                                        "x": 6.3, 
                                        "y": 0.2
                                    }, 
                                    "beersLawLab.beersLawScreen.model.detector.modeProperty": "absorbance", 
                                    "beersLawLab.beersLawScreen.model.detector.probe.locationProperty": {
                                        "x": 6.3, 
                                        "y": 2
                                    }, 
                                    "beersLawLab.beersLawScreen.model.detector.valueProperty": 0.09200000000000001, 
                                    "beersLawLab.beersLawScreen.model.light.onProperty": true, 
                                    "beersLawLab.beersLawScreen.model.light.wavelengthProperty": 380, 
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
                                "trialNumber": 3, 
                                "trialNumber_x": 3, 
                                "trialNumber_y": 3, 
                                "visible": false, 
                                "wavelength": 380, 
                                "wavelength_x": 380, 
                                "wavelength_y": 380
                            }, 
                            {
                                "absorbance": 0, 
                                "absorbance_x": 0, 
                                "absorbance_y": 0, 
                                "concentration": 0, 
                                "concentration_x": 0, 
                                "concentration_y": 0, 
                                "cuvetteWidth": 2, 
                                "cuvetteWidth_x": 2, 
                                "cuvetteWidth_y": 2, 
                                "image": {}, 
                                "state": {
                                    "beersLawLab.beersLawScreen.model.cuvette.widthProperty": 2, 
                                    "beersLawLab.beersLawScreen.model.detector.body.locationProperty": {
                                        "x": 6.3, 
                                        "y": 0.2
                                    }, 
                                    "beersLawLab.beersLawScreen.model.detector.modeProperty": "absorbance", 
                                    "beersLawLab.beersLawScreen.model.detector.probe.locationProperty": {
                                        "x": 6.3, 
                                        "y": 2
                                    }, 
                                    "beersLawLab.beersLawScreen.model.detector.valueProperty": 0, 
                                    "beersLawLab.beersLawScreen.model.light.onProperty": true, 
                                    "beersLawLab.beersLawScreen.model.light.wavelengthProperty": 380, 
                                    "beersLawLab.beersLawScreen.model.ruler.locationProperty": {
                                        "x": 3.3, 
                                        "y": 3.58
                                    }, 
                                    "beersLawLab.beersLawScreen.model.solutionProperty": "beersLawLab.beersLawScreen.solutions.copperSulfate", 
                                    "beersLawLab.beersLawScreen.solutions.cobaltChloride.concentrationProperty": 0.1, 
                                    "beersLawLab.beersLawScreen.solutions.cobaltIINitrate.concentrationProperty": 0.1, 
                                    "beersLawLab.beersLawScreen.solutions.copperSulfate.concentrationProperty": 0, 
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
                                "trialNumber": 4, 
                                "trialNumber_x": 4, 
                                "trialNumber_y": 4, 
                                "visible": false, 
                                "wavelength": 380, 
                                "wavelength_x": 380, 
                                "wavelength_y": 380
                            }, 
                            {
                                "absorbance": 0.09200000000000001, 
                                "absorbance_x": 0.09200000000000001, 
                                "absorbance_y": 0.09200000000000001, 
                                "concentration": 200, 
                                "concentration_x": 200, 
                                "concentration_y": 200, 
                                "cuvetteWidth": 2, 
                                "cuvetteWidth_x": 2, 
                                "cuvetteWidth_y": 2, 
                                "image": {}, 
                                "state": {
                                    "beersLawLab.beersLawScreen.model.cuvette.widthProperty": 2, 
                                    "beersLawLab.beersLawScreen.model.detector.body.locationProperty": {
                                        "x": 6.3, 
                                        "y": 0.2
                                    }, 
                                    "beersLawLab.beersLawScreen.model.detector.modeProperty": "absorbance", 
                                    "beersLawLab.beersLawScreen.model.detector.probe.locationProperty": {
                                        "x": 6.3, 
                                        "y": 2
                                    }, 
                                    "beersLawLab.beersLawScreen.model.detector.valueProperty": 0.09200000000000001, 
                                    "beersLawLab.beersLawScreen.model.light.onProperty": true, 
                                    "beersLawLab.beersLawScreen.model.light.wavelengthProperty": 380, 
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
                                "trialNumber": 5, 
                                "trialNumber_x": 5, 
                                "trialNumber_y": 5, 
                                "visible": false, 
                                "wavelength": 380, 
                                "wavelength_x": 380, 
                                "wavelength_y": 380
                            }
                        ]
                    }, 
                    "phetioID": "labBook.incrementButton1"
                }
            ], 
            "messageID": 442, 
            "method": "triggerEvent", 
            "phetioID": "phetio", 
            "protocol": "phet-io-0.0.1"
        }, 
        "phetioID": "beersLawLab.simIFrameAPI", 
        "time": 1490143357435
    }, 
    "event": "beersLawLab.simIFrameAPI.invoked", 
    "index": 64144, 
    "timestamp": 1490143357298, 
    "type": "model"
}
''') 

Moving_trial_in_table_event_parsed = True
Moving_trial_in_table_event_user_or_model = 'user'
Moving_trial_in_table_event_simevent = 'Moving trial in table'
Moving_trial_in_table_event_item = 'trialNumber 1'
Moving_trial_in_table_event_action = 'Moved trial down'

#####################################################################################################################
