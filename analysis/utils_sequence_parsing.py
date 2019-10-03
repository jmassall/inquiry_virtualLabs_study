from itertools import groupby
import re

class Sequence():
#     actions = set()
#         actions.update(self.seq)
# Action = namedtuple('Action', ['action', 'target', 'sim, 'time'])

# * parameters change name or stuff
# * block -> collapse
# * merge -> change A to C; change('A','C') #method signature (input) should not be ambiguous.


    def __init__(self,seq, sid=None, sim=None, timecoords=None):
        '''Store a sequence of actions for a particular student (sid)
            in a particular simulation (sim) and optionally with 
            time coordinates for each action'''
        self.seq = seq
        self.sid = sid
        self.sim = sim
        self.timecoords = timecoords
        self.actions = set()
        self.update_actions() #save a list of unique actions
        self.blocked_actions = set()
        self.removed_actions = set()
        self.sets_merged_actions = set()
        if timecoords:
            self.check_lengths_seq_timecoords()

    def __repr__(self):
        return "Sequence({0})".format(','.join(self.seq))
    
    def update_actions(self):
        self.actions = set(self.seq)
        
    def set_timecoords(self, timecoords):
        '''Sets the time coordinates for every action in the sequence'''
        self.timecoords = timecoords
        self.check_lengths_seq_timecoords()
        return self
    
    def extend_seq(self,seq_to_add,timecoords_to_add=None):
        '''Adding actions at the end of the sequence,
            and optinally the cooresponding time coordinates'''
        self.seq.extend(seq_to_add)
        self.update_actions()
        if timecoords_to_add:
            self.extend_timecoords(timecoords_to_add)
            self.check_lengths_seq_timecoords()
        return self
    
    def extend_timecoords(self,timecoords_to_add):
        '''Adding timecoordinates'''
        self.timecoords.extend(timecoords_to_add)
        self.check_lengths_seq_timecoords()
        return self
        
    def remove_actions(self,actions_to_remove):
        '''Remove 1 action or multiple actions'''
        #check if we are removing 1 or a list of actions
        if isinstance(actions_to_remove,basestring):
            actions_to_remove = [actions_to_remove]
        self.removed_actions.update(actions_to_remove)
        
        if self.timecoords:
            zipped = zip(self.seq,self.timecoords)
            new_zipped = [(s,t) for s,t in zipped if s not in actions_to_remove]
            #unzip using map(list, _) to return a list not a tuple
            self.seq, self.timecoords = map(list, zip(*new_zipped))
            self.check_lengths_seq_timecoords()
        else:
            self.seq = [s for s in self.seq if s not in actions_to_remove]
            
        #we update the list of unique actions
        self.update_actions()
        
        #we rerun blocking of actions if it was run before
        if self.blocked_actions:
            self.block_actions(self.blocked_actions)
        return self
     
    def block_actions(self,actions_to_block=None):
        '''Block 1 or multiple actions'''
        #If none specified, block all actions
        if actions_to_block == None:
            actions_to_block = self.actions
        #If one specified, turn to a list
        elif isinstance(actions_to_block,basestring):
            actions_to_block = [actions_to_block]
        self.blocked_actions.update(actions_to_block)
        
        self.unblocked_seq = list(self.seq) #make a copy
        self.seq = []

        if self.timecoords:
            updating_timecoords = True
            self.unblocked_timecoords = list(self.timecoords)
            self.timecoords = []
        else:
            updating_timecoords = False

        #zipped = zip(self.seq,self.timecoords)
        #for key, group in groupby(zipped, lambda x: x[0]):

        i=0 #index of where we are in the sequence
        for key, group in groupby(self.unblocked_seq):
            group_copy = list(group) #make a copy because it's a generator element?
            if key in actions_to_block:
                #append the one blocked action
                self.seq.append(key)
                if updating_timecoords:
                    self.timecoords.append(self.unblocked_timecoords[i])
            else:
                #append the entire group of actions of the same type
                self.seq.extend(group_copy)
                if updating_timecoords:
                    self.timecoords.extend(self.unblocked_timecoords[i:i+len(group_copy)])
            #update index
            i = i + len(group_copy)
            
        if updating_timecoords:
            self.check_lengths_seq_timecoords()
        return self
    
    def check_lengths_seq_timecoords(self):
        '''Checks that we have a time coordinate for every aciton the sequence'''
        if len(self.seq)>len(self.timecoords):
            raise ValueError('There are more sequence actions than time coordinates')
        if len(self.seq)<len(self.timecoords):
            raise ValueError('There are more time coordinates than sequence actions')

    def merge_actions(self,actions_to_merge,merged_action_name=None):
        '''Takes list of actions and replaces each instance of
            these actions with a new name. If no name provided, use first action in list'''
        if merged_action_name == None:
            merged_action_name = actions_to_merge[0]
        if len(actions_to_merge)<2:
            raise ValueError('Please provide at least 2 actions to merge.')
        self.sets_merged_actions.add(tuple(actions_to_merge))
        self.unmerged_sequence = list(self.seq)
        self.seq = [merged_action_name if s in actions_to_merge else s for s in self.unmerged_sequence]
        
        #if merged actions were previously blocked, we rerun blocking
        if set(self.blocked_actions) & set(actions_to_merge):
            self.block_actions(self.blocked_actions)
        self.update_actions()
        return self        

    def translate_variable_actions(self):
        regex_pattern_var = re.compile('[VG\_]+(?:axis\_)?([a-z]+)')
        old_seq = list(self.seq)
        self.seq = []
        current_quant = None
        number_switches = 0 #need to track so we put
        # "Switch_quant" action at the right time coordinate
        for i,s in enumerate(old_seq):
            if 'V_' in s or 'G_axis_' in s:
                var = regex_pattern_var.match(s).group(1)
                action = s
                action = action.replace(var,'')
                if var in ['wavelength','battery']:
                    #translate qual variable
                    self.seq.append(action+'qual')
                elif var not in ['area', 'separation','width','concentration']:
                    #variable is some other (lightbulb, detector, ruler...)
                    #so we don't change the action
                    self.seq.append(action+var)
                elif current_quant == None:
                    #translate quant variable
                    #first quant variable encountered
                    current_quant = var
                    self.seq.append(action+'quant')
                elif var == current_quant:
                    #previous action and current action on same quant variable
                    self.seq.append(action+'quant')
                else:
                    #previous action and current action are different
                    # so we note the change with a new action
                    self.seq.extend(['Switch_quant',action+'quant'])
                    current_quant = var
                    #need to add a timecoord for this new "action"
                    if self.timecoords!=None:
                        self.timecoords.insert(i+number_switches,self.timecoords[i+number_switches]-0.0001)
                    number_switches += 1
            else:
                self.seq.append(s)
        self.update_actions()
        if self.timecoords!=None:
            self.check_lengths_seq_timecoords()
        return self

    def parameters(self):
        '''Prints the parameters of the sequence including previous tranformations'''
        to_print = 'Length:{} actions, sid:{}, sim:{}, blocked actions:{},'.format(len(self.seq),self.sid,self.sim,self.blocked_actions)
        to_print += 'actions removed: {}, merged_actions: {}, has timecoords: {}'.format(self.removed_actions,self.sets_merged_actions,self.timecoords!=None)
        print to_print


def run_Sequence_acless_checks():
    a = Sequence(['A','B','B','G','F','G','G','A','A','F'])
    print "\nTHE BASICS"
    print a
    print a.extend_seq('A')
    print a.remove_actions('F')
    print a.block_actions(['A','B'])
    a.parameters()
    
    print "\nTIMECOORDS"
    a.set_timecoords([1,2,3,4,5,6])
    a.extend_seq('D')
    a.extend_timecoords([7])
    a.extend_seq('D',[8])
    a.parameters()
    print a
    print a.timecoords
    a.block_actions('G')
    a.remove_actions(['D','B'])
    a.timecoords
    
    print "\nMERGING and reblocking"
    print a.extend_seq(['X','Y','Z'],timecoords_to_add=[10,20,30])
    print a.merge_actions(['A','X','Z'])
    print a.remove_actions('Y')

    print "\nTranslating qual and quant variables"  
    original = ['V_concentration','P','V_concentration','P','V_detector','P','V_concentration','P','V_width','P','V_width','T_add','V_concentration','T_add','G_axis_width','T_add','P']
    S = Sequence(original)
    S.translate_variable_actions();
    for a,b in zip(original+['-','-','-','-'],S.seq):
        print a,b

    print "\nTranslating qual and quant variables with time coordinates"  
    original = ['V_concentration','V_width','G_axis_concentration']
    coords = range(len(original))
    S = Sequence(original,timecoords=coords)
    S.translate_variable_actions();
    for a,b in zip(S.timecoords,zip(S.seq+[''],original+['','','',''])):
        print a,b


def converter(row,rules_as_dict):
    for potential_action,rule in rules_as_dict:
        match=True
        for column,value in rule.iteritems():
            if row[column]!= value:
                match=False
                break
#         if match:
#             if potential_action == 'T_add':
#                 return check_cvs_table(row)
#             if potential_action == 'G_add':
#                 return check_cvs_graph(row)
        if match:
            return potential_action
    else:
        return 'no_match_found'


def check_cvs_graph(row):
    table = json.loads(row['Table'])
    points = get_pts(table,in_graph=True) #grab all points in graph
    if len(points)==1:
        return "G_add_first"
#     if row['X axis'] not in ["charge","absorbance"] and row['Y axis'] not in ["charge","absorbance"]:
#         return "G_add_messy"
    values = get_values_per_variable(points)
    confounded = pts_are_confounded(values)
#     print points
    if not confounded and 0 not in values["Laser toggle"] and "LIGHT_BULB_CONNECTED" not in values["Connection"]:
        #We could do some complex things here to check if the right axis was chosen
#         print 'cvs!'
        return "G_add_cvs"
    else:
#         print 'not!'
        return "G_add_messy"

regex_pattern_trial = re.compile('trialNumber (\d+)')
def check_cvs_table(row):
    trial_number = int(regex_pattern_trial.match(row['Item']).group(1))
    table = json.loads(row['Table'])

    # if it's the first trial added or the table only has one trial, no possibility for doing cvs
    if trial_number == 1 or len(table)==1:
        return "T_add_first"
    else:
        current_trial = table[str(trial_number)]
        # get trials in table
        all_trial_numbers = table.keys()
        #we iterate through the other trials and check if there is cvs with the current trial
        i=0
        while len(all_trial_numbers)>0:
            some_trial_number = all_trial_numbers.pop()
            if str(some_trial_number) == str(trial_number):
                continue
#                 print some_trial_number, trial_number
            some_trial = table[str(some_trial_number)]
            #we make sets of the all the values of variables between both trials
            values_of_2_points = get_values_per_variable([current_trial, some_trial])
            confounded = pts_are_confounded(values_of_2_points)
            outcomes = get_outcome_values([current_trial, some_trial])
            outcome1,outcome2 = outcomes[0],outcomes[1]
            #we check that only one variable is changed (confounded = False)
            # that the laser was not off, and that the connection wasn't to lightbulb
            # and that the outcome values are not null but floats
            if not confounded and 0 not in values_of_2_points["Laser toggle"] and "LIGHT_BULB_CONNECTED" not in values_of_2_points["Connection"] and isinstance(outcome1, float) and isinstance(outcome2, float):
                return "T_add_cvs"
        return "T_add_messy"


# PARSER FOR CONSECTUIVE TABLE ACTIONS
# regex_pattern_trial = re.compile('trialNumber (\d+)')
# def check_cvs_table(row):
#     if row['Sequence Action']=='table_add':
#         trial_number = int(regex_pattern_trial.match(row['Item']).group(1))
#         table = json.loads(row['Table'])

#         # if it's the first trial added or the table only has one trial, no possibility for doing cvs
#         if trial_number == 1 or len(table)==1:
#             return "table_add_first"
#         else:
#             #the last trial added in table (that still is in table and wasn't deleted) will have the greatest trial number
#             last_trial_number = max([int(key) for key in table.keys() if int(key)!=trial_number])
#             current_trial = table[str(trial_number)]
#             last_trial = table[str(last_trial_number)]
#     #         print trial_number, last_trial_number
#             #we make sets of the all the values of variables between both trials
#             values_of_2_points = get_values_per_variable([current_trial, last_trial])
#     #         print values_of_2_points
#             confounded = pts_are_confounded(values_of_2_points)
#             outcomes = get_outcome_values([current_trial, last_trial])
#             outcome1,outcome2 = outcomes[0],outcomes[1]
#             #we check that only one variable is changed (confounded = False)
#             # that the laser was not off, and that the connection wasn't to lightbulb
#             # and that the outcome values are not null but floats
#             if not confounded and 0 not in values_of_2_points["Laser toggle"] and "LIGHT_BULB_CONNECTED" not in values_of_2_points["Connection"] and isinstance(outcome1, float) and isinstance(outcome2, float):
#                 return "table_add_cvs"
#             else:
#                 return "table_add_messy"
#     else: return row['Sequence Action']