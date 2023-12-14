#!/usr/bin/env python 


#week10 

import numpy as np
import pandas as pd
from pydeseq2 import preprocessing
from matplotlib import pyplot as plt

# read in data
counts_df = pd.read_csv("gtex_whole_blood_counts_formatted.txt", index_col = 0)

# read in metadata
metadata = pd.read_csv("gtex_metadata.txt", index_col = 0)

# normalize
counts_df_normed = preprocessing.deseq2_norm(counts_df)[0]

# log
counts_df_logged = np.log2(counts_df_normed + 1)

# merge with metadata
full_design_df = pd.concat([counts_df_logged, metadata], axis=1)


# Step 1.1: Distribution of expression across genes
# GC_array = counts_df_logged.loc["GTEX-113IC"]
# GC_counts_nonzero = counts_df_logged.loc["GTEX-113IC"][(counts_df_logged.loc["GTEX-113IC"] !=0.0)]
# fig,ax = plt.subplots()
# ax.hist(GC_counts_nonzero.values,bins = 50)
# ax.set_xlabel("The Number of Genes")
# ax.set_ylabel("Logged Normalized Counts")
# ax.set_title( "GTEX-113JC Expression Distribution across Genes" )
# fig.savefig( "GTEX-113JC Expression Distribution" )

#Step 1.2: Expression of a single gene between sexes ---------------what is the x axis 
# 1 refers to males and 2 refers to females in metadata
# mxd4_female = []
# mxd4_male = []
# mxd4_countlist = counts_df_logged.loc[:,"MXD4"]
# for a in range(len(metadata.loc[:,"SEX"])):
# 		if metadata.loc[:,"SEX"][a] == 2: 
# 			mxd4_female.append(counts_df_logged.loc[:,"MXD4"][a])
# 		else:
# 			mxd4_male.append(counts_df_logged.loc[:,"MXD4"][a])

# fig,ax = plt.subplots()
# ax.hist(mxd4_male, color = "blue",alpha = 0.5,label = "male")
# ax.hist(mxd4_female, color = "red",label = "female")
# ax.set_title( "MXD4 Expression between Sexes")
# ax.set_ylabel("Logged Normalized Counts")
# plt.legend()
# plt.show()
# fig.savefig( "Expression between sexes" )

#Step 1.3: Distribution of subject ages
age_grouped = metadata.groupby(by=['AGE'])['AGE'].count()
y_values = age_grouped.values
x_values = age_grouped.index.tolist()
# fig,ax = plt.subplots()
# ax.bar(x_values,y_values, color = "blue")
# ax.set_title( "Subject Distribution across ages")
# ax.set_ylabel("Number of Subjects")
# ax.set_xlabel("Age")
# plt.show()
# fig.savefig( "Subject Distribution across ages" )



#Step 1.4: Sex-stratified expression with age
lpxn_countlist = counts_df_logged.loc[:,"LPXN"]
print(lpxn_countlist)
print(x_values)
print(metadata)
female_list = []
male_list = []
for i in lpxn_countlist.index:
	for a in 
	if lpxn_countlist[i] == age_grouped[i]
# lpxn_grouped = lpxn_countlist.group(by = metadata.loc['AGE'])









