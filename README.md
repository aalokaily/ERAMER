
ERAMER tool version 1.0
This tool calucalue the score of trimming a given peptide by ERAP1 enzyme

--Software version--
This is version 1.0.0.

--Prerequisite--
Python v2.7.6. 
xlrd package (https://pypi.python.org/pypi/xlrd)

--Installation--
The tool is built using python; there is no need for installation.
PWM.xlsx must be stored in the same directory of the python script

--Running HGA Tool--
Run the command: 
python HGA.py [fasta file]
Where fasta file contain the peptides/precursor sequences in fasta format 


-Output formats--
The output will be rows with the following column format:
Peptide ID: The ID(fasta header) of the peptide 	
Position of C-terminus: Assuming As the tool computes for each 16-mer the score 	 
Expected transported peptide
Specificity score


--Samples test--
Running the following command where test.fasta is sample fasta file that is provided in the github package 
python ERAMER.py test.fasta

will output the following:

Peptide number	Position of 16-mers	 Expected transported peptide	 Specificity score
-------------------------------------------------------------------------------------------
peptide1 	1 	 LLLLLLLLLLLAAAAA 	0.525438
peptide1 	1 	  LLLLLLLLLLAAAAA 	0.548467
peptide1 	1 	   LLLLLLLLLAAAAA 	0.571929
peptide1 	1 	    LLLLLLLLAAAAA 	0.595923
peptide1 	1 	     LLLLLLLAAAAA 	0.600583
peptide1 	1 	      LLLLLLAAAAA 	0.586091
peptide1 	1 	       LLLLLAAAAA 	0.5727
peptide1 	1 	        LLLLAAAAA 	0.520778
peptide1 	2 	 LLLLLLLLLLAAAAAA 	0.525438
peptide1 	2 	  LLLLLLLLLAAAAAA 	0.548467
peptide1 	2 	   LLLLLLLLAAAAAA 	0.571929
peptide1 	2 	    LLLLLLLAAAAAA 	0.595923
peptide1 	2 	     LLLLLLAAAAAA 	0.600583
peptide1 	2 	      LLLLLAAAAAA 	0.586091
peptide1 	2 	       LLLLAAAAAA 	0.5727
peptide1 	2 	        LLLAAAAAA 	0.520778
peptide1 	3 	 LLLLLLLLLAAAAAAC 	0.483125
peptide1 	3 	  LLLLLLLLAAAAAAC 	0.503333
peptide1 	3 	   LLLLLLLAAAAAAC 	0.523571
peptide1 	3 	    LLLLLLAAAAAAC 	0.543846
peptide1 	3 	     LLLLLAAAAAAC 	0.544167
peptide1 	3 	      LLLLAAAAAAC 	0.524545
peptide1 	3 	       LLLAAAAAAC 	0.505
peptide1 	3 	        LLAAAAAAC 	0.445556
peptide1 	4 	 LLLLLLLLAAAAAACC 	0.483125
peptide1 	4 	  LLLLLLLAAAAAACC 	0.503333
peptide1 	4 	   LLLLLLAAAAAACC 	0.523571
peptide1 	4 	    LLLLLAAAAAACC 	0.543846
peptide1 	4 	     LLLLAAAAAACC 	0.544167
peptide1 	4 	      LLLAAAAAACC 	0.524545
peptide1 	4 	       LLAAAAAACC 	0.505
peptide1 	4 	        LAAAAAACC 	0.485556
peptide2 	1 	 GGGGGVVVVVVAAAEE 	0.453562
peptide2 	1 	  GGGGVVVVVVAAAEE 	0.4718
peptide2 	1 	   GGGVVVVVVAAAEE 	0.489786
peptide2 	1 	    GGVVVVVVAAAEE 	0.507462
peptide2 	1 	     GVVVVVVAAAEE 	0.50475
peptide2 	1 	      VVVVVVAAAEE 	0.486727
peptide2 	1 	       VVVVVAAAEE 	0.4634
peptide2 	1 	        VVVVAAAEE 	0.380444
peptide2 	2 	 GGGGVVVVVVAAAEEE 	0.453562
peptide2 	2 	  GGGVVVVVVAAAEEE 	0.4718
peptide2 	2 	   GGVVVVVVAAAEEE 	0.489786
peptide2 	2 	    GVVVVVVAAAEEE 	0.507462
peptide2 	2 	     VVVVVVAAAEEE 	0.5095
peptide2 	2 	      VVVVVAAAEEE 	0.486727
peptide2 	2 	       VVVVAAAEEE 	0.4634
peptide2 	2 	        VVVAAAEEE 	0.406
peptide2 	3 	 GGGVVVVVVAAAEEEE 	0.453562
peptide2 	3 	  GGVVVVVVAAAEEEE 	0.4718
peptide2 	3 	   GVVVVVVAAAEEEE 	0.489786
peptide2 	3 	    VVVVVVAAAEEEE 	0.511846
peptide2 	3 	     VVVVVAAAEEEE 	0.5095
peptide2 	3 	      VVVVAAAEEEE 	0.486727
peptide2 	3 	       VVVAAAEEEE 	0.4634
peptide2 	3 	        VVAAAEEEE 	0.378222
peptide2 	4 	 GGVVVVVVAAAEEEEE 	0.453562
peptide2 	4 	  GVVVVVVAAAEEEEE 	0.4718
peptide2 	4 	   VVVVVVAAAEEEEE 	0.493857
peptide2 	4 	    VVVVVAAAEEEEE 	0.511846
peptide2 	4 	     VVVVAAAEEEEE 	0.5095
peptide2 	4 	      VVVAAAEEEEE 	0.486727
peptide2 	4 	       VVAAAEEEEE 	0.4634
peptide2 	4 	        VAAAEEEEE 	0.393778
peptide2 	5 	 GVVVVVVAAAEEEEEE 	0.453562
peptide2 	5 	  VVVVVVAAAEEEEEE 	0.4756
peptide2 	5 	   VVVVVAAAEEEEEE 	0.493857
peptide2 	5 	    VVVVAAAEEEEEE 	0.511846
peptide2 	5 	     VVVAAAEEEEEE 	0.5095
peptide2 	5 	      VVAAAEEEEEE 	0.486727
peptide2 	5 	       VAAAEEEEEE 	0.4634
peptide2 	5 	        AAAEEEEEE 	0.464778
peptide2 	6 	 VVVVVVAAAEEEEEEE 	0.457125
peptide2 	6 	  VVVVVAAAEEEEEEE 	0.4756
peptide2 	6 	   VVVVAAAEEEEEEE 	0.493857
peptide2 	6 	    VVVAAAEEEEEEE 	0.511846
peptide2 	6 	     VVAAAEEEEEEE 	0.5095
peptide2 	6 	      VAAAEEEEEEE 	0.486727
peptide2 	6 	       AAAEEEEEEE 	0.5273
peptide2 	6 	        AAEEEEEEE 	0.415
peptide3 	1 	 GGGGGVVVVVVAAAPP 	0.450937
peptide3 	1 	  GGGGVVVVVVAAAPP 	0.469
peptide3 	1 	   GGGVVVVVVAAAPP 	0.486786
peptide3 	1 	    GGVVVVVVAAAPP 	0.504231
peptide3 	1 	     GVVVVVVAAAPP 	0.50125
peptide3 	1 	      VVVVVVAAAPP 	0.482909
peptide3 	1 	       VVVVVAAAPP 	0.4592
peptide3 	1 	        VVVVAAAPP 	0.330778
peptide3 	2 	 GGGGVVVVVVAAAPPP 	0.450937
peptide3 	2 	  GGGVVVVVVAAAPPP 	0.469
peptide3 	2 	   GGVVVVVVAAAPPP 	0.486786
peptide3 	2 	    GVVVVVVAAAPPP 	0.504231
peptide3 	2 	     VVVVVVAAAPPP 	0.506
peptide3 	2 	      VVVVVAAAPPP 	0.482909
peptide3 	2 	       VVVVAAAPPP 	0.4592
peptide3 	2 	        VVVAAAPPP 	0.356333
peptide3 	3 	 GGGVVVVVVAAAPPPP 	0.450937
peptide3 	3 	  GGVVVVVVAAAPPPP 	0.469
peptide3 	3 	   GVVVVVVAAAPPPP 	0.486786
peptide3 	3 	    VVVVVVAAAPPPP 	0.508615
peptide3 	3 	     VVVVVAAAPPPP 	0.506
peptide3 	3 	      VVVVAAAPPPP 	0.482909
peptide3 	3 	       VVVAAAPPPP 	0.4592
peptide3 	3 	        VVAAAPPPP 	0.364111
peptide3 	4 	 GGVVVVVVAAAPPPPP 	0.450937
peptide3 	4 	  GVVVVVVAAAPPPPP 	0.469
peptide3 	4 	   VVVVVVAAAPPPPP 	0.490857
peptide3 	4 	    VVVVVAAAPPPPP 	0.508615
peptide3 	4 	     VVVVAAAPPPPP 	0.506
peptide3 	4 	      VVVAAAPPPPP 	0.482909
peptide3 	4 	       VVAAAPPPPP 	0.4592
peptide3 	4 	        VAAAPPPPP 	0.334111
peptide3 	5 	 GVVVVVVAAAPPPPPP 	0.450937
peptide3 	5 	  VVVVVVAAAPPPPPP 	0.4728
peptide3 	5 	   VVVVVAAAPPPPPP 	0.490857
peptide3 	5 	    VVVVAAAPPPPPP 	0.508615
peptide3 	5 	     VVVAAAPPPPPP 	0.506
peptide3 	5 	      VVAAAPPPPPP 	0.482909
peptide3 	5 	       VAAAPPPPPP 	0.4592
peptide3 	5 	        AAAPPPPPP 	0.359556
peptide3 	6 	 VVVVVVAAAPPPPPPP 	0.4545
peptide3 	6 	  VVVVVAAAPPPPPPP 	0.4728
peptide3 	6 	   VVVVAAAPPPPPPP 	0.490857
peptide3 	6 	    VVVAAAPPPPPPP 	0.508615
peptide3 	6 	     VVAAAPPPPPPP 	0.506
peptide3 	6 	      VAAAPPPPPPP 	0.482909
peptide3 	6 	       AAAPPPPPPP 	0.5231
peptide3 	6 	        AAPPPPPPP 	0.332889
peptide3 	7 	 VVVVVAAAPPPPPPPP 	0.4545
peptide3 	7 	  VVVVAAAPPPPPPPP 	0.4728
peptide3 	7 	   VVVAAAPPPPPPPP 	0.490857
peptide3 	7 	    VVAAAPPPPPPPP 	0.508615
peptide3 	7 	     VAAAPPPPPPPP 	0.506
peptide3 	7 	      AAAPPPPPPPP 	0.541
peptide3 	7 	       AAPPPPPPPP 	0.5231
peptide3 	7 	        APPPPPPPP 	0.332889


--Contacts--
For more quiries or questions, please contact
Anas Al-okaily, anas.al-okaily@uconn.edu


Last update: 12/2016
