import pandas as pd

def compare_df(df1_, df2_, calculate_IRR = True, exclude = [], verbose = False):
	
	if exclude:
		new_columns = [column for column in df1_.columns if column not in exclude]
		df1 = df1_[new_columns]
		df2 = df2_[new_columns]
	else:
		df1 = df1_
		df2 = df2_

	number_students, number_categories = df1.shape
	IRR_nonorm = 0

	for student in list(df1.index):
		agree = list(df1.loc[student,:] == df2.loc[student,:])
		disagree = [not item for item in agree]
		if calculate_IRR:
			student_IRR = sum(agree)/float(number_categories)
			IRR_nonorm += student_IRR
		if verbose:
			if (any(disagree)):
				print '\nFor Student ID:', df1_.loc[student, 'Student ID']
				if calculate_IRR:
					print 'Student IRR is:', student_IRR
				print 'Conflicting tags:', list(df1.columns[disagree])
				print '1st coder says:', list(df1.loc[student, disagree])
				print '2nd coder says:', list(df2.loc[student, disagree])
		
		
	if calculate_IRR:
		IRR = IRR_nonorm/float(number_students) 
		return number_students, number_categories, IRR


if __name__ == "__main__":

	#this tests the above function with dummy dataframes
	d1 = {'Student ID' : [12345678, 234543453, 34565436, 4564565634, 87788798],
		'Session #' : [2, 2, 2, 2, 2],
		'voltage-highest-level' : [1, 3, 3, 2, ''], 
		'area-highest-level' : ['', 1, 3, 3, 1],
		'sep-highest-level' : [0, 3, 1, 2, 0]}

	d2 = {'Student ID' : [12345678, 234543453, 34565436, 4564565634, 87788798],
		'Session #' : [2, 2, 2, 2, 2], 
		'voltage-highest-level' : [2, 3, 3, 2, 2], 
		'area-highest-level' : [1, 1, 3, 3, 0],
		'sep-highest-level' : [0, 3, 1, 2, 0]}

	df1 = pd.DataFrame(d1)
	df2 = pd.DataFrame(d2)
	# df1 = pd.read_csv('filepath')

	# print df1
	# print df2
	
	student_metadata = ['Student ID', 'Session #']
	all_categories = [column for column in list(df1.columns) if column not in student_metadata]

	#check for metadata differences between coders
	compare_df(df1, df2, exclude = all_categories, calculate_IRR = False, verbose = True)

	#calculate IRR
	number_students, number_categories, IRR = compare_df(df1, df2, exclude = student_metadata)
	print 'Total IRR for {0} students over {2} categories is: {1}'.format(number_students, IRR, number_categories)
	


	