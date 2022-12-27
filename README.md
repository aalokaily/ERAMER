
ERAMER tool version 1.0
This tool predictes a score for trimming a given peptide by ERAP1 enzyme.

--Software version--
This is version 1.0.0.

--Prerequisite--
Python v2.7.6. 
xlrd package at https://pypi.python.org/pypi/xlrd. Or, you may use the binary executable version of the tool where there is no need to install this package.  

--Installation--
The tool is built using python; there is no need for installation.
PWM.xlsx must be stored in the same directory of the python script. 

Note: if there are diffculties in installing the xlrd package, please use the provided binary executable version of the tool as the following: uncompress the file "Binary_version/binary_executable.zip", then run the the tool using ./dist/ERAMER.exe file.  

--Running ERAMER Tool--
Run the command: 
python ERAMER.py [fasta file]
Where fasta file contain the peptides/precursor sequences in fasta format 

In case the binary executable version is used, then run the command:
./binary_executable/dist/ERAMER.exe [fasta file]

 
-Output formats--
The output will be rows with the following column format:
Peptide ID: The ID (fasta header) of the peptide.
Position of the C-terminus of precursor: The position, in the peptide, of the C-terminus of the expected precursor. 
Trimming score, LETP = x: Trimming score when the length of the expeced transpoted precursor (LETP) is x, where position x is the N-terminus position and position 1 is the fixed C-terminus position. 


--Samples test--
Running the following command given that "test.fasta" is sample fasta file that is provided in the github package: 
python ERAMER.py test.fasta 

or the following command in case the binary executable version is used:
./binary_executable/dist/ERAMER.exe test.fasta

will output the following:



--Contacts--
For more queries or questions, please contact
Anas Al-okaily, anas.al-okaily@uconn.edu


Last update: 01/2023
