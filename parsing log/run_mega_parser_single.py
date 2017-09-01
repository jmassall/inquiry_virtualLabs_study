'''
author: sperez8
data: june 14 2017

Script takes a cleaned log file and parses it
'''
import sys
import os
import json
import getpass
import argparse
from mega_parser import *
from utils import find_student_log_file

INFOLDER =  'C:\\Users\\'+getpass.getuser()+'\\Documents\\Personal Content\\Lab_skills_study\\cleaned log data'
OUTFOLDER = 'C:\\Users\\'+getpass.getuser()+'\\git\\inquiry_virtualLabs_study\\parsing log'

def main(*argv):
    '''handles user input and runs pretty print function'''
    parser = argparse.ArgumentParser(description='This Script takes a cleaned log file and parses it')
    parser.add_argument('-id', help='Student id')
    parser.add_argument('-date', help='Date in format YYYY-MM-DD_hh.mm.ss',default=None)
    parser.add_argument('-beers', help='If want beers sim log file', action='store_true', default=False)
    parser.add_argument('-caps', help='If want caps sim log file', action='store_true', default=False)
    parser.add_argument('-infolder', help='Location of file', default = INFOLDER)
    parser.add_argument('-outfolder', help='Location of output file', default = OUTFOLDER)
    args = parser.parse_args()

    print '\n'

    infolder = args.infolder
    outfolder = args.outfolder
    studentid = args.id

    if args.beers == args.caps:
        print "Please pick one of the sims to parse."
        sys.exit()

    if args.beers:
        sim = 'beers'
    else:
        sim = 'capacitor'

    if args.date:
        date =args.date
        print "Parsing log file for student", studentid, "for sim", sim,"for date", date, "in folder ", infolder
    else:
        print "Parsing log file for student", studentid, "for sim", sim, "in folder ", infolder
    
    #find the right file
    in_file_path = find_student_log_file(infolder, sim, studentid, date=date)
    if date==None:
        date = re.search(r'\d{7,8}_([\d\-\.\_]+)\.json', in_file_path).group(1)
    out_file = 'dream_table_{0}_{1}_{2}.txt'.format(sim,studentid,date)

    with open(in_file_path,'r') as f:
        session = Session()
        session.get_session_data_from_file(in_file_path)
        sim, dreamtable = mega_parser(studentid, session.events)
        f.close()
    
    with open(out_file, 'w') as out_file_path:    
        np.savetxt(out_file_path, dreamtable, delimiter='\t', fmt='%s')

    print "Output in ", outfolder
    print '\n'

if __name__ == "__main__":
    main(*sys.argv[1:])
