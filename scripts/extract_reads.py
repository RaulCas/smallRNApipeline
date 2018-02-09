#!/usr/bin/env python
# -*- coding: utf-8 -*-

######################################################################################################################################
#
#	1) Extracts the fasta entries absent in "remove_file" (one per line) from "fasta_file".
#
#######################################################################################################################################

import sys
from Bio import SeqIO

remove_file = "readfile.txt" # Input wanted file, one gene name per line
fasta_file = "reads.fasta"  # Input fasta file
result_file = "clean_reads.fasta" # Output fasta file

result=open(result_file, 'w')

remove = set()
with open(remove_file) as f:
    for line in f:
        line = line.strip()
        if line != "":
            remove.add(line)

names = []

for record in SeqIO.parse(open(fasta_file),'fasta'):
	readname=str(record.id).split(' ')[0]
	names.append(readname)

seqs=set(names)

x=0
for item in SeqIO.parse(open(fasta_file),'fasta'):
	if item.id not in remove:
		x+=1
		result.write('>'+str(item.id)+'\n'+str(item.seq)+'\n')
