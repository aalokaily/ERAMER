
ERAMER tool version 1.0
This tool calculates the score of trimming a given peptide by ERAP1 enzyme

--Software version--
This is version 1.0.0.

--Prerequisite--
Python v2.7.6. 
xlrd package at https://pypi.python.org/pypi/xlrd. Or, you may use the binary executable version of the tool where there is no need to install this package.  

--Installation--
The tool is built using python; there is no need for installation.
PWM.xlsx must be stored in the same directory of the python script. 

Note: if there are diffculties in installing the xlrd package, please use the provided binary executable version of the tool as the following: uncompress the file "binary_executable.rar", then run the the tool using ./binary_executable/dist/ERAMER.exe .  

--Running ERAMER Tool--
Run the command: 
python ERAMER.py [fasta file]
Where fasta file contain the peptides/precursor sequences in fasta format 

In case the binary executable version is used, then run the command:
./binary_executable/dist/ERAMER.exe [fasta file]


-Output formats--
The output will be rows with the following column format:
Peptide ID: The ID (fasta header) of the peptide.
Position of the N-terminus of precursor: The position, in the peptide, of the N-terminus of the expected Position of the N-terminus of precursor. 
Expected transported precursor (lengths 9-16): enumerating the expected 9-16 lengths of the precursors while the N-terminus is fixed.   
Trimming score: prediction score of trimming by ERAP1 enzyme. 


--Samples test--
Running the following command given that "test.fasta" is sample fasta file that is provided in the github package: 
python ERAMER.py test.fasta 

or the following command in case the binary executable version is used:
./binary_executable/dist/ERAMER.exe test.fasta

will output the following:

Peptide ID	Position of the N-terminus of precursor 	Expected transported precursor (lengths 9-16)	Trimming score
--------------------------------------------------------------------------------------------------------
peptide1 	1 	9 	LLLLLLLLL         	0.567889
peptide1 	1 	10 	LLLLLLLLLL        	0.5791
peptide1 	1 	11 	LLLLLLLLLLL       	0.591909
peptide1 	1 	12 	LLLLLLLLLLLA      	0.600583
peptide1 	1 	13 	LLLLLLLLLLLAA     	0.595923
peptide1 	1 	14 	LLLLLLLLLLLAAA    	0.571929
peptide1 	1 	15 	LLLLLLLLLLLAAAA   	0.548467
peptide1 	1 	16 	LLLLLLLLLLLAAAAA  	0.525438
peptide1 	2 	9 	LLLLLLLLL         	0.567889
peptide1 	2 	10 	LLLLLLLLLL        	0.5791
peptide1 	2 	11 	LLLLLLLLLLA       	0.586091
peptide1 	2 	12 	LLLLLLLLLLAA      	0.600583
peptide1 	2 	13 	LLLLLLLLLLAAA     	0.595923
peptide1 	2 	14 	LLLLLLLLLLAAAA    	0.571929
peptide1 	2 	15 	LLLLLLLLLLAAAAA   	0.548467
peptide1 	2 	16 	LLLLLLLLLLAAAAAA  	0.525438
peptide1 	3 	9 	LLLLLLLLL         	0.567889
peptide1 	3 	10 	LLLLLLLLLA        	0.5727
peptide1 	3 	11 	LLLLLLLLLAA       	0.586091
peptide1 	3 	12 	LLLLLLLLLAAA      	0.600583
peptide1 	3 	13 	LLLLLLLLLAAAA     	0.595923
peptide1 	3 	14 	LLLLLLLLLAAAAA    	0.571929
peptide1 	3 	15 	LLLLLLLLLAAAAAA   	0.548467
peptide1 	3 	16 	LLLLLLLLLAAAAAAC  	0.483125
peptide1 	4 	9 	LLLLLLLLA         	0.560778
peptide1 	4 	10 	LLLLLLLLAA        	0.5727
peptide1 	4 	11 	LLLLLLLLAAA       	0.586091
peptide1 	4 	12 	LLLLLLLLAAAA      	0.600583
peptide1 	4 	13 	LLLLLLLLAAAAA     	0.595923
peptide1 	4 	14 	LLLLLLLLAAAAAA    	0.571929
peptide1 	4 	15 	LLLLLLLLAAAAAAC   	0.503333
peptide1 	4 	16 	LLLLLLLLAAAAAACC  	0.483125
peptide1 	5 	9 	LLLLLLLAA         	0.520778
peptide1 	5 	10 	LLLLLLLAAA        	0.5727
peptide1 	5 	11 	LLLLLLLAAAA       	0.586091
peptide1 	5 	12 	LLLLLLLAAAAA      	0.600583
peptide1 	5 	13 	LLLLLLLAAAAAA     	0.595923
peptide1 	5 	14 	LLLLLLLAAAAAAC    	0.523571
peptide1 	5 	15 	LLLLLLLAAAAAACC   	0.503333
peptide1 	6 	9 	LLLLLLAAA         	0.520778
peptide1 	6 	10 	LLLLLLAAAA        	0.5727
peptide1 	6 	11 	LLLLLLAAAAA       	0.586091
peptide1 	6 	12 	LLLLLLAAAAAA      	0.600583
peptide1 	6 	13 	LLLLLLAAAAAAC     	0.543846
peptide1 	6 	14 	LLLLLLAAAAAACC    	0.523571
peptide1 	7 	9 	LLLLLAAAA         	0.520778
peptide1 	7 	10 	LLLLLAAAAA        	0.5727
peptide1 	7 	11 	LLLLLAAAAAA       	0.586091
peptide1 	7 	12 	LLLLLAAAAAAC      	0.544167
peptide1 	7 	13 	LLLLLAAAAAACC     	0.543846
peptide1 	8 	9 	LLLLAAAAA         	0.520778
peptide1 	8 	10 	LLLLAAAAAA        	0.5727
peptide1 	8 	11 	LLLLAAAAAAC       	0.524545
peptide1 	8 	12 	LLLLAAAAAACC      	0.544167
peptide1 	9 	9 	LLLAAAAAA         	0.520778
peptide1 	9 	10 	LLLAAAAAAC        	0.505
peptide1 	9 	11 	LLLAAAAAACC       	0.524545
peptide1 	10 	9 	LLAAAAAAC         	0.445556
peptide1 	10 	10 	LLAAAAAACC        	0.505
peptide2 	1 	9 	GGGGGVVVV         	0.382333
peptide2 	1 	10 	GGGGGVVVVV        	0.4941
peptide2 	1 	11 	GGGGGVVVVVV       	0.514636
peptide2 	1 	12 	GGGGGVVVVVVA      	0.52975
peptide2 	1 	13 	GGGGGVVVVVVAA     	0.530538
peptide2 	1 	14 	GGGGGVVVVVVAAA    	0.511214
peptide2 	1 	15 	GGGGGVVVVVVAAAE   	0.4718
peptide2 	1 	16 	GGGGGVVVVVVAAAEE  	0.453562
peptide2 	2 	9 	GGGGVVVVV         	0.336778
peptide2 	2 	10 	GGGGVVVVVV        	0.4941
peptide2 	2 	11 	GGGGVVVVVVA       	0.508818
peptide2 	2 	12 	GGGGVVVVVVAA      	0.52975
peptide2 	2 	13 	GGGGVVVVVVAAA     	0.530538
peptide2 	2 	14 	GGGGVVVVVVAAAE    	0.489786
peptide2 	2 	15 	GGGGVVVVVVAAAEE   	0.4718
peptide2 	2 	16 	GGGGVVVVVVAAAEEE  	0.453562
peptide2 	3 	9 	GGGVVVVVV         	0.356778
peptide2 	3 	10 	GGGVVVVVVA        	0.4877
peptide2 	3 	11 	GGGVVVVVVAA       	0.508818
peptide2 	3 	12 	GGGVVVVVVAAA      	0.52975
peptide2 	3 	13 	GGGVVVVVVAAAE     	0.507462
peptide2 	3 	14 	GGGVVVVVVAAAEE    	0.489786
peptide2 	3 	15 	GGGVVVVVVAAAEEE   	0.4718
peptide2 	3 	16 	GGGVVVVVVAAAEEEE  	0.453562
peptide2 	4 	9 	GGVVVVVVA         	0.336333
peptide2 	4 	10 	GGVVVVVVAA        	0.4877
peptide2 	4 	11 	GGVVVVVVAAA       	0.508818
peptide2 	4 	12 	GGVVVVVVAAAE      	0.50475
peptide2 	4 	13 	GGVVVVVVAAAEE     	0.507462
peptide2 	4 	14 	GGVVVVVVAAAEEE    	0.489786
peptide2 	4 	15 	GGVVVVVVAAAEEEE   	0.4718
peptide2 	4 	16 	GGVVVVVVAAAEEEEE  	0.453562
peptide2 	5 	9 	GVVVVVVAA         	0.321889
peptide2 	5 	10 	GVVVVVVAAA        	0.4877
peptide2 	5 	11 	GVVVVVVAAAE       	0.481545
peptide2 	5 	12 	GVVVVVVAAAEE      	0.50475
peptide2 	5 	13 	GVVVVVVAAAEEE     	0.507462
peptide2 	5 	14 	GVVVVVVAAAEEEE    	0.489786
peptide2 	5 	15 	GVVVVVVAAAEEEEE   	0.4718
peptide2 	5 	16 	GVVVVVVAAAEEEEEE  	0.453562
peptide2 	6 	9 	VVVVVVAAA         	0.328222
peptide2 	6 	10 	VVVVVVAAAE        	0.4634
peptide2 	6 	11 	VVVVVVAAAEE       	0.486727
peptide2 	6 	12 	VVVVVVAAAEEE      	0.5095
peptide2 	6 	13 	VVVVVVAAAEEEE     	0.511846
peptide2 	6 	14 	VVVVVVAAAEEEEE    	0.493857
peptide2 	6 	15 	VVVVVVAAAEEEEEE   	0.4756
peptide2 	6 	16 	VVVVVVAAAEEEEEEE  	0.457125
peptide2 	7 	9 	VVVVVAAAE         	0.294889
peptide2 	7 	10 	VVVVVAAAEE        	0.4634
peptide2 	7 	11 	VVVVVAAAEEE       	0.486727
peptide2 	7 	12 	VVVVVAAAEEEE      	0.5095
peptide2 	7 	13 	VVVVVAAAEEEEE     	0.511846
peptide2 	7 	14 	VVVVVAAAEEEEEE    	0.493857
peptide2 	7 	15 	VVVVVAAAEEEEEEE   	0.4756
peptide2 	8 	9 	VVVVAAAEE         	0.380444
peptide2 	8 	10 	VVVVAAAEEE        	0.4634
peptide2 	8 	11 	VVVVAAAEEEE       	0.486727
peptide2 	8 	12 	VVVVAAAEEEEE      	0.5095
peptide2 	8 	13 	VVVVAAAEEEEEE     	0.511846
peptide2 	8 	14 	VVVVAAAEEEEEEE    	0.493857
peptide2 	9 	9 	VVVAAAEEE         	0.406
peptide2 	9 	10 	VVVAAAEEEE        	0.4634
peptide2 	9 	11 	VVVAAAEEEEE       	0.486727
peptide2 	9 	12 	VVVAAAEEEEEE      	0.5095
peptide2 	9 	13 	VVVAAAEEEEEEE     	0.511846
peptide2 	10 	9 	VVAAAEEEE         	0.378222
peptide2 	10 	10 	VVAAAEEEEE        	0.4634
peptide2 	10 	11 	VVAAAEEEEEE       	0.486727
peptide2 	10 	12 	VVAAAEEEEEEE      	0.5095
peptide2 	11 	9 	VAAAEEEEE         	0.393778
peptide2 	11 	10 	VAAAEEEEEE        	0.4634
peptide2 	11 	11 	VAAAEEEEEEE       	0.486727
peptide2 	12 	9 	AAAEEEEEE         	0.464778
peptide2 	12 	10 	AAAEEEEEEE        	0.5273
peptide3 	1 	9 	GGGGGVVVV         	0.382333
peptide3 	1 	10 	GGGGGVVVVV        	0.4941
peptide3 	1 	11 	GGGGGVVVVVV       	0.514636
peptide3 	2 	9 	GGGGVVVVV         	0.336778
peptide3 	2 	10 	GGGGVVVVVV        	0.4941




--Contacts--
For more queries or questions, please contact
Anas Al-okaily, anas.al-okaily@uconn.edu


Last update: 12/2016
