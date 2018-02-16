import os
import pandas as pd


def find_student_log_file(infolder, sim, studentid, date=None):
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


def remove_model_events(df):
    return df[df['User or Model'] != 'model']

PAUSE_LENGTH = 15
def add_pauses(df,pause_length=PAUSE_LENGTH):

    def detect_pause(row,current_time,next_time):
        duration_of_action = next_time - current_time
        if duration_of_action >= PAUSE_LENGTH:
            row['Family']='Pause'
            return row

    df['Timeshifted'] = df[['Time']].shift(-1)
    df_pauses = df.loc[df['Timeshifted']-df['Time']>=PAUSE_LENGTH]
    df_pauses.loc[:,('User or Model')]='user'
    df_pauses.loc[:,('Event')]='Pause'
    df_pauses.loc[:,('Item')]='Pause'
    df_pauses.loc[:,('Action')]='Pause'
    df_pauses.loc[:,('Time')]=df_pauses[('Time')]+2 #shift it by 2 sec since otherwise the original event and pause have the same start time
    df = pd.concat([df,df_pauses],ignore_index=True)
    df = df.sort_values('Time')
    return df

def prep_parsing_data(parsing_file):
    df = pd.read_table(parsing_file, sep='\t')
    df = remove_model_events(df)
    df = add_pauses(df)
    df = add_family(df)
    return df


def calculate_duration(row):
    """This function gets the duration of an action given the difference in time
    between the current and next timestamp.

    Args:
        row (Pandas element): The row of the action for which we want to find the duration.

    Returns:
        duration: The difference in time in seconds between the Timeshifted and Time variables.
    """
    if notnull(row['Timeshifted']): #check that this is not the last action which will have a NA Timeshifted value
        #check that the time of the next action is indeed later than time of the current actin
        if datetime.combine(date.min, row['Timeshifted']) >= datetime.combine(date.min, row['Time']):
            duration = (datetime.combine(date.min, row['Timeshifted']) - datetime.combine(date.min, row['Time'])).total_seconds()
        else:
            #ex: this is the case when TimeSHifted is 59:00 min and Time is 02:00 min, so we add an hour to find the duration in between
            duration = (datetime.combine(date.min, row['Timeshifted']) + timedelta(hours=1) - datetime.combine(date.min, row['Time'])).total_seconds()
    else:
        duration = 10 #last action lasts zero seconds but we need to put a dummy variable here.
    return duration