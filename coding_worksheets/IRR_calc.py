import csv
import pandas as pd
import numpy as np
from make_table_v3 import create_df


if __name__ == "__main__":

	# filename = 'IRR_data_test.csv'
	filename1 = 'IRR_data_shawna.csv'
	filename2 = 'IRR_data_jonathan.csv'
	nozero = False

	categories = ['unified', 'verbal', 'verbal-k', 'verbal-b', 'math', 'math-k', 'math-b', 'power', 'exp', 'qt-bad-ql-good', 
	'qual', 'zero-outcome', 'extreme-outcome', 'unified-extremes', 'unified-slope',	'unified-zero', 
	'summary']
	metadata_headers = ['Student ID', 'Session', 'Technical Flags', 'Comment']
	unified_categories = ['unified-irrelevant-factors', 'unified-sum', 'unified-b', 'unified-k']

	df1, dfu1, dfm1 = create_df(filename1)
	df2, dfu2, dfm2 = create_df(filename2)

	# df2 = df.copy()
	df1.rename(columns={header:header + '_S' for header in df1.columns}, inplace = True)
	df2.rename(columns={header:header + '_J' for header in df2.columns}, inplace = True)

	#check if students match
	# print df1.shape
	# print df2.shape
	students1 = df1.index.get_level_values('Student ID').unique()
	students2 = df2.index.get_level_values('Student ID').unique()
	print [v for v in students1 if v not in students2]
	print [v for v in students2 if v not in students1]

	# collapse multi-index dataframe back to normal dataframe
	df1.reset_index(inplace=True)
	df2.reset_index(inplace=True)
	df = pd.merge(df1, df2)
	IRR_dict = {}
	IRR_kappa_dict = {}
	for category in categories:
		print category
		if nozero:
			tab = pd.crosstab(df[category + '_J'][df[category + '_J'] != 0], 
					df[category + '_S'][df[category + '_S'] != 0]) 
			print tab
			try:
				tab_margins = pd.crosstab(df[category + '_J'][df[category + '_J'] != 0], 
					df[category + '_S'][df[category + '_S'] != 0], margins = True)
				print tab
				agree = 0
				common_entries = list(set(tab.columns) & set(tab.index))
				# if nozero:
				# 	common_entries = [n for n in common_entries if n != 0]
				for entry in common_entries:
					# print tab[entry][entry]
					agree += tab[entry][entry]
				IRR_dict[category] = agree/float(tab_margins['All']['All'])
			except:
				IRR_dict[category] = 0
				pass
		else:
			tab = pd.crosstab(df[category + '_J'], df[category + '_S'])
			tab_margins = pd.crosstab(df[category + '_J'], df[category + '_S'], margins = True)
			print tab_margins
			agree = 0
			expected = 0
			common_entries = list(set(tab.columns) & set(tab.index))
			
			N = float(tab_margins['All']['All'])
			for entry in common_entries:
				agree += tab[entry][entry]
				expected += tab_margins[entry]['All']*tab_margins['All'][entry] / N
				print agree, expected	

			IRR_dict[category] = agree/N
			IRR_kappa_dict[category] = (agree - expected)/(N - expected)

	print IRR_dict
	print IRR_kappa_dict


	# for student in students1:
	# 	for atopic in df1.loc[student, :].index.get_level_values('Topic').unique():
	# 		for atype in df1.loc[(student, atopic), :].index.get_level_values('Type').unique():
	# 			print dfm1.loc[(student, atopic, atype), ['Student ID', 'Session']],'\n'
	# 			for factor in df1.loc[(student, atopic, atype), :].index.get_level_values('Factors').unique():
	# 				agree = list(df1.loc[(student, atopic, atype, factor),:] == df2.loc[(student, atopic, atype, factor),:])
	# 				disagree = [not item for item in agree]
	# 				if any(disagree):
	# 					print factor, 'Conflicting tags:', list(df1.columns[disagree])
	# 					print '1st coder says:', list(df1.loc[(student, atopic, atype, factor), disagree])
	# 					print '2nd coder says:', list(df2.loc[(student, atopic, atype, factor), disagree]) 






