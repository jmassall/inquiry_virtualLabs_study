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

	filename = 'IRR_data_test.csv'
	data = {}
	students_chk = []
	categories = ['unified', 'verbal', 'verbal-k', 'verbal-b', 'math', 'math-k', 'math-b', 'power', 'exp', 'qt-bad-ql-good', 
	'qual', 'zero-outcome', 'extreme-outcome', 'unified-extremes', 'unified-slope',	'unified-zero', 'evidence']

	with open(filename) as csvfile:
		readCSV = csv.reader(csvfile, delimiter=',')
		for row in readCSV:
			factor_names = []
			factor_codes = []
			unified_codes = []
			if( row[0] == 'CAPACITORS' or row[0] == 'ABSORBANCE' ):
				activity_topic = row[0]
				headers = readCSV.next()
				nextrow = readCSV.next()
				student_id = nextrow[0]
				students_chk.append(student_id)
				factor_names.append(nextrow[4])
				factor_codes.append(nextrow[5:15] + nextrow[16:22] + [nextrow[24]])
				unified_codes.append(nextrow[22:24])
				nextrow = readCSV.next()
				factor_names.append(nextrow[4])
				factor_codes.append(nextrow[5:15] + nextrow[16:22] + [nextrow[24]])
				nextrow = readCSV.next()
				activity_type = nextrow[0]
				factor_names.append(nextrow[4])
				factor_codes.append(nextrow[5:15] + nextrow[16:22] + [nextrow[24]])
				unified_codes.append(nextrow[22:24])

				if student_id not in data.keys():
					data[student_id] = {}
				if activity_topic not in data[student_id].keys():
					data[student_id][activity_topic] = {}
				if activity_type not in data[student_id][activity_topic].keys():
					data[student_id][activity_topic][activity_type] = {}
				n=0
				for factor_name in factor_names:
					data[student_id][activity_topic][activity_type][factor_name] = {}
					m=0
					for category in categories:
						data[student_id][activity_topic][activity_type][factor_name][category] = factor_codes[n][m]
						m+=1
					n+=1
				
				data[student_id][activity_topic][activity_type]['unified data'] = unified_codes

print data['11200165']['CAPACITORS']['p'].keys()
print data['11200165']['CAPACITORS']['p']['Sep'].keys()

df = pd.DataFrame.from_dict({(i,j,k,l): data[i][j][k][l] 
							for i in data.keys() 
                            for j in data[i].keys()
                            for k in data[i][j].keys()
                            for l in data[i][j][k].keys()}, 
                            orient='index')

print df


				




