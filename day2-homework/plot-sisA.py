#!/usr/bin/env python 

import numpy as np
import matplotlib.pyplot as plt

transcripts = np.loadtxt( "all_annotated.csv", delimiter=",", usecols=0, dtype="<U30", skiprows=1 )
print( "transcripts: ", transcripts[0:5] )

samples = np.loadtxt( "all_annotated.csv", delimiter=",", max_rows=1, dtype="<U30" )[2:]
print( "samples: ", samples[0:5] )

data = np.loadtxt( "all_annotated.csv", delimiter=",", dtype=np.float32, skiprows=1, usecols=range(2, len(samples) + 2) )
print( "data: ", data[0:5, 0:5] )

# Find row with transcript of interest
for i in range(len(transcripts)):
    if transcripts[i] == 'FBtr0073461':
        row = i

# Find columns with samples of interest in female
cols = []
for i in range(len(samples)):
    if "female" in samples[i]:
        cols.append(i)

cols_male = []
for i in range(len(samples)):
	if "female" not in samples[i]:
		cols_male.append(i)

#Subset data of interest
expression = data[row, cols]
expression_male = data[row,cols_male]

# Prepare data
x = ["10", "11", "12", "13", "14A", "14B", "14C", "14D"]
y = expression
y1 = expression_male


# Plot data
fig, ax = plt.subplots()
plt.xticks(rotation = 45)
ax.set_title( "Sxl (FBtr0073461)" )
ax.plot( x, y)
ax.plot( x, y1)
ax.set_xlabel("Developmental Stage")
ax.set_ylabel(" mRNA abundance(RPKM)")
ax.legend(['female','male'])
plt.tight_layout() #order matters, has to be after this 
fig.savefig( "FBtr0073461_maleplot.png" )
plt.show()
# #plt.close( fig )