#!/usr/bin/env python 

from fasta import readFASTA 
import sys 
import pandas as pd
import numpy as np

sequences = sys.argv[1]
matrix = sys.argv[2]
gap_penalty = sys.argv[3]
# output = sys.argv[4]


score_matrix = pd.read_csv(matrix, skipinitialspace = True)

print(score_matrix)

match_score = float(score_matrix)
mismatch_score = float(score_matrix)

input_sequences = readFASTA(open(sequences))

seq1_id, sequence1 = input_sequences[0]
seq2_id, sequence2 = input_sequences[1]

F_matrix = np.zeros((len(sequence1)+1, len(sequence2)+1))
track_matrix = np.zeros((len(sequence1)+1, len(sequence2)+1))

for i in range(len(sequence1)+1):
	F_matrix[i,0] = i * gap_penalty
	track_matrix [i,0] = i * gap_penalty

for j in range(len(sequence2)+1):
	F_matrix[0,j] = j * gap_penalty
	track_matrix [j,0] = j * gap_penalty
	


# for i in range(1, len(sequence1)+1): # loop through rows
# 	for j in range(1, len(sequence2)+1): # loop through columns
# 		if sequence1[i-1] == sequence2[j-1]: # if sequence1 and sequence2 match at positions i and j, respectively...
# 			d = F_matrix[i-1, j-1] + match_score
# 		else: # if sequence1 and sequence2 don't match at those positions...
# 			d = F_matrix[i-1, j-1] + mismatch_score
# 		h = F_matrix[i,j-1] + gap_penalty
# 		v = F_matrix[i-1,j] + gap_penalty

# 		F_matrix[i,j] = max(d,h,v)

# print(F_matrix)
