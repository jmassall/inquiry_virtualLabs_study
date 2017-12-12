import csv
import pandas as pd
import numpy as np
from collections import Counter

# def add_new_entry(readCSV, df):
# 	headers = readCSV.next()
# 	data1 = readCSV.next()
# 	data2 = readCSV.next()
# 	data3 = readCSV.next()
# 	df['Student ID'] = data1[0]
# 	df['Student ID'] = data1[0]
# 	df['Student ID'] = data1[0]

# 	return df

if __name__ == "__main__":

	filename = 'IRR_data_shawna.csv'
	data = {}
	students_chk = []

	with open(filename) as csvfile:
		readCSV = csv.reader(csvfile, delimiter=',')
		for row in readCSV:
			if( row[0] == 'CAPACITORS' or row[0] == 'ABSORBANCE' ):
				activity_topic = row[0]
				headers = readCSV.next()
				nextrow = readCSV.next()
				student_id = nextrow[0]
				students_chk.append(student_id)
				factor_data1 = nextrow[5:15] + nextrow[16:22] + [nextrow[24]]
				unified_data1 = nextrow[22:24]
				nextrow = readCSV.next()
				factor_data2 = nextrow[5:15] + nextrow[16:22] + [nextrow[24]]
				nextrow = readCSV.next()
				activity_type = nextrow[0]
				factor_data3 = nextrow[5:15] + nextrow[16:22] + [nextrow[24]]
				unified_data2 = nextrow[22:24]

				factor_data = np.array([factor_data1, factor_data2, factor_data3])
				unified_data = unified_data1 + unified_data2
				if student_id not in data.keys():
					data[student_id] = {}
				if activity_topic not in data[student_id].keys():
					data[student_id][activity_topic] = {}
				if activity_type not in data[student_id][activity_topic].keys():
					data[student_id][activity_topic][activity_type] = {}

				data[student_id][activity_topic][activity_type]['factor_data'] = factor_data
				data[student_id][activity_topic][activity_type]['unified_data'] = unified_data

	types = ['p','m']
	factors = {'capacitors':['voltage','area','separation'], 'absorbance':['concentration','width','wavelength']}
	categories = ['unified', 'verbal', 'verbal-k', 'verbal-b', 'math', 'math-k', 'math-b', 'power', 'exp', 'qt-bad-ql-good', 
	'qual', 'zero-outcome', 'extreme-outcome', 'unified-extremes', 'unified-slope',	'unified-zero', 'evidence']
	metadata_headers = ['Student ID', 'Session', 'Technical Flags', 'Comment']
	unified_headers = ['unified-irrelevant-factors', 'unified-sum', 'unified-k', 'unified-b']

	# cols_cap = pd.MultiIndex.from_tuples( [ (x,y,z) for x in types for y in factors['capacitors'] for z in categories ] )
	# cols_abs = pd.MultiIndex.from_tuples( [ (x,y,z) for x in types for y in factors['absorbance'] for z in categories ] )

	# df_cap = pd.DataFrame(columns=cols_cap)
	# df_abs = pd.DataFrame(columns=cols_abs)
	# for header in metadata_headers:
	# 	df_cap[header]=""
	# 	df_abs[header]=""


	students_abs = [student for student in data.keys() if 'ABSORBANCE' in data[student].keys()]
	students_caps = [student for student in data.keys() if 'CAPACITORS' in data[student].keys()]
	print len(students_abs)
	print len(students_caps)
	# cols = pd.MultiIndex.from_tuples( [ (x,y) for x in types for y in categories ] )
	cols = categories
	rows_abs = pd.MultiIndex.from_tuples( [ (x,y) for x in students_abs for y in factors['absorbance'] ] )
	rows_caps = pd.MultiIndex.from_tuples( [ (x,y) for x in students_caps for y in factors['capacitors'] ] )

	df_abs = pd.DataFrame(index=rows_abs, columns=cols)
	df_abs.sortlevel(inplace=True)
	df_caps = pd.DataFrame(index=rows_caps, columns=cols)
	df_caps.sortlevel(inplace=True)
	# print df_abs.loc[('19089138',factors['absorbance']),'p']
	# idx = pd.IndexSlice
	# print df_abs[idx['19089138',:],:]

	# for student in data.keys():
	# 	if data[student]['topic'] == 'ABSORBANCE':
	# 		df_abs.loc[(student,factors['absorbance']),:] = data[student]['factor data']

			
	# 		print data[student][act_type]['factor_data']
	# 		print df_abs[student, act_type]

	# print df_abs
	print len(data.keys())
	print len(students_chk)
	print [k for (k,v) in Counter(students_chk).iteritems() if v > 1]
	





				




