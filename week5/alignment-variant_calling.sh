#!/bin/bash

#Step1.1
#bwa index sacCer3.fa 
#to create the index for reference genome 

#{sample}already includes the filetype
#Step1.2 
for sample in *.fastq
do
	echo "Aligning sample:" ${sample}
	bwa mem -t 4 -R "@RG\tID:${sample}\tSM:${sample}" \ 
	  sacCer3.fa \
	  ${sample} > ${sample}.sam
done

