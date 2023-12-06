Week 7 


Part 2: Exploring CpG methylation
I think overall these two file tracks align well to each other. However, under fine resolution, I can see some singals presented only in nanopore track instead of the bisulfite sequencing track. 

Q1: Are the majority of the CpG dinucleotides methylated or unmethylated?

The majority of the CpG dinucleotides are methylated. 


Part 3: Comparing nanopore vs. bisulfite sequencing methylation calling

Part 3a

The number of sites: 
shared sites: 129216; 
only in the bismark file: 4299975; percentage: 129216/4299975 * 100 = 3.01%
only in the nanopore file: 4220772 ; percentage: 129216/4220772 * 100 = 3.06%


Q2: How does using nanopore for methylation calling differ from bisulfite sequencing in terms of coverage? Which method appears better and why?

Based on the distribution of the coverage of CpG, the nanopore seq with majority of coverage centers with a more narrow peak at the 35%, while bisulfite sequencing with general normal distribution centers at 50%. Bisulfite sequencing appears better, because it provides more reads with higher coverage. 


Part 4: Using IGV to explore differential methylation

samtools index -M -b ONT_data/normal.ONT.chr2.bam 
samtools index -M -b ONT_data/tumor.ONT.chr2.bam

Part 4a:
Q5: What changes can you observe between the normal and tumor methylation landscape? What do you think the possible effects are of the changes you observed?

Majority of the reads from the tumor paitents are methylated compared to the normal patients sample, which might indicate dysregulattion of the methylation might lead to silencing of the genes related to tumor suppressors. 

Q6: What does it mean for a gene to be “imprinted”? 

A gene to be "imprinted" refers to one copy of a gene could be expressed, while the other copy is suppressed. 

Q7: What is happening when you select the option to phase the reads? What is required in order to phase the reads?

When I selected the option to phase the reads with the default number 2, I recevied a message "Not enough features to create 2 classes. Max # of classes = 0". When I zoomed in the reads, the reads then can be phased. 

Q8: Can any set of reads be phased? Explain your answer.
Yes, there are allele-specific methylation sites. For the normal group, cluster 1 and cluster2 have similar number of samples, while the cancer group, cluster 2 sizes are larger than cluster 1. This effect seem consistent across sites. There are some sets of reads cann't be phased and are listed as none. 

