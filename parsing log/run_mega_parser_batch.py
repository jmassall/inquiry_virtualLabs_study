'''
author: sperez8
data: june 14 2017

This script runs the parser on cleaned log files
'''
import os
import sys
import json
import traceback
from mega_parser import *

INFOLDER = 'C:\\Users\\'+getpass.getuser()+'\\Documents\\Personal Content\\Lab_skills_study\\cleaned log data\\cleaned_and_split_'
OUTFOLDER = 'C:\\Users\\'+getpass.getuser()+'\\Documents\\Personal Content\\Lab_skills_study\\parsed log data'

# rawfiles = ['43abdd26-76bd-4fe9-9f7b-29500369038f','38663fa4-7ac5-4868-b687-82d9aa05ab37']
RAWFILES_CAPS = '38663fa4-7ac5-4868-b687-82d9aa05ab37' ##capacitors sim logs
RAWFILES_BEERS = '43abdd26-76bd-4fe9-9f7b-29500369038f' ##beers sim logs

# Use these when looking for sims with trial missing bugs
IDS = ['12345678','12345678','12665164','16136159','17576140','17655165','18866165']
DATES = ['2016-11-08_14.23.13','2016-11-08_14.23.13','2017-03-21_18.25.09','2017-03-20_16.24.32','2017-03-22_16.25.06','2017-03-28_15.29.17','2017-03-20_16.24.18']


def batch_parse(sim,infolder,outfolder,rawfilename,reparse,skipwriteout):
    in_data_path = infolder+rawfilename
    parsed_data_path = os.path.join(outfolder,'parsed_' + rawfilename)

    #create a folder for the new data files, if one doesn't already exist.
    if not os.path.exists(parsed_data_path):
        os.makedirs(parsed_data_path)

    #for each cleaned log file in the folder
    for f in os.listdir(in_data_path):
        
        filepath = os.path.join(in_data_path, f)

        if filepath.endswith(".json"):

            if "student1" in filepath:
                studentid = "student1"
                date = re.search(r'student1_([\d\-\.\_]+)\.json', filepath).group(1)
            else:
                studentid = re.search(r'_(\d{7,8})_', filepath).group(1)
                date = re.search(r'\d{7,8}_([\d\-\.\_]+)\.json', filepath).group(1)
            sim = re.search(r'log_lab-book-([a-z\-]+)', filepath).group(1)

            outname = 'dream_table_{0}_{1}_{2}.txt'.format(sim,studentid,date)
            outfilepath = os.path.join(parsed_data_path,outname)

            if studentid not in IDS or date not in DATES:
                continue

            if os.path.isfile(outfilepath) and not reparse:
                # print  "ALREADY FOUND:", outname
                continue
            else:
                print '\n', filepath

            try:
                f = open(filepath,'r')
            except Exception:
                print "File not found.\n"
                sys.exit()

            session = Session()
            session.get_session_data_from_file(filepath)
            try: 
                sim, dreamtable = mega_parser(studentid, session.events)
            except Exception, e:
                e = sys.exc_info()
                print "Parsing failed:", filepath
                print e[0]
                print e[1]
                print traceback.print_tb(e[2])
                continue
            f.close()
            
            if not skipwriteout:
                with open(outfilepath, 'w') as outfile:    
                    np.savetxt(outfile, dreamtable, delimiter='\t', fmt='%s')


def main(*argv):
    '''handles user input and runs pretty print function'''
    parser = argparse.ArgumentParser(description='This script takes parses all log files for a paticular sim')
    parser.add_argument('-beers', help='If want beers sim log file', action='store_true', default=False)
    parser.add_argument('-caps', help='If want caps sim log file', action='store_true', default=False)
    parser.add_argument('-reparse', help='Even if parsed files already exist, reparse them.', action='store_true', default=False)
    parser.add_argument('-skipwriteout', help='If want to skip writing out parsed data to disk (use for testing)', action='store_true', default=False)
    parser.add_argument('-infolder', help='Location of file', default = INFOLDER)
    parser.add_argument('-outfolder', help='Location of output file', default = OUTFOLDER)
    args = parser.parse_args()

    print '\n'

    infolder = args.infolder
    outfolder = args.outfolder
    reparse = args.reparse
    skipwriteout = args.skipwriteout

    if args.beers == args.caps:
        print "Please pick one of the sims to parse."
        sys.exit()

    if args.beers:
        sim = 'beers'
        rawfilename = RAWFILES_BEERS
    else:
        sim = 'capacitor'
        rawfilename = RAWFILES_CAPS 

    batch_parse(sim,infolder,outfolder,rawfilename,reparse,skipwriteout)

if __name__ == "__main__":
    main(*sys.argv[1:])