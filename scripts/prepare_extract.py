#################################################################################
#  	Run this script prior "extact_reads_from_fasta.py" on sam files
#	prints a file with all the mapped reads in one colum
#	- usage: python samfile outfile
#
#################################################################################

import sys

samfile_file = "testfile.sam"  # Input file (sam)
out_file = "readfile.txt" #   outpu_file

sam=open(samfile_file, 'r')
result=open(out_file, 'w')

lista=[]

for line in sam.readlines():
	elto=line.split()
	if '@SQ' in str(elto[0]):
		pass
	else:
		try:
			if '*' in str(elto[2]):
				pass
			else:
				lista.append(elto[0])
		except:
			pass
		
reads=set(lista)

for elto in reads:
	result.write(elto+'\n')

