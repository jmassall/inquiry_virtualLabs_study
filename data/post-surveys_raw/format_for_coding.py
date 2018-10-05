# -*- coding: utf-8 -*-
import csv
import pandas as pd
import numpy as np


if __name__ == "__main__":

	# filename = 'responses_Absorbance-assessment-1LC_downloaded_4.3.2017_mod'
	# sim = 1
	# sim_topic = 'Absorbance'

	# filename = 'responses_Capacitance-assessment-1CL_downloaded_4.3.2017_mod'
	# sim = 1
	# sim_topic = 'Capacitance'

	# oldnames = ['[id] Please write your assigned #:              ',
	# '[open1] How did you go about learning physics through the virtual lab?',
	# '[open2] What worked well? What would you do differently next time?']

	# filename = 'responses_Absorbance-assessment-2CL_downloaded_4.3.2017_mod'
	# sim = 2
	# sim_topic = 'Absorbance'

	filename = 'responses_Capacitance-assessment-2LC_downloaded_4.3.2017_mod'
	sim = 2
	sim_topic = 'Capacitance'

	oldnames = ['[id] Please write your assigned #:              ',
	'[open1] How did you go about learning physics through the virtual lab? How was it different in this second virtual lab?',
	'[open2] What worked well? What would you do differently next time?']

	df = pd.read_csv(filename+'.csv')
	print df.columns
	newnames = ['Student ID', '1','2']
	rename_map = {oldname:newname for (oldname, newname) in zip(oldnames, newnames)}
	df1 = df.loc[:,oldnames]
	# df1["blah"] = ""
	# df1["blahblah"] = ""
	df1.rename(mapper=rename_map, axis='columns',inplace=True)
	df2 = pd.melt(df1, id_vars=['Student ID'], var_name='Q', value_name='Statement')
	df2 = df2.sort_values(['Student ID', 'Q'])
	df2['Sim'] = sim
	df2['Sim Topic'] = sim_topic
	df2.set_index(['Student ID', 'Sim', 'Sim Topic', 'Q'], inplace=True)
	print df2.head()
	df2.to_csv(filename+'_reshaped.csv', sep=',')
