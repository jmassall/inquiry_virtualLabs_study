'''
Here are all the functions related to loading student data (log, worksheet, metadata and survey data)
as well as connecting these different data sources using student ids (which often have mistakes in them)
'''

import os
import datetime
import getpass
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

def get_all_posts_surveys():
    posts = pd.DataFrame()
    for sim_order in ['Capacitance-assessment-2LC','Absorbance-assessment-1LC','Capacitance-assessment-1CL','Absorbance-assessment-2CL']:
        filename = 'responses_{0}_downloaded_4.3.2017.txt'.format(sim_order)
        filepath = os.path.join(BIG_FOLDER,'raw study data\\survey data\\'+filename)
        newdf = pd.read_csv(filepath,sep='\t',encoding = "ISO-8859-1")
        newdf['sim_index'] = sim_order[-3]

        posts = pd.concat([posts,newdf])    
        
    #cleaning up columns
    old_columns = list(posts.columns)
    new_columns = [c.split(']')[0].replace('[','') for c in old_columns]
    for i,(c,d) in enumerate(zip(new_columns,old_columns)):
        if new_columns.count(c)>1:
            new_columns[i] = d
    posts.columns = new_columns

    def ids_posts_to_logs(row):
        sid = row['id']
        if sid in [561164,192168,7868168]:
            return sid+10000000
        elif sid == 17595160:
            return 17597160
        elif sid == 31607164:
            return 36107164
        elif sid == 17931169:
            if row['IP Address'] == '142.103.243.201':
                return 17931169
            else:
                return 12345678 #cahnge the id so we don't use it
        elif sid == 84135167:
            return 83145167
        else:
            return sid

    #adding an sid that matches logs.
    posts['sid'] = posts.apply(lambda row: ids_posts_to_logs(row),axis=1)
    posts = posts.rename(columns = {'id':'original id'})
    
    #filtering out all post survey data that is not analyzable
    log_ids = set(get_students_to_analyze_log())
    posts = posts[posts['sid'].isin(log_ids)]
    return posts


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

def get_pre_worksheet(sim):
    #sim = beers or caps    
    primary_filepath = os.path.join(BIG_FOLDER,'coded worksheet data\\'+sim+'_gradebook_pre.csv')
    primary_df = pd.read_csv(primary_filepath,sep=',')
    
    #get file for extras worksheets
    extras_filepath = os.path.join(BIG_FOLDER,'coded worksheet data\gradebook_extras_pre.csv')
    extras_df = pd.read_csv(extras_filepath,sep=',')
    if sim == 'beers':
        extras_df = extras_df[['Student ID','Concentration','Wavelength','Width']]
    elif sim == 'caps':
        extras_df = extras_df[['Student ID','Area','Separation','Battery voltage']]
    df = pd.concat([primary_df,extras_df])
    df = df.reset_index(drop=True)
    return df

def get_main_worksheet(sim):
    #sim = beers or caps
    primary_filepath = os.path.join(BIG_FOLDER,'coded worksheet data\\'+sim+'_gradebook_main.csv')
    primary_df = pd.read_csv(primary_filepath,sep=',')
    
    #get file for extras worksheets
    extras_filepath = os.path.join(BIG_FOLDER,'coded worksheet data\\gradebook_extras_main.csv')
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

def get_students_to_analyze_log_worksheets(sim):
    ids = set(get_students_to_analyze_log())
    worksheets = get_worksheet_metadata(sim)
    return set(list(worksheets[worksheets['use analysis']==True]['Student ID']))&set(ids)

def get_date_event_pairs(sim,row):
    if sim == "beers":
        return [(row["date beers 1"],row["events beers 1"]),(row["date beers 2"],row["events beers 2"]),(row["date beers 3"],row["events beers 3"]),(row["date beers 4"],row["events beers 4"]),(row["date beers 5"],row["events beers 5"])]
    if sim == "capacitor":
        return [(row["date caps 1"],row["events caps 1"]),(row["date caps 2"],row["events caps 2"]),(row["date caps 3"],row["events caps 3"])]

import pickle
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
                if parsed_file == None: # try finding the parse file with the secondary id
                    parsed_file = find_student_log_file(sim,int(row['other id']),date=date)
                    if parsed_file == None:
                        print "ERROR: This student ({0}) has no log file for {1}, even using it's other id {2}".format(sid,sim,row['other id'])
                log_files[sid].append(parsed_file)
    pickle.dump(log_files,open(getpass.getuser()+'_'+sim+'_log_files_per_student.txt','w'))
    print "The file "+getpass.getuser()+'_'+sim+'_log_files_per_student.txt has been created and pickled'
    return log_files