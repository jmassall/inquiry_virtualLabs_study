This folder holds all the scripts and examples of data used to parse the log data.

**NOTE**: After a git pull, please update your parsed log files as the way they are parse may have changed. Rerun "clean_and_split_raw_data.py" to do so.


Here are all the folders and files in this folder:
----------------------------------------------------
utils.py					-	contains the Session class and other useful functions for reading and parsing log files
clean_and_split_raw_data.py	-	a script that does what it's name indicates
log_data_1_student_example.json - the first line of the raw file '5a257a80-aa82-471d-b75c-f1113f314da1.log' to view for testing purposes (in pretty print) (testing purposes)
log_lab-book-beers-law-lab_16606167.json - the file above without mouseover and time events. (testing purposes)
example_walk.txt 				- the result of using the "create walk" and "export walk" in the Session class (testing purposes) on the above file

