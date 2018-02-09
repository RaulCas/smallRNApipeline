#!/usr/local/bin/python

#########################################################################
#
# PIPELINE FOR SMALL RNA ANALYSIS: 1) QC filtering + mapping
#
# requires setting the path of the "scripts_path" folder (line 13)
#
#########################################################################

import commands, os, sys

scripts_path='/rhome/rcastanera/bigdata/small_RNA_WT_2015/PIPELINE_v3.0/scripts'
infile=sys.argv[1]

# STEP1: submit the first job: FastQC

cmd1 = "sbatch -p short "+scripts_path+"/fastqc.sh "+infile
print "Submitting Job1 with command: %s" % cmd1
status, jobnum = commands.getstatusoutput(cmd1)
if (status == 0 ):
    print "Job1 is %s" % jobnum
else:
    print "Error submitting Job1"

newjobnum=str(jobnum).replace("Submitted batch job ", "")

# STEP2: submit the second job: BBduk to filter adapters, contaminants and size-select (17-30nt)

cmd2 = "sbatch --depend=afterany:%s %s/trim_adapters.sh %s" % (newjobnum, scripts_path, infile)
print "Submitting Job2 with command: %s" % cmd2
status,jobnum = commands.getstatusoutput(cmd2)
if (status == 0 ):
    print "Job2 is %s" % jobnum
else:
    print "Error submitting Job2"

newjobnum=str(jobnum).replace("Submitted batch job ", "")

# STEP3: Submit FastQC again to verify 

cmd3 = "sbatch -p short --depend=afterany:%s %s/fastqc.sh trimmed_reads.fq" % (newjobnum, scripts_path)
print "Submitting Job3 with command: %s" % cmd3
status,jobnum = commands.getstatusoutput(cmd3)
if (status == 0 ):
    print "Job3 is %s" % jobnum
else:
    print "Error submitting Job3"

newjobnum=str(jobnum).replace("Submitted batch job ", "")


# STEP4 and 5: remove rRNAs and tRNAs
cmd4 = "sbatch --depend=afterany:%s --mem=12g --ntasks=8 --time=0-03:00:00 %s/remove_ribosomal.sh trimmed_reads.fq " % (newjobnum,scripts_path) 

print "Submitting Job4 with command: %s" % cmd4
status, jobnum = commands.getstatusoutput(cmd4)
if (status == 0 ):
    print "Job4 is %s" % jobnum
else:
    print "Error submitting Job4"

newjobnum=str(jobnum).replace("Submitted batch job ", "")

cmd5 = "sbatch --depend=afterany:%s --mem=12g --ntasks=8 --time=0-03:00:00 %s/extract.sh %s" % (newjobnum, scripts_path, infile)

print "Submitting Job5 with command: %s" % cmd5
status,jobnum = commands.getstatusoutput(cmd5)
if (status == 0 ):
    print "Job5 is %s" % jobnum
else:
    print "Error submitting Job5"

newjobnum=str(jobnum).replace("Submitted batch job ", "")

# STEP 6: Clean files and plot stats

cmd6 = "sbatch -p short --depend=afterany:%s %s/clean_temp.sh" % (newjobnum, scripts_path)
print "Submitting Job6 with command: %s" % cmd6
status,jobnum = commands.getstatusoutput(cmd6)
if (status == 0 ):
    print "Job6 is %s" % jobnum
else:
    print "Error submitting Job6"

newjobnum=str(jobnum).replace("Submitted batch job ", "")

"""
# STEP 7: Map with Butter

cmd6 = "sbatch -p short --depend=afterany:%s %s/butter.sh" % (newjobnum, scripts_path)
print "Submitting Job7 with command: %s" % cmd6
status,jobnum = commands.getstatusoutput(cmd6)
if (status == 0 ):
    print "Job7 is %s" % jobnum
else:
    print "Error submitting Job7"

"""














