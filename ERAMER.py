
import sys
import os
import math
import random
import fileinput
from collections import defaultdict
import xlrd

All_weights = defaultdict(float)

if len(sys.argv) != 2:
    print "Please provide a fasta file"
    sys.exit(1)

precursor_file = sys.argv[1]


def read_PWM(xls_file):
    try :
        workbook = xlrd.open_workbook(xls_file)
    except:
        print "Please store the PWM.xlsx file in the script's directory"
        sys.exit(1)

    ID = ""
    for length_precursor in [9, 10, 11, 12, 13, 14, 15, 16]:
        worksheet = workbook.sheet_by_name('Length ' + str(length_precursor))
        for row in range(1, 21):
            for col in range(2, 2 + length_precursor):
                ID = str(length_precursor)+ "_" + worksheet.cell(rowx=row,colx=1).value + "_" + str(col - 1)
                All_weights[ID] = worksheet.cell(rowx=row,colx=col).value

       
def compute_specificty(a):
    l = len(a)
    spec = 0
    for i in range(len(a)):
        spec += All_weights[str(l) + "_" + a[i] + "_" + str(i + 1)]
        #print All_weights[str(l) + "_" + a[i] + "_" + str(i + 1)]

    spec = float(spec)/l + All_weights[str(l) + "_length_weight"]
    #print All_weights[str(l) + "_length_weight"]
    return round(spec, 6)


read_PWM("PWM.xlsx")

#read fasta line per line

d = 0
precursor_id = ""
precursor_seq = ""

print "Precursor ID\tPrecursor sequence\tExpected length of epitope\tAverage of scores\tTrimming score of precursor 16\tTrimming score of precursor 15\tTrimming score of precursor 14\tTrimming score of precursor 13\tTrimming score of precursor 12\tTrimming score of precursor 11\tTrimming score of precursor 10\tTrimming score of precursor 9"


for line in fileinput.input(precursor_file):
    tmp =  line.strip()

    #print tmp
    if tmp[0] == ">":
        precursor_id = tmp[1:]

    elif tmp[0] != ">":
        tmp = tmp.split("\t")
        if len(tmp) == 1:
            epitope_lengths = [8, 9, 10]
        else:
            epitope_lengths = [len(tmp[1])]
            
        precursor_seq = tmp[0].strip().upper()
        prec_length = len(precursor_seq)
            
        if not (9 <= prec_length <= 16):
            print precursor_id + "\t" + precursor_seq + "\t" + "length is not within length range. The length of precursor that typically processed by ERAP1 enzyme is 9-16aa."
        else:
            f = ""
            for i in range(prec_length):
                if str(prec_length) + "_" + precursor_seq[i] + "_" + str(i + 1) not in All_weights:
                    f = "non-amino-acidic content"
                    break
            
            if f == "non-amino-acidic content":
                print precursor_id + "\t" + precursor_seq + "\t" + "contains non-amino-acidic content."
            
            else:
                for epitope_length in epitope_lengths:
                    scores = []
                    for l in range(prec_length, epitope_length, -1):
                        mer = precursor_seq[-1 * l:]
                        scores.append(compute_specificty(mer))
                    
                    if scores:
                        print precursor_id + "\t" + precursor_seq + "\t" + str(epitope_length) + "\t" + str(sum(scores)/len(scores)) + "\t" + "\t".join(str(x) for x in scores) 
                    else:
                        print
        
        
            
            
                
        precursor_id = ""
        precursor_seq = ""

