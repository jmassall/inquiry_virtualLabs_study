import csv
import pandas as pd
import numpy as np
from make_table_v4 import create_df
import matplotlib.pyplot as plt


if __name__ == "__main__":

	filename = 'absorbance_coded_worksheet_cleaned.csv'

	categories = ['unified', 'verbal', 'math', 'qt-bad-ql-good', 
	'qual', 'zero-outcome', 'extreme-outcome', 'unified-extremes', 'unified-slope',	'unified-zero',
	'evidence', 'irrelevant-factors', 'summary']
	metadata_headers = ['Session', 'Technical Flags', 'Comment']

	df, dfm = create_df(filename)
	students = df.index.get_level_values('Student ID').unique()
	factors = df.index.get_level_values('Factors').unique()
	atypes = df.index.get_level_values('Type').unique()

	idx = pd.IndexSlice
	# print df.loc[(slice(None), slice(None), 'p', 'Area'), :]

	problem_IDs = []
	for student in students:
		for atype in df.loc[student,:].index.get_level_values('Type').unique():
			if set(atypes) != set(df.loc[student,:].index.get_level_values('Type').unique()):
				problem_IDs = problem_IDs + [student]
				print dfm.loc[student, metadata_headers]
			for factor in factors:
				selection = idx[student, :, atype, factor]
				if ((df.loc[selection, 'unified'] == 1 ) & (df.loc[selection, 'verbal'] + df.loc[selection, 'math'] >= 0)).bool():
						df.loc[selection, 'grade'] = 3
				elif ((df.loc[selection, 'unified'] <= 0 ) & (df.loc[selection, 'verbal'] + df.loc[selection, 'math'] == 1)).bool():
						df.loc[selection, 'grade'] = 3
				elif (df.loc[selection, 'qual'] == 1 ).bool():
					df.loc[selection, 'grade'] = 2
				elif (df.loc[selection, 'summary'] > 0 ).bool():
					df.loc[selection, 'grade'] = 1
				else:
					df.loc[selection, 'grade'] = 0
	
	print len([student for student in students if student not in problem_IDs]), len(students)
	
	f, axarr = plt.subplots(1, 3, sharey=True)
	f.suptitle('Grades per factors')
	df.loc[idx[:,:,:,'Concentration'], 'grade'].groupby(level='Type').plot.hist(alpha=0.5, bins=[0,1,2,3,4], legend=True, ax=axarr[0])
	df.loc[idx[:,:,:,'Width'], 'grade'].groupby(level='Type').plot.hist(alpha=0.5, bins=[0,1,2,3,4], legend=True, ax=axarr[1])
	df.loc[idx[:,:,:,'Wavelength'], 'grade'].groupby(level='Type').plot.hist(alpha=0.5, bins=[0,1,2,3,4], legend=True, ax=axarr[2])
	axarr[0].set_title('Concentration')
	axarr[1].set_title('Width')
	axarr[2].set_title('Wavelength')
	plt.show()

	dfp = df.loc[idx[:, :, 'p'], 'grade'].reset_index().drop(['Type','Topic'], axis=1).pivot(index='Student ID', columns='Factors', values='grade')
	dfp.to_csv('gradebook_pre.csv')

	dfm = df.loc[idx[:, :, 'm'], 'grade'].reset_index().drop(['Type','Topic'], axis=1).pivot(index='Student ID', columns='Factors', values='grade')
	dfm.to_csv('gradebook_main.csv')






