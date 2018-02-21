#!/bin/bash -l

#SBATCH --nodes=1
#SBATCH --ntasks=8
#SBATCH --mem=12G 
#SBATCH --time=0-03:00:00
#SBATCH --output=BBduk_out.txt
#SBATCH --job-name="BBduk"

module load BBMap


cd $SLURM_SUBMIT_DIR


bbduk.sh -Xmx1g in1=$1 out1=trimmed_reads.fq ref=/opt/linux/centos/7.x/x86_64/pkgs/BBMap/37.76/resources/truseq.fa.gz,/opt/linux/centos/7.x/x86_64/pkgs/BBMap/37.76/resources/truseq_rna.fa.gz,/opt/linux/centos/7.x/x86_64/pkgs/BBMap/37.76/resources/nextera.fa.gz,/opt/linux/centos/7.x/x86_64/pkgs/BBMap/37.76/resources/sequencing_artifacts.fa.gz,/opt/linux/centos/7.x/x86_64/pkgs/BBMap/37.76/resources/phix_adapters.fa.gz ktrim=r k=23 mink=11 hdist=1 minlength=17 maxlength=30 tpe tbo

