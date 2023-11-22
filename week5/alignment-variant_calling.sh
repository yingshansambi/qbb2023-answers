#!/bin/bash

#Step1.1
# bwa index sacCer3.fa 
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

# # Step1.3
# for sample in A01_09 A01_11 A01_23 A01_24 A01_27 A01_31 A01_35 A01_39 A01_62 A01_63
# # for sort in *.sam
# do
# 	inFile=${sample}.fastq.sam
# 	outFile=${sample}.sorted.bam
# 	samtools sort -o ${outFile} -O BAM ${inFile} #${}label the variable.
# done

# for sample in A01_09 A01_11 A01_23 A01_24 A01_27 A01_31 A01_35 A01_39 A01_62 A01_63
# do 
# 	inPut=${sample}.sorted.bam
# 	outPut=${sample}.sorted.bam.bai
# 	samtools index -M -b ${inPut} 
# done

#Exercise2 
#Step2.1
#freebayes -f sacCer3.fa --genotype-qualities -p 1 A01_09.sorted.bam A01_11.sorted.bam A01_23.sorted.bam A01_24.sorted.bam A01_27.sorted.bam A01_31.sorted.bam A01_35.sorted.bam A01_39.sorted.bam A01_62.sorted.bam A01_63.sorted.bam > variants.vcf


#Step2.2

#vcffilter -f "QUAL > 20" variants.vcf > variants_filtered.vcf # 20 is greater than 99%


#Step2.3
# vcfallelicprimitives -k -g variants_filtered.vcf>variants_decomposed.vcf

#Step2.4
#snpEff ann -download  R64-1-1.105 variants_decomposed.vcf>variants_final.vcf
#head -n 100 variants_final.vcf > variants_submit.vcf


