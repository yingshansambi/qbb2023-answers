#!/usr/bin/env python
#Week6 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# In your base environment:
# brew install plink


# Step 1.2: Plot genotype PCs
# data = pd.read_table('plink.eigenvec', header = None, delim_whitespace = True)
# pc1 = data.loc[: , 2]
# pc2 = data.loc[: , 3]

# fig, ax = plt.subplots()
# ax.scatter(pc1,pc2)
# ax.set_title( "PCA" )
# ax.set_xlabel("pc1")
# ax.set_ylabel("pc2")
# fig.savefig( "PCA1" )
# plt.show()

#Step 2.2: Plot AFS
# allelefreq_table = pd.read_table('plink.frq', delim_whitespace = True)
# print(allelefreq_table.loc[:,'MAF'])#loc is more straight-forward
# # print(allelefreq_table)
# allelefreq = allelefreq_table.loc[:,'MAF']
# fig, ax = plt.subplots()
# ax.hist(allelefreq, bins= 50,range = (0,1))
# ax.set_title( "Allele Frequencies" )
# ax.set_xlabel("Allele Frequencies")
# plt.show()
# fig.savefig( "Allele Frequencies" )

# Step 3.2: Visualing GWAS results
# table1 = pd.read_table('CB1908_IC50_gwas_results.assoc.linear', delim_whitespace = True)
# pvalue1 = table1.loc[:,'P']
# print(pvalue1)
# pvalue_log = -np.log10(pvalue1)
# fig, (ax1, ax2) = plt.subplots(1,2)
# ax1.scatter(range(len(pvalue1)), pvalue_log, c=["r" if v > 5 else "b" for v in pvalue_log])
# ax1.set_title( "Manhattan Plot of CB1908_IC50" )
# ax1.set_xlabel("SNP")
# ax1.set_ylabel("-log10(P-value)")


# table2 = pd.read_table('GS451_IC50_gwas_results.assoc.linear', delim_whitespace = True)
# pvalue2 = table2.loc[:,'P']
# print(pvalue2)
# pvalue_log2 = -np.log10(pvalue2)
# ax2.scatter(range(len(pvalue2)), pvalue_log2, c=["r" if v > 5 else "b" for v in pvalue_log2])
# ax2.set_title( "Manhattan Plot of GS451_IC50" )
# ax2.set_xlabel("SNP")
# ax2.set_ylabel("-log10(P-value)")
# fig.savefig( "Manhattan Plots" )
#plt.show()


#Step 3.3: Visualizing effect-size
# table1 = pd.read_table('CB1908_IC50_gwas_results.assoc.linear', delim_whitespace = True)
# # print(table1)
# min1 = table1["P"].min()
# print(table1.loc[table1["P"] == min1, :]) # rs10876043


# vcf = pd.read_table('gwas_data/genotypes.vcf', header = 27, delim_whitespace = True)
# idx = table1.index[table1['SNP'] == "rs10876043"][0]
# #print(vcf)
# miniSNP = vcf.loc[vcf["ID"] == "rs10876043", :]
# #print(vcf.loc[vcf["ID"] == "rs10876043", :])

# geno = miniSNP.iloc[0,9:]

# table1 = pd.read_table('gwas_data/CB1908_IC50.txt', delim_whitespace = True)

# homo_ref = []
# homo_alt = []
# heter =[]

# # print(geno)

# for i in table1.index:
# 	id = table1.loc[i,"IID"]
# 	pheno = table1.loc[i,"CB1908_IC50"]
# 	id1= str(id) + "_" + str(id)
# 	#print(id1, geno.loc[:, id1], pheno)
# 	if geno.loc[id1] == "0/0": 
# 		homo_ref.append(pheno)
# 	elif geno.loc[id1] == "1/1"  :
# 		homo_alt.append(pheno)
# 	elif geno.loc[id1] == "0/1" : 
# 		heter.append(pheno)

# heter[12] = 0.0
# heter[30] = 0.0

# fig,ax = plt.subplots()
# plt.boxplot([homo_ref, heter, homo_alt])
# ax.set_title( "Boxplot of Effect-Size of CB1908 across genotypes" )
# ax.set_xlabel("Genotype")
# ax.set_ylabel("Effect-Size")
# fig.savefig( "Boxplot of Effect-Size" )
# ax.set_xticklabels(["homozygote_ref","heterzygote","homozygote_alt"])
# plt.show()

# Step3.4 :What gene could it be?

table1 = pd.read_table('CB1908_IC50_gwas_results.assoc.linear', delim_whitespace = True)
min1 = table1["P"].min()
print(table1.loc[table1["P"] == min1, :])

table2 = pd.read_table('GS451_IC50_gwas_results.assoc.linear', delim_whitespace = True)
min2 = table2["P"].min()
print(table2.loc[table2["P"] == min2, :])

