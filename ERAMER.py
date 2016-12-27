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

peptide_file =  sys.argv[1]


def check_has_lower(s):
    flag = False
    for c in s:
        if c.islower():
            flag = True

    return flag

def read_PWM(xls_file):
    try :
        workbook = xlrd.open_workbook(xls_file)
    except:
        print "Please store the PWM.xlsx file in the script's directory"
        sys.exit(1) 
        
    ID = ""
    for length_peptide in [9, 10, 11, 12, 13, 14, 15, 16]:
        worksheet = workbook.sheet_by_name('Length ' + str(length_peptide))
        for row in range(1, 21):
            for col in range(2, 2 + length_peptide):
                ID = str(length_peptide)+ "_" + worksheet.cell(rowx=row,colx=1).value + "_" + str(col - 1)
                All_weights[ID] = worksheet.cell(rowx=row,colx=col).value
                #print ID, worksheet.cell(rowx=row,colx=col).value

        All_weights[str(length_peptide) + "_length_weight"] = worksheet.cell(rowx=24,colx=2).value
        #print length_peptide, worksheet.cell(rowx=24,colx=2).value


def compute_specificty(a):
    l = len(a)
    spec = 0
    for i in range(len(a)):
        if str(l) + "_" + a[i] + "_" + str(i + 1) in All_weights:
            spec += All_weights[str(l) + "_" + a[i] + "_" + str(i + 1)]
            #print All_weights[str(l) + "_" + a[i] + "_" + str(i + 1)]
        else:
            return "non-amino-acidic content"

    spec = float(spec)/l + All_weights[str(l) + "_length_weight"]
    #print All_weights[str(l) + "_length_weight"]
    return round(spec, 6)




read_PWM("PWM.xlsx")

#read fasta line per line

d = 0
peptide_id = ""
peptide_seq = ""

print "Peptide ID\tPosition of the N-terminus of precursor \tExpected transported precursor (lengths 9-16)\tTrimming score\n--------------------------------------------------------------------------------------------------------------------------------"
for line in fileinput.input(peptide_file):
    tmp =  line.strip()
    #print tmp
    if tmp[0] == ">" and d == 0:
        peptide_id = tmp[1:]

    elif tmp[0] == ">" and d != 0:
        peptide_seq.upper()
        for i in range(0, len(peptide_seq) - 9):
            for prec_length in [9, 10, 11, 12, 13, 14, 15, 16]:
                mer = peptide_seq[i:i+prec_length]
                if len(mer)  == prec_length:
                    print peptide_id, "\t", i + 1, "\t", prec_length, "\t", mer, (16 - prec_length) * " ", "\t", compute_specificty(mer)

        peptide_id = tmp[1:]
        peptide_seq = ""

    else:
        peptide_seq += line.strip()
        d = 1
# process the last peptide

peptide_seq.upper()
for i in range(0, len(peptide_seq) - 9):
    for prec_length in [9, 10, 11, 12, 13, 14, 15, 16]:
        mer = peptide_seq[i:i+prec_length]
        if len(mer)  == prec_length:
            print peptide_id, "\t", i + 1, "\t", prec_length, "\t", mer, (16 - prec_length) * " ", "\t", compute_specificty(mer)

















