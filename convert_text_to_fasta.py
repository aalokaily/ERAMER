import sys
import os
import fileinput

peptide_file = sys.argv[1]

for line in fileinput.input(peptide_file):
    tmp =  line.strip().split("\t")
    print ">" + tmp[0]
    print tmp[0]
    
    