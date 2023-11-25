#!/usr/bin/env python 

#Week5
import matplotlib.pyplot as plt
import numpy as np

#Step 3.0 : Parse the VCF file

depth_list = []
for line in open('variants_final.vcf'):
    if line.startswith('#'):
        continue
    fields = line.rstrip('\n').split('\t')
    genotypes = fields[9:]
    for subgenotype in genotypes:
    	subgenotype = subgenotype.split(':')
    	depth = subgenotype[2]
    	if depth == ".":
    		depth = 0
    	depth = int(depth)
    	depth_list.append(depth)
print(depth_list)

fig, ([ax1,ax2],[ax3,ax4]) = plt.subplots(2,2)

#Step3.1 Read Depth Distribution
x = depth_list
ax1.hist(x, bins= 50,range = (0,25))
ax1.set_title( "Read Depth Distribution" )
ax1.set_xlabel("Number of Variants")
ax1.set_ylabel("Read Depth")



#Step3.2 Genotype quality distribution
quality_list = []
for line in open('variants_final.vcf'):
    if line.startswith('#'):
        continue
    fields = line.rstrip('\n').split('\t')
    genotypes = fields[9:]
    for subgenotype in genotypes:
    	subgenotype = subgenotype.split(':')
    	quality = subgenotype[1]
    	if quality == ".":
    		quality = 0
    	quality = float(quality)
    	quality_list.append(quality)
	
# print(quality_list)
a = quality_list
ax2.hist(a, bins= 100,range = (0,200),color = "red", alpha = 0.5)
ax2.set_title( "Genotype Quality Distribution" )
ax2.set_xlabel("Number of Variants")
ax2.set_ylabel("Genotype Quality")



#Step 3.3: Allele frequency spectrum
allelefreq_list = []
for line in open('variants_final.vcf'):
    if line.startswith('#'):
        continue
    fields = line.rstrip('\n').split('\t')
    block = fields[7]
    block = block.split(';')
    for subblock in block:
    	subblock = block[3]
    	subblock = subblock.split("=")
    	allelefreq = subblock[1]
    	allelefreq_list.append(allelefreq)

allelefreq_float = []
for allelefreq in allelefreq_list:
	count = allelefreq.count(",")
	if count!=0:
		print(block)
	if "," in allelefreq:
		continue
	allelefreq = float(allelefreq)
	allelefreq_float.append(allelefreq) #make a new list and change into float, then added into the new list 
# print(type(allelefreq))
b = allelefreq_float

ax3.hist(b, bins= 50,range = (0,1),color = "green")
ax3.set_title( "Allele Frequency Spectrum" )
ax3.set_xlabel("Number of Variants")
ax3.set_ylabel("Allele Frequency")



#Step3.4 Predicted effects
predictedeffect_list = []
for line in open('variants_final.vcf'):
    if line.startswith('#'):
        continue
    fields = line.rstrip('\n').split('\t')
    block = fields[7]
    block = block.split(';')
    for subblock1 in block:
    	subblock1 = block[41]
    	subblock1 = subblock1.split("|")
    	predictedeffect = subblock1[1]
    	predictedeffect_list.append(predictedeffect)
# print(predictedeffect_list)

for i in range(len(predictedeffect_list)):
	if predictedeffect_list[i] == "":
		predictedeffect_list[i] = "undefined"

predictedeffect_list1 = list(set(predictedeffect_list))


pedictionary = {}
for effect in predictedeffect_list1: 
		count = predictedeffect_list.count(effect)
		pedictionary[effect] = count
# print(pedictionary)

plt.bar(range(len(pedictionary)),list(pedictionary.values()),align = "center",color = "orange")
plt.xticks(range(len(pedictionary)),list(pedictionary.keys()),rotation = 90)
ax4.set_title( "Distribution of Predicted Effects", loc='left')
ax4.set_xlabel("Predicted Effects")
ax4.set_ylabel("Number of Variants")
plt.xticks(fontsize = 5)
plt.tight_layout()

plt.show()
fig.savefig( "Multi-plane plot for week5" )

