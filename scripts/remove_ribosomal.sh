#!/bin/bash -l


#SBATCH --output=out.txt
#SBATCH --job-name="rRNA"

module load fastx_toolkit
module load bowtie 

cd $SLURM_SUBMIT_DIR

# convert fastq tp fasta
cat $1 | awk '{if(NR%4==1) {printf(">%s\n",substr($0,2));} else if(NR%4==2) print;}' > reads.fasta

# map vs Bowtie
bowtie -v 1 -k 1 -S /rhome/rcastanera/bigdata/small_RNA_WT_2015/PIPELINE_v3.0/databases/Bowtie/PC15_rRNA_tRNA $1 testfile.sam


# Prepare and remove reads mapping to rRNAs and tRNAs. 
#python /rhome/rcastanera/bigdata/small_RNA_WT_2015/PIPELINE_v3.0/scripts/prepare_extract.py
#python /rhome/rcastanera/bigdata/small_RNA_WT_2015/PIPELINE_v3.0/scripts/extract_reads.py
