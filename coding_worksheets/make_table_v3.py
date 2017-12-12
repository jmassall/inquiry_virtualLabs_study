import csv
import pandas as pd
import numpy as np
from collections import Counter

def create_df(filename):
	data = {}
	unified_data = {}
	metadata = {}
	students_chk = []

	categories = ['unified', 'verbal', 'verbal-k', 'verbal-b', 'math', 'math-k', 'math-b', 'power', 'exp', 'qt-bad-ql-good', 
	'qual', 'zero-outcome', 'extreme-outcome', 'unified-extremes', 'unified-slope',	'unified-zero', 
	'evidence', 'summary']
	metadata_headers = ['Student ID', 'Session', 'Technical Flags', 'Comment']
	unified_categories = ['unified-irrelevant-factors', 'unified-sum', 'unified-b', 'unified-k']

	with open(filename) as csvfile:
		readCSV = csv.reader(csvfile, delimiter=',')
		for row in readCSV:
			factor_names = []
			factor_codes = []
			unified_codes = []
			metadata_info =[]
			identified = []
			if( row[0] == 'CAPACITORS' or row[0] == 'ABSORBANCE' ):
				activity_topic = row[0]
				headers = readCSV.next()
				nextrow = readCSV.next()
				metadata_info = nextrow[0:4]
				student_id= nextrow[0]
				#concatenate instead of append
				students_chk.append(student_id)
				factor_names.append(nextrow[4])
				factor_codes.append(nextrow[5:15] + nextrow[16:22] + [nextrow[24]])
				unified_codes = nextrow[22:24]
				nextrow = readCSV.next()
				factor_names.append(nextrow[4])
				factor_codes.append(nextrow[5:15] + nextrow[16:22] + [nextrow[24]])
				nextrow = readCSV.next()
				activity_type = nextrow[0]
				factor_names.append(nextrow[4])
				factor_codes.append(nextrow[5:15] + nextrow[16:22] + [nextrow[24]])
				#puts 'control centre' value in array, important to see the identified value
				factor_codes[0] = factor_codes[0] + [nextrow[1]]
				factor_codes[1] = factor_codes[1] + [nextrow[2]]
				factor_codes[2] = factor_codes[2] + [nextrow[3]]

				unified_codes = unified_codes + nextrow[22:24]

				#check if student already exists
				if student_id not in data.keys():
					data[student_id] = {}
					unified_data[student_id] = {}
					metadata[student_id] = {}
				#if student exists, check if activity topic exists
				if activity_topic not in data[student_id].keys():
					data[student_id][activity_topic] = {}
					unified_data[student_id][activity_topic] = {}
					metadata[student_id][activity_topic] = {}
				#if student and topic already exist, then create empty dictionary for the other type
				if activity_type not in data[student_id][activity_topic].keys():
					data[student_id][activity_topic][activity_type] = {}
					unified_data[student_id][activity_topic][activity_type] = {}
					metadata[student_id][activity_topic][activity_type] = {}

				#build dictionary, can probably make a nested list comprehension here
				n=0
				for factor_name in factor_names:
					data[student_id][activity_topic][activity_type][factor_name] = {}
					m=0
					for category in categories:
						data[student_id][activity_topic][activity_type][factor_name][category] = factor_codes[n][m]
						m+=1
					n+=1
				unified_data[student_id][activity_topic][activity_type] = {header:uc for (header, uc) in zip(unified_categories, unified_codes)}
				metadata[student_id][activity_topic][activity_type] = {header:mi for (header, mi) in zip(metadata_headers, metadata_info)}


	df = pd.DataFrame.from_dict({(i,j,k,l): data[i][j][k][l] 
								for i in data.keys() 
	                            for j in data[i].keys()
	                            for k in data[i][j].keys()
	                            for l in data[i][j][k].keys()}, 
	                            orient='index')
	names = ['Student ID', 'Topic', 'Type', 'Factors']
	df.index.set_names(names, inplace=True)

	dfu = pd.DataFrame.from_dict({(i,j,k): unified_data[i][j][k] 
								for i in unified_data.keys() 
	                            for j in unified_data[i].keys()
	                            for k in unified_data[i][j].keys()}, 
	                            orient='index')
	namesu = ['Student ID', 'Topic', 'Type']
	dfu.index.set_names(namesu, inplace=True)

	dfm = pd.DataFrame.from_dict({(i,j,k): metadata[i][j][k] 
								for i in metadata.keys() 
	                            for j in metadata[i].keys()
	                            for k in metadata[i][j].keys()}, 
	                            orient='index')

	#get rid of empty spaces
	df.replace('', 0, inplace=True)
	dfu.replace('', 0, inplace=True)

	#making everything numbers
	df = df.apply(pd.to_numeric, errors='ignore')
	dfu = dfu.apply(pd.to_numeric, errors='ignore')

	#reorder columns
	df = df[categories]
	dfu = dfu[unified_categories]
	
	return df, dfu, dfm

if __name__ == "__main__":

	filename = 'IRR_data_test.csv'
	# filename = 'IRR_data_shawna.csv'

	df, dfu, dfm = create_df(filename)

	# print df.head()
	print df.dtypes
	

	# print df.loc[('27630167','CAPACITORS')]
	# print dfu.loc[('27630167','CAPACITORS')]
	# print dfm.loc['27630167']
				




