# smallRNApipeline

Pipeline for cleaning and mapping smallRNAseq reads: 

Dependencies:

  - Slurm Workload Manager
  - Python/Biopython
  - Fastqc
  - BBDuk
  - Bowtie
  - Butter
  - Samtools

  
USAGE: python smallRNApipeline.py raw_reads.fastq

Important: This pipeline is prepared to work in the UCR biocluster. The path to the scripts folder will need to be changed in the code in order to make it work in other systems.
