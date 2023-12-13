#!/usr/bin/env python

#week8 

import sys
import pandas as pd

# baitmap = sys.argv[1] #/Users/cmdb/qbb2023-answers/week8/raw/Design/h19_chr20and21.baitmap
# washu = sys.argv[2] #/Users/cmdb/qbb2023-answers/week8/chicago/data/chicago_washU_text.txt

baitmap_data= pd.read_table('raw/Design/h19_chr20and21.baitmap', header = None, delim_whitespace = True)
# print(baitmap_data.loc[:1]) #the header
# print(baitmap_data.iloc[:,1])

washu = pd.read_table('chicago/data/chicago_washU_text.txt', header = None, delim_whitespace = True)
washusplit_1 = washu[0].str.split(",",expand = True)
washusplit_2 = washu[1].str.split(",",expand = True)
print(washu.loc[:1])
# print(washusplit_1.iloc[:1]) #the header 
# print(washusplit_2.iloc[:1]) #the header 
# print(washusplit_1.iloc[:,1])

gene_name1 = []
for baitloc in range(len(baitmap_data.iloc[:,1])):
	for start1 in range(len(washusplit_1.iloc[:,1])):
		start1 = int(start1)
		if baitloc == start1:
			gene_name1.append(baitmap_data.iloc[:,4][baitloc])
# print(len(gene_name1))

for baitloc in range(len(baitmap_data.iloc[:,1])):
	for start2 in range(len(washusplit_2.iloc[:,1])):
		start2 = int(start2)
		if baitloc == start2:
			gene_name1.append(baitmap_data.iloc[:,4][baitloc])
# print(len(gene_name1))
gene_namefinal = list(set(gene_name1))

# print(gene_namefinal)
# print(len(gene_namefinal)) #875 corresponding genes

interaction_score = []
for baitloc in range(len(baitmap_data.iloc[:,1])):
	for start1 in range(len(washusplit_1.iloc[:,1])):
		start1 = int(start1)
		if baitloc == start1:
			interaction_score.append(washu.iloc[:,2][baitloc])#index the df?

interaction_score = list(interaction_score)
print(len(interaction_score)) # 365 after removing the duplicates
score_max = max(interaction_score)
print(score_max)

for score in range(len(interaction_score)): 
	interaction_score[score] = int(score / score_max) * 1000

print(interaction_score)

# chrom = []
# for chrom_ele in chrom: 
# 	chrom[chrom_ele] = baitmap_dat[]

print(washu)

maxScore = max(washu.loc[:, 2])
print(maxScore)

file = open("UCSC.bed","w")
file.write('track type=interact name="pCHIC" description="Chromatin interactions" useScore=on maxHeightPixels=200:100:50 visibility=full' + "\n")
for i in washu.index:
	line = []
	line.append(washu.loc[i, 0].split(",")[0])
	line.append(str(min(int(washu.loc[i, 0].split(",")[1]), int(washu.loc[i, 1].split(",")[1]))))
	line.append(str(max(int(washu.loc[i, 0].split(",")[2]), int(washu.loc[i, 1].split(",")[2]))))
	line.append('.')
	line.append(str(int(washu.loc[i, 2] / maxScore * 1000)))
	line.append(str(washu.loc[i, 2]))
	line.append('.') #exp
	line.append('0')
	if int(washu.loc[i, 0].split(",")[1]) in baitmap_data.iloc[:,1].to_list(): # if first segment is bait 
		# Bait 
		line.append(washu.loc[i, 0].split(",")[0])#sourceChrom
		line.append(washu.loc[i, 0].split(",")[1])#sourceStart
		line.append(washu.loc[i, 0].split(",")[2])#sourceEnd
		line.append(str(baitmap_data.loc[baitmap_data[1] == int(washu.loc[i, 0].split(",")[1]), 4].values[0]))
		line.append('+')
		if int(washu.loc[i, 1].split(",")[1]) in baitmap_data.iloc[:,1].to_list():
		# if second segment is bait
			line.append(washu.loc[i, 1].split(",")[0])#targetChrom if both baits copied the second segment
			line.append(washu.loc[i, 1].split(",")[1])#targetStart 
			line.append(washu.loc[i, 1].split(",")[2])#targetEnd
			line.append(str(baitmap_data.loc[baitmap_data[1] == int(washu.loc[i, 1].split(",")[1]), 4].values[0]))
			line.append('+')
		else: # if second segment is target 
			line.append(washu.loc[i, 1].split(",")[0])#targetChrom if both baits copied the second segment
			line.append(washu.loc[i, 1].split(",")[1])#targetStart 
			line.append(washu.loc[i, 1].split(",")[2])#targetEnd
			line.append('.')
			line.append('-')

	else: # if first segment isnt bait 
		# Bait 
		line.append(washu.loc[i, 1].split(",")[0])
		line.append(washu.loc[i, 1].split(",")[1])
		line.append(washu.loc[i, 1].split(",")[2])
		line.append(str(baitmap_data.loc[baitmap_data[1] == int(washu.loc[i, 1].split(",")[1]), 4].values[0]))
		line.append('+')
		# append first segment as target 
		line.append(washu.loc[i, 0].split(",")[0])
		line.append(washu.loc[i, 0].split(",")[1])
		line.append(washu.loc[i, 0].split(",")[2])
		line.append('.')
		line.append('-')

	# print("\t".join(line))
	file.write("\t".join(line) + "\n")


#Step 2.2: Finding the most significant interactions
ucsc_bed = pd.read_table('UCSC.bed', delim_whitespace = True, skiprows = 1, header=None)
print(ucsc_bed)

#filter by the dataframe
bothbait_df = ucsc_bed.loc[[("+" in i) and ("+" in j) for i, j in zip(ucsc_bed.iloc[:, 12], ucsc_bed.iloc[:, 17])], :]
bothbait_df_sorted = bothbait_df.sort_values(4, ascending = False).head(6)
print(bothbait_df_sorted)


#filter out the source strand and targe strand are both bait fragments

onebait_df = ucsc_bed.loc[[("+" in i) and ("-" in j) for i, j in zip(ucsc_bed.iloc[:, 12], ucsc_bed.iloc[:, 17])], :]
onebait_df_sorted = onebait_df.sort_values(4, ascending = False).head(6)
# print(onebait_df_sorted)






