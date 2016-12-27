import sys
import os
import math
import random
import fileinput
from collections import defaultdict
import xlrd

All_weights = defaultdict(float)

peptide_file = sys.argv[1]     # "test.fasta"


def check_has_lower(s):
    flag = False
    for c in s:
        if c.islower():
            flag = True

    return flag

def read_PWM(xls_file):
    workbook = xlrd.open_workbook(xls_file)
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

print "Peptide ID\tPosition of 16-mers\t Expected transported peptide\t Specificity score\n-------------------------------------------------------------------------------------------"
for line in fileinput.input(peptide_file):
    tmp =  line.strip()
    #print tmp
    if tmp[0] == ">" and d == 0:
        peptide_id = tmp[1:]

    elif tmp[0] == ">" and d != 0:
        peptide_seq.upper()
        for i in range(0, len(peptide_seq) - 15):
            _16_mer = peptide_seq[i:i+16]
            #print _16_mer, len(_16_mer)
            for j in range(len(_16_mer)):
                if len(_16_mer[j:]) < 9:
                    break
                else:
                    print peptide_id, "\t", i +1, "\t", j *" ", _16_mer[j:], "\t", compute_specificty(_16_mer[j:])
        peptide_id = tmp[1:]
        peptide_seq = ""

    else:
        peptide_seq += line.strip()
        d = 1
# process the last peptide
peptide_seq.upper()
for i in range(0, len(peptide_seq) - 15):
        _16_mer = peptide_seq[i:i+16]

        for j in range(len(_16_mer)):
            if len(_16_mer[j:]) < 9:
                break
            else:
                    print peptide_id, "\t", i +1, "\t", j *" ", _16_mer[j:], "\t", compute_specificty(_16_mer[j:])

















