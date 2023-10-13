#!/usr/bin/env python

import sys


import numpy
import scipy.stats as stats
from scipy.stats import poisson #need to import poisson first 
import matplotlib.pyplot as plt
from week4livecode import load_bedgraph, bin_array

def main():
    # Load file names and fragment width
    # Define what genomic region we want to analyze
    chrom = "chr2R"
    chromstart = 10000000
    chromend =  12000000
    chromlen = chromend - chromstart

    # Load the sample bedgraph data, reusing the function we already wrote

    sample1F = sys.argv[1]
    sample1R = sys.argv[2]
    ctrlF = sys.argv[3]
    ctrlR = sys.argv[4]
    output = sys.argv[5]
    fragment = sys.argv[6]
    fragment = int(fragment)

    forward = load_bedgraph(sample1F, chrom, chromstart, chromend) #bedfile  give you the location
    reverse = load_bedgraph(sample1R, chrom,chromstart, chromend) # wiggle file will be just p values # and shift one read length to a point when the correlation is very good 
    #

    # Combine tag densities, shifting by our previously found fragment width

    # Load the control bedgraph data, reusing the function we already wrote
    controlF = load_bedgraph(ctrlF, chrom, chromstart, chromend)
    controlR = load_bedgraph(ctrlR, chrom, chromstart, chromend)

    # Combine tag densities
    combined = numpy.zeros(chromlen,int)
    combined[:-fragment//2] += reverse[fragment//2:]
    combined [fragment//2:] += forward[:-fragment//2] 
    #print(combined)   
    # Adjust the control to have the same coverage as our sample

    combined_ctrl = controlF + controlR

    # Create a background mean using our previous binning function and a 1K window
    # Make sure to adjust to be the mean expected per base

    background_mean = bin_array(combined_ctrl, 1000)/1000
    #print(background_mean)

    # Find the mean tags/bp and make each background position the higher of the
    # the binned score and global background score

    store_list = numpy.maximum(numpy.mean(combined_ctrl),background_mean) #choose the maximum one between the twos
    #print(store_list)

#at every point, store either control value or store whatever is higher 

    # Score the sample using a binsize that is twice our fragment size
    # We can reuse the binning function we already wrote
    scores = bin_array(combined, 198*2)
    #print(scores)

    # Find the p-value for each position (you can pass a whole array of values
    # and and array of means). Use scipy.stats.poisson for the distribution.
    # Remeber that we're looking for the probability of seeing a value this large
    # or larger
    # Also, don't forget that your background is per base, while your sample is
    # per 2 * width bases. You'll need to adjust your background

    Pvalue = 1 - stats.poisson.cdf(scores, background_mean*2*198)
    # print(Pvalue)

    # Transform the p-values into -log10
    # You will also need to set a minimum pvalue so you doen't get a divide by
    # zero error. I suggest using 1e-250
    Pvalue_list = numpy.maximum(Pvalue, 1e-250)
    Pvalue_list_transformed = numpy.log10(Pvalue_list)


    # Write p-values to a wiggle file
    # The file should start with the line
    # "fixedStep chrom=CHROM start=CHROMSTART step=1 span=1" where CHROM and
    # CHROMSTART are filled in from your target genomic region. Then you have
    # one value per line (in this case, representing a value for each basepair).

    wiggle = write_wiggle(Pvalue_list, chrom, chromstart + 1, 'wigglefile_2.wig')

    bed = write_bed(scores, chrom, chromstart, chromend, 198, 'sample2_peaks.bed')

    # Note that wiggle files start coordinates at 1, not zero, so add 1 to your
    # chromstart. Also, the file should end in the suffix ".wig"

    # Write bed file with non-overlapping peaks defined by high-scoring regions 


def write_wiggle(pvalues, chrom, chromstart, fname):
    output = open(fname, 'w')
    print(f"fixedStep chrom={chrom} start={chromstart + 1} step=1 span=1",
          file=output)
    for i in pvalues:
        print(i, file=output)
    output.close()

def write_bed(scores, chrom, chromstart, chromend, width, fname):
    chromlen = chromend - chromstart
    output = open(fname, 'w')
    while numpy.amax(scores) >= 10:
        pos = numpy.argmax(scores)
        start = pos
        while start > 0 and scores[start - 1] >= 10:
            start -= 1
        end = pos
        while end < chromlen - 1 and scores[end + 1] >= 10:
            end += 1
        end = min(chromlen, end + width - 1)
        print(f"{chrom}\t{start + chromstart}\t{end + chromstart}", file=output)
        scores[start:end] = 0
    output.close()


if __name__ == "__main__":
    main()