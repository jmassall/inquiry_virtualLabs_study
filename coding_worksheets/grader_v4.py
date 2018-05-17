import csv
import pandas as pd
import numpy as np
from make_table_v4 import create_df
import matplotlib.pyplot as plt


if __name__ == "__main__":

	# filename = 'coded_worksheet_test.csv'
	# filename = 'absorbance_coded_worksheet_cleaned_final.csv'
	# filename = 'capacitors_coded_worksheets_cleaned_final.csv'
	filename = 'extra_session_coded_worksheets_cleaned.csv'

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
	data = {}
	for student in students:
		data[student] = {}
		for topic in df.loc[student,:].index.get_level_values('Topic').unique():
			data[student][topic] = {}
			if set(topics) != set(df.loc[student,:].index.get_level_values('Topic').unique()):
					problem_IDs = problem_IDs + [student]
					print 'missing topic for ', student
			for atype in df.loc[idx[student,topic,:],:].index.get_level_values('Type').unique():
				data[student][topic][atype] = {}
				if set(atypes) != set(df.loc[idx[student,topic,:],:].index.get_level_values('Type').unique()):
					problem_IDs = problem_IDs + [student]
					print 'missing type for ', student
				for factor in df.loc[idx[student,topic,:],:].index.get_level_values('Factors').unique():
					data[student][topic][atype][factor] = {}
					selection = idx[student, topic, atype, factor]
					data[student][topic][atype][factor]['quant'] = np.nan
					data[student][topic][atype][factor]['qual'] = np.nan
					data[student][topic][atype][factor]['ident'] = np.nan
					if ((df.loc[selection, 'unified'] != 0 ) | (df.loc[selection, 'verbal'] != 0 ) | (df.loc[selection, 'math'] != 0 )):
						if ((df.loc[selection, 'unified'] == 1 ) & (df.loc[selection, 'verbal'] >= 0 ) & (df.loc[selection, 'math'] >=0 )):
							data[student][topic][atype][factor]['quant'] = 1
						elif ((df.loc[selection, 'verbal'] == 1 ) & (df.loc[selection, 'unified'] >= 0 ) & (df.loc[selection, 'math'] >=0 )):
							data[student][topic][atype][factor]['quant'] = 1
						elif ((df.loc[selection, 'math'] == 1 ) & (df.loc[selection, 'unified'] >= 0 ) & (df.loc[selection, 'verbal'] >=0 )):
							data[student][topic][atype][factor]['quant'] = 1
						else:
							data[student][topic][atype][factor]['quant'] = 0
					if (df.loc[selection, 'qual'] != 0 ):
						if (df.loc[selection, 'qual'] == 1 ):
							data[student][topic][atype][factor]['qual'] = 1
						else:
							data[student][topic][atype][factor]['qual'] = 0
					if (np.abs(df.loc[selection, 'summary']) == 1 ):
						if (df.loc[selection, 'summary'] == 1 ):
							data[student][topic][atype][factor]['ident'] = 1
						elif (df.loc[selection, 'summary'] == -1 ):
							data[student][topic][atype][factor]['ident'] = 0
						

dft = pd.DataFrame.from_dict({(i,j,k,l): data[i][j][k][l] 
								for i in data.keys() 
	                            for j in data[i].keys()
	                            for k in data[i][j].keys()
	                            for l in data[i][j][k].keys()}, 
	                            orient='index')

dft = dft.reset_index()
model_types = ['qual', 'ident', 'quant']
ws_id = ['Student ID', 'Topic', 'Type', 'Factors']
dft.columns = ws_id+model_types
dft = dft.melt(id_vars = ws_id, value_vars = model_types, var_name = ['Model'], value_name = 'Correct')
# print dft
dft.to_csv('extra_coded_with_model-type.csv', sep=',', index=False)








