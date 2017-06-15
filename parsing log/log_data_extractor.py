'''
author: sperez8
data: june 14 2017

This script extracts relevant information from log data from a PhET sim
'''
import os
import json

folder = 'C:\\Users\\sperez8\\Documents\\Personal Content\\Lab_skills_study\\raw study data\\log data\\'
samplefile = '5a257a80-aa82-471d-b75c-f1113f314da1.log'

def get_one_line():
    outfile = open("log_data_1_student_example.txt", "w") 

    data = []
    with open(os.path.join(folder+samplefile),'r') as f:
        for line in f:
    		try:
    			line_json=json.loads(line)
    			print >> outfile, json.dumps(line_json, indent=4, sort_keys=True)
    		except:
    			pass
    		break

    f.close()
    outfile.close()
    return None

class Session:

    def __init__(self, filename):
        self.filename = filename
        self.get_session_data()

    def get_session_data(self):
        with open((self.filename),'r') as f:
            try:
                data=json.load(f)
                self.all_events = data['events']
                self.student_id = data['session']['learner_id']
                self.session_id = data['session']['session_id']
                self.sim = data['session']['widget_id']
            except:
                pass
        f.close()
        return None


    def clean_events(self):
        self.events = []
        for event in self.all_events:
            if event['event'] == 'phetio.stepSimulation' or event['event'] == 'phetio.inputEvent':
                pass
            else:
                self.events.append(event)
        return None

    def create_walk(self):
        self.walk = []
        for event in self.events:
            # self.walk.append([str(event['timestamp']),str(event['type']),str(event['event'])])
            self.walk.append(str(event['event']))
        return None

    def export_walk(self):
        outfile = open('example_walk.txt', 'w')
        for event in self.walk:
            # outfile.write(','.join(event)+'\n')
            outfile.write(event+'\n')

        outfile.close()



filename = "log_data_1_student_example.json"

session = Session(filename)
print session.student_id
print len(session.all_events)
session.clean_events()
print len(session.events)
session.create_walk()
session.export_walk()

# filter_out_time_counter(filename)
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


