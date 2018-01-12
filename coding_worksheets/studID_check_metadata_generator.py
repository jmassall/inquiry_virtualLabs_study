import csv
import pandas as pd
import numpy as np
from make_table_v4 import create_df
import matplotlib.pyplot as plt


if __name__ == "__main__":

	# filename = 'absorbance_coded_worksheet_cleaned.csv'
	# filename = 'capacitors_coded_worksheets_cleaned.csv'
	filename = 'extra_session_coded_worksheets_cleaned.csv'

	categories = ['unified', 'verbal', 'math', 'qt-bad-ql-good', 
	'qual', 'zero-outcome', 'extreme-outcome', 'unified-extremes', 'unified-slope',	'unified-zero',
	'evidence', 'irrelevant-factors', 'summary']
	metadata_headers = ['Session', 'Technical Flags', 'Comment']

	#create_df automatically spits out duplicates when it finds them
	df, dfm = create_df(filename)
	students = df.index.get_level_values('Student ID').unique()
	factors = df.index.get_level_values('Factors').unique()
	atypes = df.index.get_level_values('Type').unique()
	topics = df.index.get_level_values('Topic').unique()

	idx = pd.IndexSlice

	#next and last thing to check for are students that don't have exactly "m" and "p" in their index for activity type
	#these are usually because of coder and/or student typos on worksheets resulting in the same student being split in different entries
	problem_students = []
	for student in students:
		for topic in df.loc[student,:].index.get_level_values('Topic').unique():
			for atype in df.loc[idx[student,topic,:],:].index.get_level_values('Type').unique():
				if set(atypes) != set(df.loc[idx[student,topic,:],:].index.get_level_values('Type').unique()):
					problem_students = problem_students + [student]
					print dfm.loc[idx[student,:,:], :]

	no_problem_students = [student for student in students if student not in problem_students]
	dfm.loc[no_problem_students, 'use analysis'] = True
	if problem_students:
		dfm.loc[problem_students, 'use analysis'] = False

	dfm.loc[:, 'other id'] = dfm.index.get_level_values('Student ID')
	new_metadata_headers = ['other id','Session', 'Technical Flags', 'Comment','use analysis']

	# dfp = df.loc[idx[:, :, 'p'], 'grade'].reset_index().drop(['Type','Topic'], axis=1).pivot(index='Student ID', columns='Factors', values='grade')
	dfm[new_metadata_headers].to_csv('extra_session_coded_worksheets_metadata.csv')