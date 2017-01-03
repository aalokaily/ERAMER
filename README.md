
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
Peptide ID	Position of the C-terminus of precursor 	Trimming score, LETP = 9	Trimming score, LETP = 10	Trimming score, LETP = 11	Trimming score, LETP = 12	Trimming score, LETP = 13	Trimming score, LETP = 14	Trimming score, LETP = 15	Trimming score, LETP = 16	
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
peptide1 	9 	0.567889 	0	0	0	0	0	0	0	
peptide1 	10 	0.567889 	0.5791 	0	0	0	0	0	0	
peptide1 	11 	0.567889 	0.5791 	0.591909 	0	0	0	0	0	
peptide1 	12 	0.560778 	0.5727 	0.586091 	0.600583 	0	0	0	0	
peptide1 	13 	0.520778 	0.5727 	0.586091 	0.600583 	0.595923 	0	0	0	
peptide1 	14 	0.520778 	0.5727 	0.586091 	0.600583 	0.595923 	0.571929 	0	0	
peptide1 	15 	0.520778 	0.5727 	0.586091 	0.600583 	0.595923 	0.571929 	0.548467 	0	
peptide1 	16 	0.520778 	0.5727 	0.586091 	0.600583 	0.595923 	0.571929 	0.548467 	0.525438 	
peptide1 	17 	0.520778 	0.5727 	0.586091 	0.600583 	0.595923 	0.571929 	0.548467 	0.525438 	
peptide1 	18 	0.445556 	0.505 	0.524545 	0.544167 	0.543846 	0.523571 	0.503333 	0.483125 	
peptide1 	19 	0.485556 	0.505 	0.524545 	0.544167 	0.543846 	0.523571 	0.503333 	0.483125 	
peptide2 	9 	0.382333 	0	0	0	0	0	0	0	
peptide2 	10 	0.336778 	0.4941 	0	0	0	0	0	0	
peptide2 	11 	0.356778 	0.4941 	0.514636 	0	0	0	0	0	
peptide2 	12 	0.336333 	0.4877 	0.508818 	0.52975 	0	0	0	0	
peptide2 	13 	0.321889 	0.4877 	0.508818 	0.52975 	0.530538 	0	0	0	
peptide2 	14 	0.328222 	0.4877 	0.508818 	0.52975 	0.530538 	0.511214 	0	0	
peptide2 	15 	0.294889 	0.4634 	0.481545 	0.50475 	0.507462 	0.489786 	0.4718 	0	
peptide2 	16 	0.380444 	0.4634 	0.486727 	0.50475 	0.507462 	0.489786 	0.4718 	0.453562 	
peptide2 	17 	0.406 	0.4634 	0.486727 	0.5095 	0.507462 	0.489786 	0.4718 	0.453562 	
peptide2 	18 	0.378222 	0.4634 	0.486727 	0.5095 	0.511846 	0.489786 	0.4718 	0.453562 	
peptide2 	19 	0.393778 	0.4634 	0.486727 	0.5095 	0.511846 	0.493857 	0.4718 	0.453562 	
peptide2 	20 	0.464778 	0.4634 	0.486727 	0.5095 	0.511846 	0.493857 	0.4756 	0.453562 	
peptide2 	21 	0.415 	0.5273 	0.486727 	0.5095 	0.511846 	0.493857 	0.4756 	0.457125 	
peptide3 	9 	0.382333 	0	0	0	0	0	0	0	
peptide3 	10 	0.336778 	0.4941 	0	0	0	0	0	0	
peptide3 	11 	0.356778 	0.4941 	0.514636 	0	0	0	0	0	





--Contacts--
For more queries or questions, please contact
Anas Al-okaily, anas.al-okaily@uconn.edu


Last update: 01/2017
