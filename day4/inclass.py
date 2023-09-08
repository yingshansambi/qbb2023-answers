#!/usr/bin/env python 

#Question 1 
# import numpy as np 
# import matplotlib.pyplot as plt 

# def WFModel(AF,Pop): #AF = allele frequency 
# 	AFlist = []
# 	i = 0
# 	while 0< AF < 1: 
# 		i = i + 1 
# 		num = np.random.binomial(2*Pop, AF)
# 		AF = num/(2*Pop)
# 		AFlist.append(AF)
# 	return [AFlist, i]

# print(WFModel(0.5,200))


# import numpy as np 
# import matplotlib.pyplot as plt 

# def WFModel(AF,Pop): #AF = allele frequency 
# 	AFlist = []
# 	i = 0
# 	gen = []
# 	while 0< AF < 1: 
# 		i = i + 1 
# 		num = np.random.binomial(2*Pop, AF)
# 		AF = num/(2*Pop)
# 		AFlist.append(AF)
# 		gen.append(i)
# 	return [AFlist, gen]

# trajectory = WFModel(0.5,200)
# fig, ax = plt.subplots()
# x_positions = trajectory[1]
# y_positions = trajectory[0]
# ax.set_title( "The Wright-Fisher Model" )
# ax.set_xlabel("Generations")
# ax.set_ylabel("Allele Frequency")
# ax.plot(x_positions, y_positions)
# fig.savefig( "WF.png" )
# plt.show()

#Question 2 

import numpy as np 
import matplotlib.pyplot as plt 

def WFModel(AF,Pop): #AF = allele frequency 
	AFlist = []
	i = 0
	gen = []
	while 0< AF < 1: 
		i = i + 1 
		num = np.random.binomial(2*Pop, AF)
		AF = num/(2*Pop)
		AFlist.append(AF)
		gen.append(i)
	return [AFlist, gen]



fig, ax = plt.subplots()
for i in range(100):
	trajectory = WFModel(0.5,200)
	x_positions = trajectory[1]
	y_positions = trajectory[0]
	ax.set_title( "The Wright-Fisher Model(Repeats = 100)" )
	ax.set_xlabel("Generations")
	ax.set_ylabel("Allele Frequency")
	ax.plot(x_positions,y_positions)
fig.savefig( "WF-Part2-Plot1.png" )
plt.show()