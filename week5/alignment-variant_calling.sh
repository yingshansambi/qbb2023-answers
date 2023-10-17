#!/bin/bash

#Step1.1
#bwa index sacCer3.fa 
#to create the index for reference genome 

#{sample}already includes the filetype
#Step1.2 
# for sample in *.fastq
# do
# 	echo "Aligning sample:" ${sample}
# 	bwa mem -t 4 -R "@RG\tID:${sample}\tSM:${sample}" \ 
# 	  sacCer3.fa \
# 	  ${sample} > ${sample}.sam
# done

# Step1.3
# for sample in A01_09 A01_11 A01_23 A01_24 A01_27 A01_31 A01_35 A01_39 A01_62 A01_63
# # for sort in *.sam
# do
# 	inFile=${sample}.fastq.sam
# 	outFile=${sample}.sorted.bam
# 	samtools sort -o ${outFile} -O BAM ${inFile} #${}label the variable.
# done

for sample_index in A01_09 A01_11 A01_23 A01_24 A01_27 A01_31 A01_35 A01_39 A01_62 A01_63
do 
	inPut=${sample_index}.sorted.bam
	outPut=${sample_index}.sorted.bam.bai
	samtools index -M -b ${inPut} 
done