#!/usr/bin/env python 

from fasta import readFASTA 
import sys 
import pandas as pd
import numpy as np

sequences = sys.argv[1]
matrix = sys.argv[2]
gap_penalty = float(sys.argv[3])
output = sys.argv[4]


score_matrix = pd.read_csv(matrix, delim_whitespace=True)

#print(score_matrix.columns) #.columns refers to column names
#print(score_matrix.index) # .index refers to row names

input_sequences = readFASTA(open(sequences))

seq1_id, sequence1 = input_sequences[0]
seq2_id, sequence2 = input_sequences[1]

F_matrix = np.zeros((len(sequence1)+1, len(sequence2)+1))
track_matrix = np.zeros((len(sequence1)+1, len(sequence2)+1), dtype = str)


for i in range(len(sequence1)+1):
	F_matrix[i,0] = i * gap_penalty
	track_matrix [i,0] = "h"

for j in range(len(sequence2)+1):
	F_matrix[0,j] = j * gap_penalty
	track_matrix[0,j]= "v"

#numpy array deisgned working for one type of datetype, while pandas can works with mutltiple datetypes


	
for i in range(1, len(sequence1)+1): 
	for j in range(1, len(sequence2)+1): 
		#if sequence1[i-1] == sequence2[j-1]:
		d = F_matrix[i-1, j-1] + score_matrix.loc[sequence1[i-1],sequence2[j-1]] #pandas using loc, numpy using the []
		h = F_matrix[i,j-1] + gap_penalty
		v = F_matrix[i-1,j] + gap_penalty
		F_matrix[i,j] = max(d,h,v)

		if max(d, v, h) == d:
			track_matrix[i,j] ="d"

		elif max(d, v, h) == v: 
			track_matrix[i,j] ="v"

		elif max(d, v, h) == h: 
			track_matrix[i,j] ="h"

# print(F_matrix)
#print(track_matrix)

#Step1.4 
i = track_matrix.shape[0] - 1
j = track_matrix.shape[1] - 1

sequence1_aligned = ""
sequence2_aligned = ""
while i>0 and j>0:
	if track_matrix[i, j] =="d": 
		sequence1_aligned = sequence1_aligned + sequence1[i-1]
		sequence2_aligned = sequence2_aligned + sequence2[j-1]
		i = i - 1
		j = j - 1 	
	elif track_matrix[i, j] =="v": 
		sequence1_aligned = sequence1_aligned + sequence1[i-1]
		sequence2_aligned = sequence2_aligned + "-"
		i = i - 1
		j = j
	
	elif track_matrix[i,j] =="h":
		sequence1_aligned = sequence1_aligned + "-"
		sequence2_aligned = sequence2_aligned + sequence2[j-1]
		i = i
		j = j - 1

final_sequence1 = sequence1_aligned[::-1]
final_sequence2 = sequence2_aligned[::-1]

print(final_sequence1.count("-"))
print(final_sequence2.count("-"))

