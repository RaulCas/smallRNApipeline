#!/bin/bash -l

#SBATCH --nodes=1
#SBATCH --ntasks=8
#SBATCH --mem=8G 
#SBATCH --time=0-00:20:00
#SBATCH --job-name="Clean"

module load BBMap

cd $SLURM_SUBMIT_DIR

# remove unnecesary files
rm testfile.sam;
rm "*.zip";

# create histogram of read lenght 
readlength.sh clean_reads.fasta out=histogram_readlenght.txt bin=1 max=30




 
 



