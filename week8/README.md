Week8

#input-files: /Users/cmdb/qbb2023-answers/week8/raw/PCHIC_Data

#output-files: /Users/cmdb/qbb2023-answers/week8/chicago

#-d --design-dir: /Users/cmdb/qbb2023-answers/week8/raw/Design

#--en-feat-list: /Users/cmdb/qbb2023-answers/week8/raw/Features

#-e --export-format: washU_text

#Step 1.1: Running the runChicago.R script 
Rscript runChicago.R /Users/cmdb/qbb2023-answers/week8/raw/PCHIC_Data/GM_rep1.chinput chicago -e washU_text -d /Users/cmdb/qbb2023-answers/week8/raw/Design/ --en-feat-list /Users/cmdb/qbb2023-answers/week8/raw/Features/featuresGM.txt


#Step 1.2: Feature enrichment
Do these enrichments make sense to you? Are any surprising? Explain your reasoning briefly for each feature.

I think overall these enrichments make sense to me. I would expect the number of the "target" fragement is proportional to the mean number of the random fragments that overlap that feature, because the mean number is first determined by the "significant interactions", which associates with how they define "target" fragments. The mean number of the random fragments are more like background noise to me when we look at the "target" fragments. Turns out it is not linear, if we compared H3k27ac with CTCF, which is also surprising to me. 



bothbait:
        0         1         2  3    4      5  6   7   ...        10                                               11  12     13        14        15               16  17
911  chr21  34854620  34868437  .  653  18.64  .   0  ...  34861406                                      AP000302.58   +  chr21  34861480  34868437          DNAJC28   +
234  chr20  24972345  25043735  .  614  17.53  .   0  ...  24985047                                            APMAP   +  chr20  25036380  25043735            ACSS1   +
359  chr20  35888367  36164466  .  589  16.82  .   0  ...  36164466                                BLCAP;NNAT;PPIAP3   +  chr20  35888367  35895684             GHRH   +
877  chr21  33755386  33987743  .  536  15.30  .   0  ...  33987743                             AP000275.65;C21orf59   +  chr21  33755386  33767163   C21orf119;URB1   +
721  chr21  26803999  26939577  .  520  14.85  .   0  ...  26805415                                        LINC00158   +  chr21  26926437  26939577         MIR155HG   +
377  chr20  37045992  37082176  .  514  14.66  .   0  ...  37082176  SNHG11;SNHG17;SNORA60;SNORA71C;SNORA71D;SNORA71   +  chr20  37045992  37055959  SNHG17;SNORA71B   +

onebait:
        0         1         2  3     4      5  6   7      8         9         10                        11 12     13        14        15 16 17
614  chr20  55957140  56074932  .  1000  28.52  .   0  chr20  55957140  55973022        RBM38;RP4-800J21.3  +  chr20  56067414  56074932  .  -
399  chr20  39640890  39662867  .   601  17.15  .   0  chr20  39656513  39662867                      TOP1  +  chr20  39640890  39647373  .  -
765  chr21  28223187  30117523  .   582  16.62  .   0  chr21  30112950  30117523                 RNU6-872P  +  chr21  28223187  28225329  .  -
726  chr21  26790966  26939577  .   575  16.41  .   0  chr21  26926437  26939577                  MIR155HG  +  chr21  26790966  26793953  .  -
286  chr20  32041602  32262823  .   573  16.36  .   0  chr20  32254019  32262823  ACTL10;NECAB3;RP1-63M2.5  +  chr20  32041602  32060758  .  -
727  chr21  26793954  26939577  .   570  16.26  .   0  chr21  26926437  26939577                  MIR155HG  +  chr21  26793954  26795680  .  -
(base) [bootcamp-65


Step2.3 
I think overall it makes sense to visualize the ineraction between the promoter and enhancer could be across a long distance of the genomes. 
