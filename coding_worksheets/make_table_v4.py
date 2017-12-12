import csv
import pandas as pd
import numpy as np
from collections import Counter

def create_df(filename):
	data = {}
	unified_data = {}
	metadata = {}
	students_chk = []

	categories = ['unified', 'verbal', 'math', 'qt-bad-ql-good', 
	'qual', 'zero-outcome', 'extreme-outcome', 'unified-extremes', 'unified-slope',	'unified-zero',
	'evidence', 'irrelevant-factors', 'summary']
	metadata_headers = ['Session', 'Technical Flags', 'Comment']

	with open(filename) as csvfile:
		readCSV = csv.reader(csvfile, delimiter=',')
		for row in readCSV:
			factor_names = []
			factor_codes = []
			metadata_info =[]
			identified = []
			if( row[0] == 'CAPACITORS' or row[0] == 'ABSORBANCE' ):
				activity_topic = row[0]
				headers = readCSV.next()
				nextrow = readCSV.next()
				metadata_info = nextrow[1:4]
				student_id= nextrow[0]
				students_chk.append(student_id)
				factor_names.append(nextrow[4])
				irr_factor_num = nextrow[16]
				factor_codes.append(nextrow[5:9] + nextrow[10:16] + [nextrow[17]])
				nextrow = readCSV.next()
				factor_names.append(nextrow[4])
				factor_codes.append(nextrow[5:9] + nextrow[10:16] + [nextrow[17]])
				nextrow = readCSV.next()
				activity_type = nextrow[0]
				factor_names.append(nextrow[4])
				factor_codes.append(nextrow[5:9] + nextrow[10:16] + [nextrow[17]])
				#puts 'control centre' value in array, important to see the identified value
				#every factor gets same value for irrelevant factor, not sure where else to put it
				factor_codes[0] = factor_codes[0] + [irr_factor_num] + [nextrow[1]] 
				factor_codes[1] = factor_codes[1] + [irr_factor_num] + [nextrow[2]]
				factor_codes[2] = factor_codes[2] + [irr_factor_num] + [nextrow[3]]

				skip_student = False
				#check if student already exists
				if student_id not in data.keys():
					data[student_id] = {}
					metadata[student_id] = {}
				#if student exists, check if activity topic exists
				if activity_topic not in data[student_id].keys():
					data[student_id][activity_topic] = {}
					metadata[student_id][activity_topic] = {}
				#if student and topic already exist, then create empty dictionary for the other type
				if activity_type not in data[student_id][activity_topic].keys():
					data[student_id][activity_topic][activity_type] = {}
					metadata[student_id][activity_topic][activity_type] = {}
				else:
					print('Duplicate student activity found.')
					print student_id, activity_topic, activity_type
					# exit()
					skip_student = True

				#build dictionary, can probably make a nested list comprehension here
				if not skip_student:
					n=0
					for factor_name in factor_names:
						data[student_id][activity_topic][activity_type][factor_name] = {}
						m=0
						for category in categories:
							data[student_id][activity_topic][activity_type][factor_name][category] = factor_codes[n][m]
							m+=1
						n+=1
					metadata[student_id][activity_topic][activity_type] = {header:mi for (header, mi) in zip(metadata_headers, metadata_info)}


	df = pd.DataFrame.from_dict({(i,j,k,l): data[i][j][k][l] 
								for i in data.keys() 
	                            for j in data[i].keys()
	                            for k in data[i][j].keys()
	                            for l in data[i][j][k].keys()}, 
	                            orient='index')
	names = ['Student ID', 'Topic', 'Type', 'Factors']
	df.index.set_names(names, inplace=True)

	dfm = pd.DataFrame.from_dict({(i,j,k): metadata[i][j][k] 
								for i in metadata.keys() 
	                            for j in metadata[i].keys()
	                            for k in metadata[i][j].keys()}, 
	                            orient='index')
	names = ['Student ID', 'Topic', 'Type']
	dfm.index.set_names(names, inplace=True)

	#get rid of empty spaces
	df.replace('', 0, inplace=True)

	#making everything numbers
	df = df.apply(pd.to_numeric, errors='ignore')

	#reorder columns
	df = df[categories]
	dfm = dfm[metadata_headers]
	
	return df, dfm


if __name__ == "__main__":

	# filename = 'IRR_data_test2.csv'
	# filename = 'IRR_data_shawna.csv'


	# print df.head()
	# print df.dtypes
	

	# print df.loc[('27630167','CAPACITORS')]
	# print dfu.loc[('27630167','CAPACITORS')]
	# print dfm.loc['27630167']
				




