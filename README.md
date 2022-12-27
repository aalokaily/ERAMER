
# ERAMER tool
This tool predictes a score for trimming a given peptide by ERAP1 enzyme.


----------------------------------Software version ----------------------------------

Version 1.0.0.

----------------------------------Prerequisite----------------------------------
- Python v2.7.6. 
- xlrd package at https://pypi.python.org/pypi/xlrd.

----------------------------------Installation----------------------------------

The tool is built using python; there is no need for installation.
PWM.xlsx must be stored in the same directory of the python script. 


----------------------------------Running ERAMER Tool---------------------------

Run the command: 
```python
python ERAMER.py [fasta file]
```
Where fasta file contain the peptides/precursor sequences in fasta format 

 

----------------------------------Output formats--------------------------------



----------------------------------Samples test---------------------------------

Running the following command given that "test.fasta" is sample fasta file that is provided in the github package: 

```python
python ERAMER.py test.fasta 
```

will output the following:



----------------------------------Contacts----------------------------------

For more queries or questions, please contact
Anas Al-okaily, anas.al-okaily@uconn.edu


Last update: 01/2023
