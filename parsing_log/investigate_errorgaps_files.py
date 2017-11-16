import os
import json
import sys
import getpass

datapath = 'C:\\Users\\'+getpass.getuser()+'\Documents\\CTLT stuff\\new raw logs\\NewErrorGaps\\'
outpath =  'C:\\Users\\'+getpass.getuser()+'\Documents\\CTLT stuff\\new raw logs\\NewErrorGaps\\'
rawfile = 'CLB_requested_10-27-2017_0c82b6bf_errorGaps.json' #all logs - caps
# rawfile = 'BBL_requested_10-27-2017_0c82b6bf_errorGaps.json' #all logs beers

i = 0
with open(os.path.join(datapath+rawfile),'r') as f:
    #each line is a session which we load as a json element
    for line in f:
        line_json=json.loads(line)
        i += 1
        # print >> open("first_error_gap_line.txt",'w'), json.dumps(line_json, indent=4, sort_keys=True)
        # sys.exit()
print i