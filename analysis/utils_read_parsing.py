'''
author: sperez8
Here are all the functions related to loading student data (log, worksheet, metadata and survey data)
as well as connecting these different data sources using student ids (which often have mistakes in them)
'''

import os
import datetime
import getpass
import pickle
import pandas as pd
from utils_timeline_viz import find_student_log_file

FOLDER =  'C:\\Users\\'+getpass.getuser()+'\\Documents\\Personal Content\\Lab_study_data\\parsed log data'
BIG_FOLDER =  'C:\\Users\\'+getpass.getuser()+'\\Documents\\Personal Content\\Lab_study_data'


def find_latest_parsing_report_file(sim, date=None, infolder=FOLDER):
    '''
    Given a sim (beers or capacitor), find the latest parsing report from a certain folder.
    You can also specific a report from a certain date or folder.
    '''
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


def get_pre_survey():
    filepath = os.path.join(BIG_FOLDER,'raw study data\\survey data\\responses_pre-assessment_downloaded_4.3.2017.txt')
    df = pd.read_csv(filepath,sep='\t',encoding = "ISO-8859-1")
    return df

def get_post_answers_key():
    filepath = os.path.join(BIG_FOLDER,'all_massaged_data\\all_quant_answers_key.txt')
    df = pd.read_csv(filepath,sep='\t')
    return df   

def get_massaged_pre_survey():
    filepath = os.path.join(BIG_FOLDER,'all_massaged_data\\pre_survey_results.txt')
    df = pd.read_csv(filepath,sep='\t')
    return df    

def get_massaged_post_survey():
    filepath = os.path.join(BIG_FOLDER,'all_massaged_data\\post_survey_results.txt')
    df = pd.read_csv(filepath,sep='\t')
    return df 

def get_massaged_worksheet_model_data():
    filepath = os.path.join(BIG_FOLDER,'all_massaged_data\\worksheets_models.txt')
    df = pd.read_csv(filepath,sep='\t')
    return df 

def get_massaged_worksheet_highest_understanding_data():
    filepath = os.path.join(BIG_FOLDER,'all_massaged_data\\worksheets_highest_understanding.txt')
    df = pd.read_csv(filepath,sep='\t')
    return df 

def get_massaged_near_transfer_data():
    filepath = os.path.join(BIG_FOLDER,'all_massaged_data\\post_scores_near_transfer_per_variable.txt')
    df = pd.read_csv(filepath,sep='\t')
    return df 

def get_incoming_attitudes():
    filepath = os.path.join(BIG_FOLDER,'all_massaged_data\\incoming_attitudes.txt')
    df = pd.read_csv(filepath, sep='\t')
    return df

def get_use_wrapper_results():
    filepath = os.path.join(BIG_FOLDER,'all_massaged_data\\use_wrapper_results.txt')
    df = pd.read_csv(filepath, sep='\t')
    return df

def get_table_cvs_results():
    filepath = os.path.join(BIG_FOLDER,'all_massaged_data\\table_cvs_results.txt')
    df = pd.read_csv(filepath, sep='\t')
    return df

def get_table_non_consecutive_cvs_results():
    filepath = os.path.join(BIG_FOLDER,'all_massaged_data\\table_non_consecutive_cvs_results_2-3-4.txt')
    df = pd.read_csv(filepath, sep='\t')
    return df

def get_table_intervals_results():
    filepath = os.path.join(BIG_FOLDER,'all_massaged_data\\table_intervals_results.txt')
    df = pd.read_csv(filepath, sep='\t')
    return df

def get_graph_cvs_results():
    filepath = os.path.join(BIG_FOLDER,'all_massaged_data\\graph_cvs_results.txt')
    df = pd.read_csv(filepath, sep='\t')
    return df

def get_cvs_results(number_trials,merged=True):
    if merged:
        filepath = os.path.join(BIG_FOLDER,'all_massaged_data\\cvs_{0}_merged_context.txt'.format(number_trials))
    else:
        filepath = os.path.join(BIG_FOLDER,'all_massaged_data\\cvs_{0}_context.txt'.format(number_trials))
    df = pd.read_csv(filepath, sep='\t')
    return df

def get_cvs_graph_inverse_results():
    filepath = os.path.join(BIG_FOLDER,'all_massaged_data\\graph_inverse_cvs_df.txt')
    df = pd.read_csv(filepath, sep='\t')
    return df

SIM_NAMES = {'beers':'ABSORBANCE','caps':'CAPACITORS'}
def get_worksheet_metadata(sim):
    if sim == 'capacitor':
        sim = 'caps'
    #get primary metadata file for that sim
    primary_filepath = os.path.join(BIG_FOLDER,'coded worksheet data\\'+sim+'_coded_worksheets_metadata.csv')
    primary_df = pd.read_csv(primary_filepath,sep=',')
    
    #get metadata file for extras worksheets
    extras_filepath = os.path.join(BIG_FOLDER,'coded worksheet data\extra_session_coded_worksheets_metadata.csv')
    extras_df = pd.read_csv(extras_filepath,sep=',')
    extras_df = extras_df[extras_df['Topic']==SIM_NAMES[sim]]
    df = pd.concat([primary_df,extras_df])   
    df = df.reset_index(drop=True)
    return df

def get_worksheet_data_by_model_per_sim(sim):
    if sim == 'capacitor':
        sim = 'caps'
    #get primary metadata file for that sim
    primary_filepath = os.path.join(BIG_FOLDER,'coded worksheet data\\all_model_types_correctness_coding\\'+sim+'_coded_with_model-type.csv')
    primary_df = pd.read_csv(primary_filepath,sep=',')
    
    #get metadata file for extras worksheets
    extras_filepath = os.path.join(BIG_FOLDER,'coded worksheet data\\all_model_types_correctness_coding\\extras_coded_with_model-type.csv')
    extras_df = pd.read_csv(extras_filepath,sep=',')
    extras_df = extras_df[extras_df['Topic']==SIM_NAMES[sim]]
    df = pd.concat([primary_df,extras_df])   
    df = df.reset_index(drop=True)
    return df

def get_pre_worksheet_highest_understanding(sim):
    #sim = beers or caps    
    primary_filepath = os.path.join(BIG_FOLDER,'coded worksheet data\\highest_correct_model_coding\\'+sim+'_gradebook_pre.csv')
    primary_df = pd.read_csv(primary_filepath,sep=',')
    
    #get file for extras worksheets
    extras_filepath = os.path.join(BIG_FOLDER,'coded worksheet data\\highest_correct_model_coding\\gradebook_extras_pre.csv')
    extras_df = pd.read_csv(extras_filepath,sep=',')
    if sim == 'beers':
        extras_df = extras_df[['Student ID','Concentration','Wavelength','Width']]
    elif sim == 'caps':
        extras_df = extras_df[['Student ID','Area','Separation','Battery voltage']]
    df = pd.concat([primary_df,extras_df])
    df = df.reset_index(drop=True)
    return df

def get_main_worksheet_highest_understanding(sim):
    #sim = beers or caps
    primary_filepath = os.path.join(BIG_FOLDER,'coded worksheet data\\highest_correct_model_coding\\'+sim+'_gradebook_main.csv')
    primary_df = pd.read_csv(primary_filepath,sep=',')
    
    #get file for extras worksheets
    extras_filepath = os.path.join(BIG_FOLDER,'coded worksheet data\\highest_correct_model_coding\\gradebook_extras_main.csv')
    extras_df = pd.read_csv(extras_filepath,sep=',')
    if sim == 'beers':
        extras_df = extras_df[['Student ID','Concentration','Wavelength','Width']]
    elif sim == 'caps':
        extras_df = extras_df[['Student ID','Area','Separation','Battery voltage']]
    df = pd.concat([primary_df,extras_df])   
    df = df.reset_index(drop=True)
    return df

def get_session_data():
    return pd.read_table('C:\\Users\\'+getpass.getuser()+'\\Documents\\Personal Content\\Lab_study_data\\signout sheets\\session_data.txt',sep='\t')            

def get_student_metadata():
    return pd.read_excel(os.path.join(BIG_FOLDER,'connector_id_to_log_files_and_session_annotated_fixed.xlsx'), sep='\t')

def get_students_to_analyze_log():
    df = get_student_metadata()
    return df[df['use analysis']==True].index.values

def get_date_event_pairs(sim,row):
    if sim == "beers":
        return [(row["date beers 1"],row["events beers 1"]),(row["date beers 2"],row["events beers 2"]),(row["date beers 3"],row["events beers 3"]),(row["date beers 4"],row["events beers 4"]),(row["date beers 5"],row["events beers 5"])]
    if sim == "capacitor":
        return [(row["date caps 1"],row["events caps 1"]),(row["date caps 2"],row["events caps 2"]),(row["date caps 3"],row["events caps 3"])]

def get_parsed_log_files_per_student_for_sim(sim,update=False):

    if update == False:
        try:
            log_files = pickle.load(open(getpass.getuser()+'_'+sim+'_log_files_per_student.txt','r'))
            print "The file "+getpass.getuser()+'_'+sim+'_log_files_per_student.txt has been unpickled and loaded'
            return log_files
        except IOError:
            print "The file "+getpass.getuser()+'_'+sim+"_log_files_per_student.txt was not found. Creating it..."

    df = get_student_metadata()
    students = get_students_to_analyze_log_worksheets(sim)
    df['sid'] = df.index
    print df.shape
    df = df[df['sid'].isin(students)]
    print df.shape
    log_files = {sid:[] for sid in students}

    for sid, row in df.iterrows():
        #grab date-event number pairs
        pairs = get_date_event_pairs(sim,row)
        #for dates with non zero events
        for date,number_events in pairs:
#             print date, number_events
            if number_events > 0 :
                parsed_file = find_student_log_file(sim,sid,date=date)
                if parsed_file is None: # try finding the parse file with the secondary id
                    parsed_file = find_student_log_file(sim,int(row['other id']),date=date)
                    if parsed_file is None:
                        print "ERROR: This student ({0}) has no log file for {1}, even using it's other id {2}".format(sid,sim,row['other id'])
                log_files[sid].append(parsed_file)
    pickle.dump(log_files,open(getpass.getuser()+'_'+sim+'_log_files_per_student.txt','w'))
    print "The file "+getpass.getuser()+'_'+sim+'_log_files_per_student.txt has been created and pickled'
    return log_files