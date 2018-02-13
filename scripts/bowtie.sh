#!/bin/bash -l

#SBATCH --nodes=1
#SBATCH --ntasks=12
#SBATCH --mem=12G 
#SBATCH --time=0-02:00:00
#SBATCH --output=bowtie.txt
#SBATCH --job-name="bowtie"

module load bowtie 

bowtie -f -v 1 -k 1 -p 12 /rhome/rcastanera/bigdata/small_RNA_WT_2015/PIPELINE_v3.0/databases/PleosPC15.fa ../clean_reads.fasta mapped_reads
