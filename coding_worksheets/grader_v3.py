import csv
import pandas as pd
import numpy as np
from make_table_v4 import create_df
import matplotlib.pyplot as plt


if __name__ == "__main__":

	filename = 'absorbance_coded_worksheet_cleaned_final.csv'
	# filename = 'capacitors_coded_worksheets_cleaned.csv'
	# filename = 'extra_session_coded_worksheets_cleaned.csv'

	categories = ['unified', 'verbal', 'math', 'qt-bad-ql-good', 
	'qual', 'zero-outcome', 'extreme-outcome', 'unified-extremes', 'unified-slope',	'unified-zero',
	'evidence', 'irrelevant-factors', 'summary']
	metadata_headers = ['Student ID','Topic','Type','other id','Session','Technical Flags',	'Comment','use analysis']

	df, dfm = create_df(filename)
	students = df.index.get_level_values('Student ID').unique()
	factors = df.index.get_level_values('Factors').unique()
	atypes = df.index.get_level_values('Type').unique()
	topics = df.index.get_level_values('Topic').unique()

	idx = pd.IndexSlice
	# print df.loc[(slice(None), slice(None), 'p', 'Area'), :]

	problem_IDs = []
	for student in students:
		for topic in df.loc[student,:].index.get_level_values('Topic').unique():
			for atype in df.loc[idx[student,topic,:],:].index.get_level_values('Type').unique():
				if set(atypes) != set(df.loc[idx[student,topic,:],:].index.get_level_values('Type').unique()):
					problem_IDs = problem_IDs + [student]
					# print dfm.loc[student, metadata_headers]
				for factor in df.loc[idx[student,topic,:],:].index.get_level_values('Factors').unique():
					selection = idx[student, topic, atype, factor]
					if ((df.loc[selection, 'unified'] == 1 ) & (df.loc[selection, 'verbal'] + df.loc[selection, 'math'] >= 0)):
							df.loc[selection, 'grade'] = 3
					elif ((df.loc[selection, 'unified'] <= 0 ) & (df.loc[selection, 'verbal'] + df.loc[selection, 'math'] >= 1)):
							df.loc[selection, 'grade'] = 3
					elif (df.loc[selection, 'qual'] == 1 ):
						df.loc[selection, 'grade'] = 2
					elif (df.loc[selection, 'summary'] > 0 ):
						df.loc[selection, 'grade'] = 1
					else:
						df.loc[selection, 'grade'] = 0

					#if quant is wrong
					if ((df.loc[selection, 'verbal'] < 0) | (df.loc[selection, 'math'] < 0)):
						trap = 1
						#if qual is wrong
						if (df.loc[selection, 'qual'] < 0 ):
							#if id is wrong or undefined
							if (df.loc[selection, 'summary'] <= 0 ):
								df.loc[selection, 'grade2'] = 0
							#if id is right
							else:
								df.loc[selection, 'grade2'] = 1
						#if qual is correct
						elif (df.loc[selection, 'qual'] == 1 ):
							#if id is wrong
							if (df.loc[selection, 'summary'] < 0 ):
								df.loc[selection, 'grade2'] = 0
							#if id is right or undefined
							else:
								df.loc[selection, 'grade2'] = 2
						#if qual is undefined
						else:
							#if id is wrong or undefined
							if (df.loc[selection, 'summary'] <= 0 ):
								df.loc[selection, 'grade2'] = 0
							#if id is right
							else:
								df.loc[selection, 'grade2'] = 1

					#if quant is right
					elif ( (df.loc[selection, 'verbal'] == 1) | (df.loc[selection, 'math'] == 1) | (df.loc[selection, 'unified'] == 1) ):
						trap = 2
						#if qual is wrong
						if (df.loc[selection, 'qual'] < 0 ):
							#if id is wrong 
							if (df.loc[selection, 'summary'] < 0 ):
								df.loc[selection, 'grade2'] = 0
							#if id is right or undefined
							else:
								df.loc[selection, 'grade2'] = 1
						#if qual is correct
						elif (df.loc[selection, 'qual'] == 1 ):
							#if id is wrong
							if (df.loc[selection, 'summary'] < 0 ):
								df.loc[selection, 'grade2'] = 0
							#if id is right or undefined
							else:
								df.loc[selection, 'grade2'] = 3
						#if qual is undefined
						else:
							#if id is wrong 
							if (df.loc[selection, 'summary'] < 0 ):
								df.loc[selection, 'grade2'] = 0
							#if id is right or undefined
							else:
								df.loc[selection, 'grade2'] = 3

					#if quant is undefined
					else:
						trap = 3
						#if qual is wrong
						if (df.loc[selection, 'qual'] < 0 ):
							#if id is wrong 
							if (df.loc[selection, 'summary'] < 0 ):
								df.loc[selection, 'grade2'] = 0
							#if id is right or undefined
							else:
								df.loc[selection, 'grade2'] = 1
						#if qual is correct
						elif (df.loc[selection, 'qual'] == 1 ):
							#if id is wrong
							if (df.loc[selection, 'summary'] < 0 ):
								df.loc[selection, 'grade2'] = 0
							#if id is right or undefined
							else:
								df.loc[selection, 'grade2'] = 2
						#if qual is undefined
						else:
							#if id is wrong or undefined
							if (df.loc[selection, 'summary'] <= 0 ):
								df.loc[selection, 'grade2'] = 0
							#if id is right 
							else:
								df.loc[selection, 'grade2'] = 1
				
					if ~(df.loc[selection, 'grade'] == df.loc[selection, 'grade2']):
						print 'oh oh disagreement in grading scheme'
						print df.loc[selection, :]
						print trap


	print len([student for student in students if student not in problem_IDs]), len(students)
	
	# f, axarr = plt.subplots(1, 3, sharey=True)
	# f.suptitle('Grades per factors')

	# df.loc[idx[:,:,:,factors[0]], 'grade'].groupby(level='Type').plot.hist(alpha=0.5, bins=[0,1,2,3,4], legend=True, ax=axarr[0])
	# df.loc[idx[:,:,:,factors[1]], 'grade'].groupby(level='Type').plot.hist(alpha=0.5, bins=[0,1,2,3,4], legend=True, ax=axarr[1])
	# df.loc[idx[:,:,:,factors[2]], 'grade'].groupby(level='Type').plot.hist(alpha=0.5, bins=[0,1,2,3,4], legend=True, ax=axarr[2])
	# axarr[0].set_title(factors[0])
	# axarr[1].set_title(factors[1])
	# axarr[2].set_title(factors[2])
	# plt.show()

	dfp = df.loc[idx[:, :, 'p'], 'grade'].reset_index().drop(['Type','Topic'], axis=1).pivot(index='Student ID', columns='Factors', values='grade')
	# dfp.to_csv('gradebook_extras_pre.csv')

	dfm = df.loc[idx[:, :, 'm'], 'grade'].reset_index().drop(['Type','Topic'], axis=1).pivot(index='Student ID', columns='Factors', values='grade')
	# dfm.to_csv('gradebook_extras_main.csv')






