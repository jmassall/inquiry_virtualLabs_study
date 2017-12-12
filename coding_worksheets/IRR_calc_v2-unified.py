import csv
import pandas as pd
import numpy as np
from make_table_v3 import create_df


if __name__ == "__main__":

	# filename = 'IRR_data_test.csv'
	filename1 = 'IRR_data_shawna.csv'
	filename2 = 'IRR_data_jonathan.csv'

	# i ommited 'evidence' and 'summary' here since we don't care about that
	unified_categories = ['unified', 'verbal', 'verbal-k', 'verbal-b', 'math', 'math-k', 'math-b', 'power', 'exp', 'qt-bad-ql-good', 
	'qual', 'zero-outcome', 'extreme-outcome', 'unified-extremes', 'unified-slope',	'unified-zero', 'evidence', 'summary']
	metadata_headers = ['Student ID', 'Session', 'Technical Flags', 'Comment']
	categories = ['unified-irrelevant-factors', 'unified-sum', 'unified-b', 'unified-k']

	dfu1, df1, dfm1 = create_df(filename1)
	dfu2, df2, dfm2 = create_df(filename2)

	df1.rename(columns={header:header + '_1' for header in df1.columns}, inplace = True)
	df2.rename(columns={header:header + '_2' for header in df2.columns}, inplace = True)
	categories1 = [header + '_1' for header in categories]
	categories2 = [header + '_2' for header in categories]

	print df1.head()

	#check if students match
	if (df1.shape != df2.shape):
		print df1.shape
		print df2.shape
		print('Dataframe sizes don\'t match!')
		
	students1 = df1.index.get_level_values('Student ID').unique()
	students2 = df2.index.get_level_values('Student ID').unique()
	nonunique1 = [v for v in students1 if v not in students2]
	nonunique2 = [v for v in students2 if v not in students1]
	if nonunique1+nonunique2:
		print nonunique1
		print nonunique2
		print('Student IDs don\'t match!')
	
	# student = '0561164'
	# atopic = 'ABSORBANCE'
	# atype = 'p'
	# factor = 'Concentration'
	# # category = 
	# print df1.loc[(student, atopic, atype, factor), categories1]
	# print df2.loc[(student, atopic, atype, factor), categories2]
	# agree = list(df1.loc[(student, atopic, atype, factor), categories1] == df2.loc[(student, atopic, atype, factor), categories2])
	# disagree = [not item for item in agree]
	# print list(df1.columns[disagree])
	 

	# #print all disagreements
	# disagreement_cnt = 0
	# for student in students1:
	# 	atopics = df1.loc[student, :].index.get_level_values('Topic').unique()

	# 	for atopic in atopics:
	# 		atypes = df1.loc[(student, atopic), :].index.get_level_values('Type').unique()

	# 		for atype in atypes:
	# 			factors = df1.loc[(student, atopic, atype), :].index.get_level_values('Factors').unique()
	# 			newActivity = True

	# 			for factor in factors:
	# 				agree = list(df1.loc[(student, atopic, atype, factor), categories1] == df2.loc[(student, atopic, atype, factor), categories2])
	# 				disagree = [not item for item in agree]

	# 				if any(disagree):
	# 					if newActivity:
	# 						print '\n\n', dfm1.loc[(student, atopic, atype), ['Student ID', 'Session']], '\n'
	# 						newActivity = False
	# 						disagreement_cnt += 1
	# 					print factor, 'Conflicting categories:', list(df1.columns[disagree])
	# 					print '1st coder says:', list(df1.loc[(student, atopic, atype, factor), disagree])
	# 					print '2nd coder says:', list(df2.loc[(student, atopic, atype, factor), disagree]) 

	# print '\n', 'Disagreement count is', disagreement_cnt
	print '\n', 'IRR STATS:', '\n'
	# print summary statistics of IRR
	# collapse multi-index dataframe back to normal dataframe
	df1.reset_index(inplace=True)
	df2.reset_index(inplace=True)
	df = pd.merge(df1, df2)
	IRR_percent_dict = {}
	IRR_kappa_dict = {}
	for category in categories:
		print category.upper()
		tab = pd.crosstab(df[category + '_1'], df[category + '_2'])
		tab_margins = pd.crosstab(df[category + '_1'], df[category + '_2'], margins = True)
		print tab_margins
		agree = 0
		expected = 0
		common_entries = list(set(tab.columns) & set(tab.index))
		
		N = float(tab_margins['All']['All'])
		for entry in common_entries:
			agree += tab[entry][entry]
			expected += tab_margins[entry]['All']*tab_margins['All'][entry] / N
			# print agree, expected	
		
		IRR_percent_dict[category] = agree/N
		IRR_kappa_dict[category] = (agree - expected)/(N - expected)

		print 'Percent agreement  =', IRR_percent_dict[category]
		print 'Cohen\'s kappa =', IRR_kappa_dict[category], '\n'





