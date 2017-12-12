import os
import datetime
import getpass
import pandas as pd
from utils_timeline_viz import find_student_log_file

FOLDER =  'C:\\Users\\'+getpass.getuser()+'\\Documents\\Personal Content\\Lab_study_data\\parsed log data'
BIG_FOLDER =  'C:\\Users\\'+getpass.getuser()+'\\Documents\\Personal Content\\Lab_study_data'


def find_latest_parsing_report_file(sim, date=None, infolder=FOLDER):
    if date:
        for root, dirs, files in os.walk(infolder):
            for f in files:
                if sim in f and "report" in f and date in f:
                    print "Captured {0} parsing report that was parsed on {1}".format(sim,date)
                    return os.path.join(root, f)
        print "No file found for {0} sim and on date {1}.".format(sim,date)
    else:
        report_dates = []
        for root, dirs, files in os.walk(infolder):
            for f in files:
                if sim in f and "report" in f:
                    report_dates.append(os.path.join(root, f).split('on=')[1].replace('.txt',''))
        dates = [datetime.datetime.strptime(d, '%Y-%m-%d_%H.%M.%S') for d in report_dates]
        dates.sort()
        sorteddates = [datetime.datetime.strftime(ts, '%Y-%m-%d_%H.%M.%S') for ts in dates]
        if sorteddates:
            return find_latest_parsing_report_file(sim, date=sorteddates[-1], infolder=infolder)
        else:
            print "No file found for {0} sim.".format(sim)

def get_pre_survey():
    filepath = os.path.join(BIG_FOLDER,'raw study data\\survey data\\responses_pre-assessment_downloaded_4.3.2017.txt')
    df = pd.read_csv(filepath,sep='\t',encoding = "ISO-8859-1")
    return df

def get_worksheet_metadata():
    filepath = os.path.join(BIG_FOLDER,'coded worksheet data\coded_worksheets_metadata.csv')
    df = pd.read_csv(filepath,sep=',')
    return df

def get_latest_parsing_report(sim, date=None, infolder=FOLDER):
    return  pd.read_table(find_latest_parsing_report_file(sim, date=None, infolder=FOLDER), sep='\t')

def get_session_data():
    return pd.read_table('C:\\Users\\'+getpass.getuser()+'\\Documents\\Personal Content\\Lab_study_data\\signout sheets\\session_data.txt',sep='\t')            

def get_student_metadata():
    return pd.read_excel(os.path.join(BIG_FOLDER,'connector_id_to_log_files_and_session_annotated_fixed.xlsx'), sep='\t')

def get_students_to_analyze():
    df = get_student_metadata()
    return df[df['use analysis']==True].index.values

def get_date_event_pairs(sim,row):
    if sim == "beers":
        return [(row["date beers 1"],row["events beers 1"]),(row["date beers 2"],row["events beers 2"]),(row["date beers 3"],row["events beers 3"]),(row["date beers 4"],row["events beers 4"]),(row["date beers 5"],row["events beers 5"])]
    if sim == "capacitor":
        return [(row["date caps 1"],row["events caps 1"]),(row["date caps 2"],row["events caps 2"]),(row["date caps 3"],row["events caps 3"])]

# def get_students_order():
#     df = get_student_metadata()
#     return dict(zip(df.studentid,df['activity order']))

def get_parsed_log_files_per_student_for_sim(sim):
    df = get_student_metadata()
    df = df[df['use analysis']==True]
    log_files = {sid:[] for sid in df.index.values}
    for sid, row in df.iterrows():
        #grab date-event number pairs
        pairs = get_date_event_pairs(sim,row)
        #for dates with non zero events
        for date,number_events in pairs:
            if number_events > 0 :
                parsed_file = find_student_log_file(sim,sid,date=date)
                if parsed_file == None: # try finding the parse file with the secondary id
                    parsed_file = find_student_log_file(sim,int(row['other id']),date=date)
                    if parsed_file == None:
                        print "ERROR: This student ({0}) has no log file for {1}, even using it's other id {2}".format(sid,sim,row['other id'])
                log_files[sid].append(parsed_file)
    return log_files
