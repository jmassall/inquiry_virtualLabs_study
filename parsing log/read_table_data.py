'''
author: sperez8
data: july 11th 2017

This captures the recorded data from a single student's activity file
'''
import os
import sys
import json
from utils import *

def detect_recordData(event):
    if event['event'] == "beersLawLab.simIFrameAPI.invoked":
        if 'children' in event['data']:
            if event['data']['children'][0]['phetioID'] == "labBook.recordDataButton":
                return True
    return False

def detect_notesActivity(event):
    if event['event'] == "beersLawLab.simIFrameAPI.invoked":
        if 'children' in event['data']:
            if event['data']['children'][0]['phetioID'] == "labBook.textArea":
                return True
    return False

def parse_recordData(event):
    data = {}
    meat = event['data']['children'][0]['parameters']
    data['Trial'] = meat['trialNumber']
    data['Wavelength'] = meat['wavelength']
    data['Width'] = meat['cuvetteWidth']
    data['Concentration'] = meat['concentration']
    data['Absorbance'] = meat['absorbance']
    data['inGraph'] = meat['visible']
    return data

def parse_notesActivity(event):
    notes = event['data']['children'][0]['parameters']['text']
    return notes

def iterate_and_parse(events):
    state = 'increasing'
    previous_notes = ''
    for i,event in enumerate(events):
        # if detect_recordData(event):
        #   data = parse_recordData(event)
        #   print data
        if detect_notesActivity(event):
            notes = parse_notesActivity(event)
            print state, len(notes),len(previous_notes), notes+'.'
            if state == 'increasing' and len(notes)<len(previous_notes):
                print 'out\t', notes
                state = 'decreasing'
            if state == 'decreasing' and len(notes)>len(previous_notes):
                print 'out\t', notes
                state = 'increasing'
            previous_notes = notes
    return None

# # test_json = 'example_parsed_student_data_file.json'
datapath = 'C:\\Users\\'+getpass.getuser()+'\\Documents\\Personal Content\\Lab_skills_study\\cleaned log data\\cleaned_and_split_5a257a80-aa82-471d-b75c-f1113f314da1'
# session_file = 'log_lab-book-beers-law-lab_12288167_2017-03-22_11.40.14.json'
# test_json =  os.path.join(datapath,session_file)
# session = Session()
# session.get_session_data_from_file(test_json)
# # iterate_and_parse(session.events)



#let's iterate thorugh all raw files for beerslaw and capture the last note state for all students. Yeah!

notes_report = open('reports_on_notes.txt','w')
notes_report.write('\t'.join(['filename','notes']))
for file in os.listdir(datapath):
    if file.endswith(".json"):
        notes_report.write('\n')
        session_file = os.path.join(datapath, file)
        notes_report.write(file)
        session = Session()
        session.get_session_data_from_file(session_file)
        notes = ''
        for i,event in enumerate(session.events):
            if detect_notesActivity(event):
                notes = parse_notesActivity(event)
        notes_report.write('\t')
        notes_report.write(notes)
        