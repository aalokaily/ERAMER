
# ERAMER tool
This tool predicts a score for trimming a given peptide by ERAP1 enzyme. The score can be in range from -1 to 1, where 1 indicates high possibility for trimming by ERAP1 enzyme and -1 indicates the opposite. 

----------------------------------Software version ----------------------------------

Version 1.0.0.

----------------------------------Prerequisite----------------------------------
- Python v2.7.6. 
- xlrd package at https://pypi.python.org/pypi/xlrd.

----------------------------------Installation----------------------------------

The tool is built using python; there is no need for installation.

PWM.xlsx must be stored in the same directory of the python script (the tables in the PWM.xlsx file were not embedded inside the python script so that the PWMs can be modified more easily in future). 


----------------------------------Running ERAMER Tool---------------------------

Run the command: 
```python
python ERAMER.py [fasta file]
```
Where fasta file contain the peptides/precursor sequences in fasta format. 

----------------------------------Output formats--------------------------------

The following columns will be outputted:
```
Precursor ID
Precursor sequence
Expected length of epitope	
Average of scores	
Trimming score of precursor 16	
Trimming score of precursor 15	
Trimming score of precursor 14	
Trimming score of precursor 13	
Trimming score of precursor 12	
Trimming score of precursor 11	
Trimming score of precursor 10	
Trimming score of precursor 9
```

----------------------------------Samples test---------------------------------

Running the following command given that "test.fasta" is sample fasta file that is provided in the github package: 

```python
python ERAMER.py test.fasta 
```

will output the following:
```
Precursor ID	Precursor sequence	Expected length of epitope	Average of scores	Trimming score of precursor 16	Trimming score of precursor 15	Trimming score of precursor 14	Trimming score of precursor 13	Trimming score of precursor 12	Trimming score of precursor 11	Trimming score of precursor 10	Trimming score of precursor 9
peptide1	GGGGGVVVVVVAAAEE	8	0.085322875	0.082079	0.102341	0.098547	0.05217	0.060521	0.069076	0.085425	0.132424
peptide1	GGGGGVVVVVVAAAEE	9	0.0785941428571	0.082079	0.102341	0.098547	0.05217	0.060521	0.069076	0.085425
peptide1	GGGGGVVVVVVAAAEE	10	0.0774556666667	0.082079	0.102341	0.098547	0.05217	0.060521	0.069076
peptide2	GGGGGVVVVVVVVVVVVVVVVVVVV	length is not within length range. The length of precursor that typically processed by ERAP1 enzyme is 9-16aa.
peptide3	GGGGGVVVVVV	8	0.0386456666667	0.025999	0.050784	0.039154
peptide3	GGGGGVVVVVV	9	0.0383915	0.025999	0.050784
peptide3	GGGGGVVVVVV	10	0.025999	0.025999
peptide4	GGGGGVVV''VVV	contains non-amino-acidic content.
peptide5	LLLLLLLLLLLAAAAA	8	0.273310375	0.302437	0.297252	0.291327	0.282246	0.259116	0.251543	0.238311	0.264251
peptide5	LLLLLLLLLLLAAAAA	9	0.274604571429	0.302437	0.297252	0.291327	0.282246	0.259116	0.251543	0.238311
peptide5	LLLLLLLLLLLAAAAA	10	0.2806535	0.302437	0.297252	0.291327	0.282246	0.259116	0.251543
```

Note that for each precursor, the tool will compute the specificity for each expected epitope length 8, 9, and 10. For validation process (which was performed in the paper) or in case epitope/s are known, add (in the fasta file) each epitope associated with a precursor and place it next to the precursor separated by tab (\t). Then, for each precursor the specificity will be computed where the expected epitope-length is the length of the given epitope (not 8, 9, and 10). The specificity therefore will be computed as the average value of the specificities in PWM of amino acids from position 0 to position L - Y - 1 in the precursor where position 0 is the amino acid at the N terminus of the precursor, L is the length of the precursor, and Y is the length of epitope next to the precursor.

----------------------------------Contacts----------------------------------

For more queries or questions, please contact
Anas Al-okaily, anas.al-okaily@uconn.edu


Last update: 01/2023
