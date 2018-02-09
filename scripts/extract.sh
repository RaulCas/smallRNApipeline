#!/bin/bash -l

cd $SLURM_SUBMIT_DIR


python /rhome/rcastanera/bigdata/small_RNA_WT_2015/PIPELINE_v3.0/scripts/prepare_extract.py
python /rhome/rcastanera/bigdata/small_RNA_WT_2015/PIPELINE_v3.0/scripts/extract_reads.py



