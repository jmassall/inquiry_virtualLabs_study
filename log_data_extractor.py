'''
author: sperez8
data: june 14 2017

This script extracts relevant information from log data from a PhET sim
'''

folder = 'C:\\Users\\sperez8\\Documents\\Personal Content\\Lab_skills_study\\raw study data\\log data\\'
samplefile = '5a257a80-aa82-471d-b75c-f1113f314da1.log'

outfile = open("log_data_1_student_example.txt", "w") 
import os
import json

data = []
with open(os.path.join(folder+samplefile),'r') as f:
    for line in f:
        # data.append(json.loads(line))
        # break

		try:
			line_json=json.loads(line)
			print >> outfile, json.dumps(line_json, indent=4, sort_keys=True)
		except:
			pass
		break

f.close()
outfile.close()


"""
In that file I found different kinds of events:

            "event": "phetio.stepSimulation", 
                "event": "stepSimulation", 
                "event": "inputEvent", 
            "event": "phetio.inputEvent", 
                                        "event": "textChanged", 
                                "event": "changed", 
                        "event": "changed", 
                "event": "dragged", 
            "event": "beersLawLab.beersLawScreen.view.solutionControls.concentrationControl.slider.thumb.dragHandler.dragged", 
                "event": "state", 
            "event": "phetio.state", 


Now it's time to remove "phetio.stepSimulation" and "phetio.inputEvent"
"""