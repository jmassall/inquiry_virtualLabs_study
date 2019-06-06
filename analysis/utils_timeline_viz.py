'''
author: sperez8
Here are all the functions related to loading student log data, cleaning it, parsing it and
visualizing it using a timeline visualization.
'''

import os
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import re
import seaborn as sns
import getpass
import json
from matplotlib.ticker import MultipleLocator
from itertools import chain, izip

FOLDER =  'C:\\Users\\'+getpass.getuser()+'\\Documents\\Personal Content\\Lab_study_data\\parsed log data'

def find_student_log_file(sim, studentid, date=None, infolder = FOLDER):
    studentid = str(studentid)
    if date:
        for root, dirs, files in os.walk(infolder):
            for f in files:
                if sim in f and studentid in f and date in f:
                    return os.path.join(root, f)
    else:
        for root, dirs, files in os.walk(infolder):
            for f in files:
                if sim in f and studentid in f:
                    return os.path.join(root, f)

def add_pauses(df,pause_length=9):

    def detect_pause(row,current_time,next_time):
        duration_of_action = next_time - current_time
        if duration_of_action >= pause_length:
            row['Family']='Pause'
            return row

    df['Timeshifted'] = df[['Time']].shift(-1)
    df_pauses = df.loc[df['Timeshifted']-df['Time']>=pause_length]
    df_pauses.loc[:,('User or Model')]='user'
    df_pauses.loc[:,('Event')]='Pause'
    df_pauses.loc[:,('Item')]='Pause'
    df_pauses.loc[:,('Action')]='Pause'
    df_pauses.loc[:,('Time')]=df_pauses[('Time')]+2 #shift it by 2 sec since otherwise the original event and pause have the same start time
    df = pd.concat([df,df_pauses],ignore_index=True)
    df = df.sort_values('Time')
    #Now that we added pauses, we have to recreate the time shifted column to calculate durations
    df['Timeshifted'] = df[['Time']].shift(-1)
    df['Duration'] = df['Timeshifted']-df['Time']
    df['Duration'] = df['Duration'].fillna(2) # the last duration will be NaN so we replace wiht 2 seconds
    return df

action_to_family = {'N':['editing notes'],
                    'R':['Restoring sim state from trial'],
                    'M':['recording data'],
                   'Dt':['Removing data from table'],
                    'Ga':['Adding data to graph'],
                    'Dm':['Moving trial in table'],
                    'Ge':['Selecting Y-axis','Selecting X-axis', 'Selecting scale of Y-axis','Selecting scale of X-axis'],
                    'Gr':['Removing data from graph'],
                   'I':['expanding table','collapsing table','expanding graph','collapsing graph','collapsing simulation','expanding simulation','Playing with PhET menu'],
                    'P':['Pause']}

variable_actions = ['toggle laser','dragEnded','dragged','dragStarted','Changed concentration','Changed wavelength','changed connection']


def add_family(df):
    event_to_family = {}
    for family, events in action_to_family.iteritems():
        for event in events:
            event_to_family[event]=family

    def map_event_family(event,item):
        if event in variable_actions:
            if 'plateArea' in item: return 'Va'
            elif 'switch' in item: return 'Vt'
            else:
                return 'V'+item[0]
        else:
            try:
                return event_to_family[event]
            except KeyError:
                print("New event found:",event)

    df['Family'] = df.apply(lambda row: map_event_family(row['Event'],row['Item']), axis=1)
    return df

def remove_model_events_from_df(df):
    return df[df['User or Model'] != 'model']

def prep_parsing_data(parsing_file,remove_model_events=True):
    df = pd.read_table(parsing_file, sep='\t')
    if remove_model_events:
        df = remove_model_events_from_df(df)
        if len(df)==0:
            print "The parsed file has no user events, only model events. No dataframe prepared."
            return df
        df = add_pauses(df)
        df = add_family(df)
    return df


def action_usage(df,column,regex):
    '''Given a regex, we detect its use using a particular column
    and then extract a list of time coordinates for when
    they were used. These coordinates are in the format (start_time, duration)
    
    Args:
        df (Pandas dataframe): The dataframe to search in.
        column (str): The column where the action regex might be logged (usualy the Family column)
        regex (str): The regex or often the name of the action family to search for in the column.    

    Returns:
        A list of tuples with start times of the regex and it's duration [(start1,duration1),(start2,duration2),...]
    '''
    if df[column].isnull().values.all():
        return [(0,0)]
    else:
        timecoords = zip(df[df[column].str.contains(regex,na=False)]['Time'],df[df[column].str.contains(regex,na=False)]['Duration'])
        return clean_coords(timecoords)

def clean_coords(coords_brocken_up):
    #since the coordinates all subsequent in time, we want to merge them to clean them up.
    #For example:
    # coords_brocken_up = [(0,2),(2,5),(7,2)]
    # coords -> [(0,9)]
    while True:
        coords = merge_usage(coords_brocken_up,coords_brocken_up)
        if coords == coords_brocken_up:
            return coords
        else:
            coords_brocken_up = coords

def intersect_usage(x,y):
    '''
    Given two lists of coordinates, we find the intersect of comon time coordinates and return the new coordinates.
    These coordinates are in the format (start_time, duration)
    
    Args:
        x (list): One set of coordinates
        y (list): A second set of coordinates

    Returns:
        A list of tuples with a intersect of start and duration coordinates [(start1,duration1),(start2,duration2),...]
        
    For example:
        x = [(0,1),(2,3),(10,3)] #0,2,3,4,10,11,12
        y = [(0,2),(3,1),(9,2),(12,2)] #0,1,3,9,10,12,13
        then intersect_usage(x,y) -> [(0, 1), (3, 1), (10, 1), (12, 1)] #0,3,10,12

    '''
    x.sort() #sort them by start time
    y.sort()
    intersect = []
    
    #for pairs of coordinates, we check if we can capture intersect
    while len(x) > 0 and len(y) > 0:
        (sx,dx) = x[0]
        (sy,dy) = y[0]

        if sx == sy: #if same start times, find min duration
            intersect.append((sx,min(dx,dy)))
            if dx<dy:
                x.pop(0)
            else:
                y.pop(0)             
        elif sx < sy and sx+dx > sy: # if they overlap
            if sx+dx >= sy+dy: #if one coordinate bounds the other
                intersect.append((sy,dy)) #we add that inner coordinate
                y.pop(0) #and remove it
            else: #if no bounding, then just overlap
                intersect.append((sy,dx - (sy-sx))) #add the new coordinate with latest start time
                x.pop(0) #and remove the earliest one
        elif sy < sx and sy+dy > sx: # if they overlap (opposite scenario)
            if sy+dy >= sx+dx: #if one coordinate bounds the other (opposite scenario)
                intersect.append((sx,dx)) #we add that inner coordinate
                x.pop(0) #and remove it
            else:
                intersect.append((sx,dy - (sx-sy))) #add the new coordinate with latest start time
                y.pop(0) #and remove the earliest one
        else:
            #there was no intersect so we remove the earliest coordinate
            if sx < sy:
                x.pop(0)
            else:
                y.pop(0)

    return intersect
            
def merge_usage(x,y):
    '''
    Given two lists of coordinates, we merged them and return the new coordinates.
    These coordinates are in the format (start_time, duration)
    
    Args:
        x (list): One set of coordinates
        y (list): A second set of coordinates

    Returns:
        A list of tuples with merged start and duration coordinates [(start1,duration1),(start2,duration2),...]
        
    For example:
        x = [(0,1),(2,3),(10,3)] #0,2,3,4,10,11,12
        y = [(0,2),(3,1),(9,2),(12,2)] #0,1,3,9,10,12,13
        then merged(x,y) => [(0, 2), (2, 3), (9, 5)] #0,1,2,3,4,9,10,11,12,13

    '''
    
    x = x+y #we put all the coordinates in one list
    
    x = list(set(x)) #remove duplicate coordinates
    x.sort() #sort them by start time
    
    if len(x)==1:
        return x
    
    merged = []
    
    
    #for pairs of coordinates, we check if we can merged them
    for i,(s1,d1) in enumerate(x):
        if i != len(x)-1: 
            s2,d2 = x[i+1] #get next coordinates
#             print s1,d1,s2,d2
            if s1 == s2: #if same start times, find max duration
                merged.append((s1,max(d1,d2)))
                x.remove((s2,d2))
            elif s1+d1 >= s2+d2: #if one coordinate bounds the other
                merged.append((s1,d1)) #we add that coordinate
                x.remove((s2,d2)) #and remove the other
            elif s1+d1 >= s2: # if they overlap
                new_duration = d2 + s2-s1 #we calculate a new duration
                merged.append((s1,new_duration)) #add the new coordinate with earliest start time
                x.remove((s2,d2)) #and remove the other
            else:
                merged.append((s1,d1))
        else:
            #these are the last coordinates of x and haven't been merged yet, 
            # so we try to merge them with the previous coordinates
            if s1 <= merged[-1][0]+merged[-1][1]:
                new_start = merged[-1][0]
                new_duration = d1 + s1 - merged[-1][0]
                merged[-1] = (new_start,new_duration) #extend the duration of the last coordinate
            else: #if it fails, then there is no overlap and we merge them
                merged.append((s1,d1))
    return merged



def get_record_usage(df):
    record_usage = action_usage(df,'Family','M')
    #We want record events ot be singular not episodes
    record_usage = [(time,4) for time,duration in record_usage]
    return record_usage

def axis_absorbance_usage(df):
    x_axis_usage = action_usage(df,'X axis','absorbance')
    y_axis_usage = action_usage(df,'Y axis','absorbance')
    return merge_usage(x_axis_usage,y_axis_usage)

def axis_trialNumber_usage(df):
    x_axis_usage = action_usage(df,'X axis','trialNumber')
    y_axis_usage = action_usage(df,'Y axis','trialNumber')
    return merge_usage(x_axis_usage,y_axis_usage)

def axis_width_usage(df):
    x_axis_usage = action_usage(df,'X axis','cuvetteWidth')
    y_axis_usage = action_usage(df,'Y axis','cuvetteWidth')
    return merge_usage(x_axis_usage,y_axis_usage)

def axis_concentration_usage(df):
    x_axis_usage = action_usage(df,'X axis','concentration')
    y_axis_usage = action_usage(df,'Y axis','concentration')
    return merge_usage(x_axis_usage,y_axis_usage)

def axis_charge_usage(df):
    x_axis_usage = action_usage(df,'X axis','charge')
    y_axis_usage = action_usage(df,'Y axis','charge')
    return merge_usage(x_axis_usage,y_axis_usage)

def axis_area_usage(df):
    x_axis_usage = action_usage(df,'X axis','area')
    y_axis_usage = action_usage(df,'Y axis','area')
    return merge_usage(x_axis_usage,y_axis_usage)

def axis_separation_usage(df):
    x_axis_usage = action_usage(df,'X axis','separation')
    y_axis_usage = action_usage(df,'Y axis','separation')
    return merge_usage(x_axis_usage,y_axis_usage)

def get_value_and_coords(df,variable):
    usage = action_usage(df,'Family',family_name_to_code[variable])
    values = list(df[df['Family'].str.contains(family_name_to_code[variable],na=False)][variable])
    coords = list(df[df['Family'].str.contains(family_name_to_code[variable],na=False)]['Time'])
    return values, coords, usage

def get_absorbance(df,_):
#     usage = action_usage(df,'Family',".*")
    values = list(df['Absorbance'])
    coords = list(df['Time'])
    return values, coords, None

def get_charge(df,_):
#     usage = action_usage(df,'Family',".*")
    values = list(df['Charge'])
    coords = list(df['Time'])
    return values, coords, None

def get_connection(df):
    return action_usage(df,'Connection',"LIGHT_BULB_CONNECTED")

def get_graph_add_del_coords(df,_):
    usage1 = action_usage(df,'Family',family_name_to_code['Graph add'])
    usage2 = action_usage(df,'Family',family_name_to_code['Graph remove'])
    coords = list(df['Time'])
    values = [len(get_pts(read_table(table), in_graph = True)) for table in list(df['Table'])]
    confounded = [pts_are_confounded(get_values_per_variable(get_pts(read_table(table), in_graph = True))) for table in list(df['Table'])]
    #get index of first time there are points in graph
    #only get values and coords after first points are added
    if 1 in values: #if points are ever added to graph
        i = values.index(1)
        coords = [c for j,c in enumerate(coords) if j >= i ]
        values = [v for j,v in enumerate(values) if j >= i ]
        confounded = [f for j,f in enumerate(confounded) if j >= i ]
        return values, coords, confounded, merge_usage(usage1,usage2)
    else:
        return [],[],[], merge_usage(usage1,usage2)

def axis_absorbance_trialNumber_usage(df):
    absorbance = axis_absorbance_usage(df)
    trialNumber = axis_trialNumber_usage(df)
    return intersect_usage(absorbance,trialNumber)

def axis_absorbance_width_usage(df):
    absorbance = axis_absorbance_usage(df)
    width = axis_width_usage(df)
    return intersect_usage(absorbance,width)

def axis_absorbance_concentration_usage(df):
    absorbance = axis_absorbance_usage(df)
    concentration = axis_concentration_usage(df)
    return intersect_usage(absorbance,concentration)

def axis_charge_trialNumber_usage(df):
    charge = axis_charge_usage(df)
    trialNumber = axis_trialNumber_usage(df)
    return intersect_usage(charge,trialNumber)

def axis_charge_area_usage(df):
    charge = axis_charge_usage(df)
    area = axis_area_usage(df)
    return intersect_usage(charge,area)

def axis_charge_separation_usage(df):
    charge = axis_charge_usage(df)
    separation = axis_separation_usage(df)
    return intersect_usage(charge,separation)
    
def axis_other_usage(df):
    trialNumber = axis_trialNumber_usage(df)
    concentration = axis_concentration_usage(df)
    width = axis_width_usage(df)
    combo1 = intersect_usage(width,trialNumber)
    combo2 = intersect_usage(width,concentration)
    combo3 = intersect_usage(concentration,trialNumber)
    usage = merge_usage(combo1,combo2)
    return merge_usage(combo3,usage)

def axis_scale_linear_usage(df):
    x_axis_usage = action_usage(df,'X axis scale','linear')
    y_axis_usage = action_usage(df,'Y axis scale','linear')
    return merge_usage(x_axis_usage,y_axis_usage)

def axis_scale_log_usage(df):
    x_axis_usage = action_usage(df,'X axis scale','log')
    y_axis_usage = action_usage(df,'Y axis scale','log')
    return merge_usage(x_axis_usage,y_axis_usage)

def axis_scale_inverse_usage(df):
    x_axis_usage = action_usage(df,'X axis scale','inverse')
    y_axis_usage = action_usage(df,'Y axis scale','inverse')
    return merge_usage(x_axis_usage,y_axis_usage)

def axis_change_scale_usage(df):
    x_axis_usage = action_usage(df,'Event','Selecting scale of X-axis')
    y_axis_usage = action_usage(df,'Event','Selecting scale of Y-axis')
    return merge_usage(x_axis_usage,y_axis_usage)

family_name_to_code = {'Interface':'I',
                        'Restore':'R',
                        'Pause':'P',
                        'Graph edit axes':'Ge',
                        'Graph remove':'Gr',
                        'Graph add':'Ga',
                        'Data Table delete':'Dt',
                        'Data Table move trial':'Dm',
                        'Notes':'N',
                        'Record':'M',
                        'Detector':'Vd',
                        'Wavelength':'Vw',
                        'Width':'Vc',
                        'Concentration':'Vs',
                        'Laser toggle':'Vl',
                        'Battery voltage':'Vb',
                        'Area':'Va',
                        'Separation':'Vp',
                        'Connection':'Vt',
                        }

function_to_use = {'Record':get_record_usage,
                    'Graph add/del':get_graph_add_del_coords,
                    'Abs vs. TrialNumber':axis_absorbance_trialNumber_usage,
                   'Abs vs. Concentration':axis_absorbance_concentration_usage,
                   'Abs vs. Width':axis_absorbance_width_usage,
                   'Charge vs. TrialNumber':axis_charge_trialNumber_usage,
                   'Charge vs. area':axis_charge_area_usage,
                   'Charge vs. separation':axis_charge_separation_usage,                   
                   'Other axes':axis_other_usage,
                   'Change scales':axis_change_scale_usage,
                   'Linear axis':axis_scale_linear_usage,
                   'Log axis':axis_scale_log_usage,
                   'Inverse axis':axis_scale_inverse_usage,
                  'Wavelength':get_value_and_coords,
                  'Width':get_value_and_coords,
                  'Concentration':get_value_and_coords,
                  'Lightbulb connected':get_connection,
                   'Battery voltage':get_value_and_coords,
                   'Separation':get_value_and_coords,
                   'Area':get_value_and_coords,
                   'Absorbance':get_absorbance,
                   'Charge':get_charge,
                  'Laser toggle':get_value_and_coords}

colors = {'Interface':'#969696',
            'Notes':'#f1cb2d',
            'Pause':'#f1cb2d',
            'Change scales':'#2a2d34',
            'Linear axis':'#737373',
            'Log axis':'#737373',
            'Inverse axis':'#737373',
            'Other axes':'#2a2d34',
            'Abs vs. TrialNumber':'#4a000b',
            'Abs vs. Width':'#f1cb2d',
            'Abs vs. Concentration':'#5c8dfc',
            'Graph edit axes':'#2a2d34',#'#6000fc',
            'Graph add/del':'#2a2d34',#'#6000fc',
            'Restore':'#2a2d34',#'#6000fc',
            'Data Table delete':'#2a2d34',#'#6000fc',
            'Data Table move trial':'#2a2d34',#'#6000fc',
            '':'white',
            'Record':'#2a2d34',#'#6000fc',
            'Detector':'#32883b',
            'Wavelength':'#9b0017',
            'Connection':'#9b0017',
            'Width': '#ec7d27',
            'Concentration':'#5c8dfc',
            'Laser toggle':'#e90023',
            'Battery voltage':'#ec7d27',#
            'Lightbulb connected':'#e90023',#
            'Separation':'#25b25b',#
            'Area':'#003bf7',#
            'Charge vs. TrialNumber':'#4a000b',#
            'Charge vs. separation':'#25b25b',#
            'Charge vs. area':'#003bf7',#
            'Absorbance':'#2a2d34',
            'Charge':'#2a2d34'}

to_plot_caps = ['Interface','Notes','Pause','','Log axis','Inverse axis','Linear axis','Other axes','Charge vs. TrialNumber','Charge vs. separation','Charge vs. area','Graph edit axes','Graph add/del','','Restore','Data Table delete','Data Table move trial','','Record','Lightbulb connected','Battery voltage','Separation','Area','','Charge']
to_plot_beers = ['Interface','Notes','Pause','','Log axis','Inverse axis','Linear axis','Other axes','Abs vs. TrialNumber','Abs vs. Width','Abs vs. Concentration','Graph edit axes','Graph add/del','','Restore','Data Table delete','Data Table move trial','','Record','Detector','Wavelength','Width','Concentration','Laser toggle','','Absorbance']


MIN_MAX = {'Wavelength':(380,780),
           'Width':(0.5,2.0),
           'Concentration':(0.0,200.0),
           'Absorbance':(0.0,3.84),
          'Laser toggle':(0.0,1.0),
          'Battery voltage':(-1.5,1.5),
          'Area':(100,400),
          'Separation':(2,10),
          'Charge':(-2.6562,2.6562)}


def fix_laser(values,coords):
    opp = [0.0 if v == 1.0 else 1.0 for v in values]
    newvalues = list(chain.from_iterable(izip(values,opp)))
    newcoords = list(chain.from_iterable(izip(coords,coords)))
    return newvalues,newcoords

# connection_conversion = {"BATTERY_CONNECTED":0.0,
#                          "IN_TRANSIT":0.5,
#                          "LIGHT_BULB_CONNECTED":1.0}

# def fix_connection(values,coords):
#     fixed_values = []
#     previous = "BATTERY_CONNECTED"
#     for v in values:
#         if v == "IN_TRANSIT":
#             fixed_values.append(previous)
#         else:
#             fixed_values.append(v)
#             previous = v
#     joined = zip(fixed_values,coords)
#     newjoined = [(connection_conversion[j[0]],j[1]) for j in joined]# if j[0] != "IN_TRANSIT"]
#     values, coords = zip(*newjoined)
#     opp = [0.0 if v == 1.0 else 1.0 for v in values]
#     newvalues = list(chain.from_iterable(izip(values,opp)))
#     newcoords = list(chain.from_iterable(izip(coords,coords)))
#     return newvalues,newcoords

def plot(df,to_plot,family_name_to_code,function_to_use,colors):
    ax = plt.subplot()
    spacing = 10
    margin = 0.5
    component_spacer = spacing
    n_spacer = 0
    max_time = 17*60 #max 17 min long
#     colors = sns.color_palette("hls", len(to_plot))
#     colors = sns.husl_palette(len(to_plot), l=.4, s=1)
#     sns.palplot(sns.husl_palette(len(to_plot), l=.5, s=.7))

    for i,action in enumerate(to_plot):
        alpha = 0.9
        color = colors[action]
        if action == '':
            alpha = 1
            color = 'white'
            action_use = [(0,max_time)]
        elif action  == 'Graph add/del':
            values,coords,confounded,action_use = function_to_use[action](df,action)
            if len(values)>0:
                min_v,max_v = 0.0,max(values)
                #plot legend
                ax.text(coords[0]-10,i*spacing,'0',horizontalalignment='left',fontsize=14, color=colors[action])
                ax.text(coords[-1]+2,(i+1)*spacing-2,str(max_v),horizontalalignment='left',fontsize=14, color=colors[action])
                #Add "0 points" in the values and coords
                coords.insert(0,coords[0])
                values.insert(0,0)
                norm_values = [(v-min_v)/(max_v-min_v)*(spacing-margin) +i*spacing for v in values] #normalize so it fits in x_axis
                #split confounded and non
                c_to_plot = []
                v_to_plot = []
                f_to_plot = []
                prev_conf = None
                ax.plot(coords, norm_values,'-',color=color, linewidth=1.5,alpha=1)
                ###CONFOUNDING NEEDS FIXING
                # for j,(c,v,f) in enumerate(zip(coords, norm_values, confounded)):
                #     ax.plot([c],[v],'.',color=color, linewidth=1.5,alpha=1)
                    # # print c,v,f, prev_conf
                    # if (j == len(norm_values)-1) or f != prev_conf:
                    #     if f and len(v_to_plot)>0:
                    #         ax.plot(c_to_plot,v_to_plot,'.',color=color, linewidth=1.5,alpha=1)
                    #         #FIX ME

                    #         # ax.plot(c_to_plot,v_to_plot,'.',color='red', linewidth=1.5,alpha=1)
                    #     if not f and len(v_to_plot)>0:
                    #         ax.plot(c_to_plot,v_to_plot,'.',color=color, linewidth=1.5,alpha=1)
                    # if f != prev_conf:
                    #     c_to_plot = [c]
                    #     v_to_plot = [v]
                    #     f_to_plot = [f]
                    # else:
                    #     c_to_plot.append(c)
                    #     v_to_plot.append(v)
                    #     f_to_plot.append(f)
                    # prev_conf = f

                    
                # vals_conf = [v for j,v in enumerate(norm_values) if confounded[j]]
                # vals_not = [v for j,v in enumerate(norm_values) if not confounded[j]]
                # coords_conf = [v for j,v in enumerate(coords) if confounded[j]]
                # coords_not = [v for j,v in enumerate(coords) if not confounded[j]]
                # if len(vals_conf)>0:
                #     ax.plot(coords_conf,vals_conf,'.',color='red', mew=2)#,linewidth=1.5,alpha=1)
                # if len(vals_not)>0:
                #     ax.plot(coords_not,vals_not,'.',color=color, mew=2)#,linewidth=1.5,alpha=1)
                # for v,c,f in zip(values,coords,confounded):
                #     if f:
                #         ax.plot([c],[v],'+',color='red',linewidth=1.5,alpha=1)
                #     else:
                #         ax.plot([c],[v],'+',color=color,linewidth=1.5,alpha=1)
        elif action in ['Absorbance','Wavelength','Width','Concentration','Laser toggle',
                        'Battery voltage','Separation','Area','Charge']:
            #get time coords for changes in that variable, and the values of those changes
            values,coords,action_use = function_to_use[action](df,action)
            if action == 'Laser toggle':#values for the laser toggle are actually the previous value before action so we need to fix up the values a bit
                values,coords = fix_laser(values,coords)
            # elif action == 'Connection':
            #     if np.nan == values[0]: #when no udpate states in log
            #         values,coords = fix_connection(values,coords)
            elif len(values)>0:
                #add last value ended sim with
                values.append(values[-1])
                coords.append(df['Time'].iloc[-1])
            min_v,max_v = MIN_MAX[action]
            norm_values = [(v-min_v)/(max_v-min_v)*(spacing-margin) +i*spacing for v in values] #normalize so it fits in x_axis
            ax.plot(coords,norm_values,'-',color=color,linewidth=1.5,alpha=1)
            if action == 'Charge' or action == 'Battery voltage': #show baseline around 0 to see when values are pos or negative
                ax.plot(coords,[(0-min_v)/(max_v-min_v)*(spacing-margin) +i*spacing for v in values],'-',color='white',linewidth=1.5,alpha=0.8)
            alpha = 0.3
        elif action in function_to_use.keys():
            action_use = function_to_use[action](df)   
        else:
            action_use = action_usage(df,'Family',family_name_to_code[action])
            action_use = clean_coords(action_use)
        if "vs. Concentration" in action:
            color = colors['Concentration']
        elif "vs. Width" in action:
            color = colors['Width']
        if action_use:
            if action in ['Pause','Notes']:
                a = 0.25
                ax.broken_barh(action_use,(i*spacing,(spacing)*(len(to_plot)-i)),facecolors=color,linewidth=0,edgecolor='k',alpha=a)
            elif action == 'Record':
                a = 0.25
                ax.broken_barh(action_use,(i*spacing,(spacing)*(len(to_plot)-i)),facecolors=color,linewidth=0,edgecolor='k',alpha=a)
            elif action == 'Lightbulb connected' or action == 'Graph add/del':
                alpha = 0.4
            height = (i*spacing+(n_spacer)*component_spacer,(component_spacer-margin))
            ax.broken_barh(action_use,height,facecolors=color,alpha=alpha)#,linewidth=0,edgecolor='k')

    #Shape plot
    ax.set_ylim(0, len(to_plot)*spacing+1)
    ax.set_xlim(0, max_time)
    
    #Add labels
    ax.set_xlabel('Time (min)',fontsize=20)
    ax.set_xticks(range(0,int(max_time),60))
    ax.set_xticklabels([str(x/60)+''if x in range(0,int(max_time),60*5) else "" for x in range(0,int(max_time),60)],fontsize=20)
    ax.set_xticks(range(0,int(max_time),60), minor=True)
    ax.set_xticklabels([str(x/60)+''if x not in range(0,int(max_time),60*5) else "" for x in range(0,int(max_time),60)],fontsize=14, minor=True)
    ax.set_yticks(range(0,len(to_plot)*spacing,spacing)) #for the grid
    ax.set_yticklabels(['' for p in to_plot])
    ax.set_yticks(range(spacing/2,len(to_plot)*spacing,spacing),minor=True) #minor ticks
    ax.set_yticklabels([a.capitalize() for a in to_plot],fontsize=20, minor=True)
    ax.grid(True)
    
    # ax2 = ax.twiny()
    # ax2.set_xlim(0, max_time)
    # ax2.set_xlabel('',fontsize=20)
    # ax2.set_xticks(range(0,int(max_time),60))
    # ax2.set_xticklabels([str(x/60)+''if x in range(0,int(max_time),60*5) else "" for x in range(0,int(max_time),60)],fontsize=13)
    # ax2.grid(False)


def count_pts_in_graph(table):
    return len(get_pts_in_graph(table))

def get_empty_values():
    return {"Battery voltage":set(),
                        "Area":set(),
                        "Connection":set(),
                        "Separation":set(),
                        "Width":set(),
                        "Wavelength":set(),
                        "Concentration":set(),
                        "Laser toggle":set()}
                
def get_values_per_variable(pts):
    values_per_variable = get_empty_values()
    for point in pts:
        for attribute in point.keys():
            if attribute in values_per_variable.keys():
                values_per_variable[attribute].add(point[attribute])
    return values_per_variable

def pts_are_confounded(values_per_variable):
    #check how many variables have more than 1 value
    number_of_values_varied = sum([1 if len(vals)>1 else 0 for vals in values_per_variable.values()])
    # print number_of_values_varied
    if number_of_values_varied >1:
        return True
    else:
        return False

def get_pts(table, in_graph = False, remove_bad_point = False):
    points = []
    for datapoint, attributes in table.iteritems():
        if remove_bad_point:
            if "Laser toggle" in attributes.keys():
                if attributes["Laser toggle"]==0:
                    continue
            elif "Connection" in attributes.keys():
                if attributes["Connection"]=="LIGHT_BULB_CONNECTED":
                    continue
        if not in_graph:
            points.append(attributes)
        elif attributes['visible']:
            points.append(attributes)
    return points

def read_table(table):
    return {int(k):v for k,v in json.loads(table).iteritems()}