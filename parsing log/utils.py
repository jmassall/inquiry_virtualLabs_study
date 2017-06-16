'''
author: sperez8
data: june 14 2017

This script extracts relevant information from log data from a PhET sim
'''
import json

class Session:

    def __init__(self, filename=None):
        if filename:
            self.get_session_data_from_file(filename)


    def get_session_data_from_file(self,filename):
        with open((filename),'r') as f:
            try:
                data=json.load(f)
                self.parse_data(data)
            except:
                pass
        f.close()
        return None

    def parse_data(self,data):
        self.all_events = data['events']
        self.student_id = data['session']['learner_id']
        self.session_id = data['session']['session_id']
        self.sim = data['session']['widget_id']

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


#HOW TO USE THE SESSION CLASS?

    # filename = "log_data_1_student_example.json"
    # session = Session(filename) where filename is a file with a single json element
    # or
    # session = Session()
    # session.parse_data(line_json) where line_json is a loaded json element

    # then we can do fun things:
    # print session.student_id
    # print len(session.all_events)
    # session.clean_events()
    # print len(session.events)
    # session.create_walk()
    # session.export_walk()





