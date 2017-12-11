import pandas as pd

def compare_df(df1_, df2_, categories, exclude = [], verbose = False):
	
	if exclude:
		new_columns1 = [column for column in df1_.columns if column not in exclude]
		df1 = df1_[new_columns1]
		new_columns2 = [column for column in df2_.columns if column not in exclude]
		df2 = df2_[new_columns2]
	else:
		df1 = df1_
		df2 = df2_

	df = pd.merge(df1, df2, on='Student ID')

	IRR_dict = {}
	for category in categories:
		tab = pd.crosstab(df[category + '_JMA'], df[category + '_AM'])
		tab_margins = pd.crosstab(df[category + '_JMA'], df[category + '_AM'], margins = True)
		agree = 0
		for entry in list(tab.columns):
			print tab[entry][entry]
			agree += tab[entry][entry]
		print tab
		IRR_dict[category] = agree/float(tab_margins['All']['All'])

	return IRR_dict


if __name__ == "__main__":

	#this tests the above function with dummy dataframes
	d1 = {'Student ID' : [12345678, 234543453, 34565436, 4564565634, 87788798],
		'Session #' : [2, 2, 2, 2, 2],
		'voltage-highest-level' : [1, 3, 3, 2, 0], 
		'area-qual' : [0, 1, -1, 1, 1],
		'voltage-qual' : [0, 1, -1, 1, 1]
		}

	d2 = {'Student ID' : [12345678, 234543453, 34565436, 4564565634, 87788798],
		'Session #' : [2, 2, 2, 2, 2], 
		'voltage-highest-level' : [2, 3, 3, 2, 2], 
		'area-qual' : [1, 1, -1, 0, 0],
		'voltage-qual' : [0, 1, 1, 1, 1]
		}

	df1 = pd.DataFrame(d1)
	df2 = pd.DataFrame(d2)
	# df1 = pd.read_csv('filepath_to_JMA')
	# df2 = pd.read_csv('filepath_to_AM')

	student_ID = ['Student ID']
	student_metadata = ['Session #']
	coding_aids = ['voltage-highest-level']
	categories = [column for column in list(df1.columns) if column not in student_ID+student_metadata+coding_aids]
	
	df1.rename(columns={category:category + '_JMA' for category in categories}, inplace = True)
	df2.rename(columns={category:category + '_AM' for category in categories}, inplace = True)
	
	#calculate IRR
	IRR = compare_df(df1, df2, ['voltage-qual'], exclude = student_metadata+coding_aids)
	# print IRR
	
	


	