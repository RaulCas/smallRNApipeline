module load bowtie
module load perl
module load STAR

STAR --runMode genomeGenerate --genomeDir /rhome/rcastanera/bigdata/small_RNA_WT_2015/PIPELINE_v2.0/PC15/ --genomeFastaFiles /rhome/rcastanera/bigdata/small_RNA_WT_2015/PIPELINE_v2.0/PC15/rRNA_tRNA_bank.fa

