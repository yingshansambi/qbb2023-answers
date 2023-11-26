#Step 1.1: Compute genotype PCs

Week 6 
Step 1.1: Compute genotype PCs
plink --vcf gwas_data/genotypes.vcf --pca 10

The output of top10 values from the eigneval: 
2.23286
1.91716
1.88858
1.83419
1.82363
1.81699
1.80463
1.80033
1.7953
1.78938

#Step 2.1: Compute allele frequencies
plink --vcf gwas_data/genotypes.vcf --freq 

#Step 3.1: Running the GWAS
 plink --vcf gwas_data/genotypes.vcf --linear --pheno gwas_data/CB1908_IC50.txt  --covar plink.eigenvec --allow-no-sex --out CB1908_IC50_gwas_results

plink --vcf gwas_data/genotypes.vcf --linear --pheno gwas_data/GS451_IC50.txt  --covar plink.eigenvec --allow-no-sex --out GS451_IC50_gwas_results

#Step 3.4: What gene could it be?
table1 = pd.read_table('CB1908_IC50_gwas_results.assoc.linear', delim_whitespace = True)
min1 = table1["P"].min()
print(table1.loc[table1["P"] == min1, :])

For CB1908: 
         CHR         SNP        BP A1 TEST  NMISS   BETA   STAT             P
2028444   12  rs10876043  49190411  G  ADD    161  2.002  7.422  8.199000e-12

The highly associated gene related to the rs10876043 SNP in human is Human Gene DIP2B, Disco-interacting protein 2 homolog B (DIP2 homolog B).According to the description from UCSC, the encoded protein contains a binding site for the transcriptional regulator DNA methyltransferase 1 associated protein 1 as well as AMP-binding sites. The presence of these sites suggests that the encoded protein may participate in DNA methylation. This could be one of the potential reasons why this gene might impact this trait. 


table2 = pd.read_table('GS451_IC50_gwas_results.assoc.linear', delim_whitespace = True)
min2 = table2["P"].min()
print(table2.loc[table2["P"] == min2, :])

For GS451:
         CHR        SNP        BP A1 TEST  NMISS   BETA   STAT             P
2650065   19  rs7257475  20372113  T  ADD     88 -2.626 -5.801  1.430000e-07

The highly associated gene related to the rs7257475 SNP in human is Human Gene ZNF826, which is moderately similar to Zinc finger protein 91. One of the potential reasons that this gene impact this trait could be as ZNF, which could be able to interact with various molecules, such as DNA, RNA and other proteins. The ZNFs are also known for involving in regualtion of several cellular processes, such as transcriptional regulation, DNA repair, and so on. 