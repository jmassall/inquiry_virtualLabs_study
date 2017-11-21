import os
import datetime
import getpass
import pandas as pd

FOLDER =  'C:\\Users\\'+getpass.getuser()+'\\Documents\\Personal Content\\Lab_study_data\\parsed log data'

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

def get_latest_parsing_report(sim, date=None, infolder=FOLDER):
    return  pd.read_table(find_latest_parsing_report_file(sim, date=None, infolder=FOLDER), sep='\t')

def get_session_data():
    return pd.read_table('C:\\Users\\'+getpass.getuser()+'\\Documents\\Personal Content\\Lab_study_data\\signout sheets\\session_data.txt',sep='\t')            