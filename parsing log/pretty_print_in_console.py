'''
author: sperez8
data: june 14 2017

Script takes a cleaned log file and pretty prints it to facilitate parsing
'''
import sys
import os
import json
import getpass
import argparse

INFOLDER_BEERS =  'C:\\Users\\'+getpass.getuser()+'\\Documents\\Personal Content\\Lab_skills_study\\cleaned log data'
INFOLDER_CAPS =  'C:\\Users\\'+getpass.getuser()+'\\Documents\\Personal Content\\Lab_skills_study\\cleaned log data'
OUTFOLDER = 'C:\\Users\\'+getpass.getuser()+'\\git\\inquiry_virtualLabs_study\\parsing log'

def find_student_log_file(infolder, sim, studentid):
    for root, dirs, files in os.walk(infolder):
        for f in files:
            if sim in f and studentid in f:
                return os.path.join(root, f)

def pretty_print_cleaned_file(raw_file_path,output_file):
    ''' opens a raw data file, grabs the first line and outputs
     it in pretty print format in a new file.'''

    out = open(output_file, "w") 

    data = []
    with open(raw_file_path,'r') as f:
        for line in f:
            try:
                line_json=json.loads(line)
                print >> out, json.dumps(line_json, indent=4, sort_keys=True)
            except:
                pass
            break

    f.close()
    out.close()
    return None


def main(*argv):
    '''handles user input and runs pretty print function'''
    parser = argparse.ArgumentParser(description='TScript takes a cleaned log file and pretty prints it to facilitate parsing')
    parser.add_argument('-id', help='Student id')
    parser.add_argument('-beers', help='If want beers sim log file', action='store_true', default=False)
    parser.add_argument('-caps', help='If want caps sim log file', action='store_true', default=False)
    parser.add_argument('-infolder', help='Location of file', default = '')
    parser.add_argument('-outfolder', help='Location of output file', default = OUTFOLDER)
    args = parser.parse_args()

    print '\n'

    infolder = args.infolder
    outfolder = args.outfolder
    studentid = args.id

    if args.beers == args.caps:
        print "Please pick one of the sims to parse."
        sys.exit()

    if infolder == '':
        if args.beers:
            infolder = INFOLDER_BEERS
        else:
            infolder = INFOLDER_CAPS

    if args.beers:
        sim = 'beers'
    else:
        sim = 'capacitor'

    print "Pretty printing log file for student", studentid, "for sim", sim, "in folder ", infolder
    
    #find the right file
    in_file_path = find_student_log_file(infolder, sim, studentid)
    out_file_path = os.path.join(outfolder, 'pretty_print_copy_'+ in_file_path.split('\\')[-1] )

    #now we pretty print it into the output folder
    pretty_print_cleaned_file(in_file_path,out_file_path)
    print "Output in ", outfolder
    print '\n'

if __name__ == "__main__":
    main(*sys.argv[1:])