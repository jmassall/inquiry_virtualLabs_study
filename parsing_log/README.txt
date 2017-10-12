This folder holds all the scripts and examples of data used to parse the log data.

**NOTE**: After a git pull, please update your parsed log files as the way they are parse may have changed. Rerun "clean_and_split_raw_data.py" to do so.


Here are all the folders and files in this folder:
----------------------------------------------------
utils.py					-	contains the Session class and other useful functions for reading and parsing log files
clean_and_split_raw_data.py	-	a script that does what it's name indicates
log_data_1_student_example.json - the first line of the raw file '5a257a80-aa82-471d-b75c-f1113f314da1.log' to view for testing purposes (in pretty print) (testing purposes)
log_lab-book-beers-law-lab_16606167.json - the file above without mouseover and time events. (testing purposes)
example_walk.txt 				- the result of using the "create walk" and "export walk" in the Session class (testing purposes) on the above file


test sim with this link
-----------------------------------
 https://phet-io.colorado.edu/sims/beers-law-lab/1.6.3-phetio/wrappers/login/login.html?wrapper=lab-book&validationRule=validateDigits&numberOfDigits=8&sim=beers-law-lab&console&publisher_id=0c82b6bf&application_id=1d0612a8397e8b1dbf4993bc58869fa1&widget_id=lab-book-beers-law-lab&phetioEmitStates=true&phetioEmitInputEvents=false
 https://phet-io.colorado.edu/sims/capacitor-lab-basics/1.4.2-phetio/wrappers/login/login.html?wrapper=lab-book&validationRule=validateDigits&numberOfDigits=8&sim=capacitor-lab-basics&console&publisher_id=0c82b6bf&application_id=1d0612a8397e8b1dbf4993bc58869fa1&widget_id=lab-book-capacitor-lab-basics&phet-io.emitStates

TO DO
-----------------
	investigate the unparsed files using error output
	add some meat to testing suite maker
	rerun testing suite maker
	check that everything is parsed the way we want it to be parsed!!!
	done :)
