#!/usr/bin/env python 

#Exercise 1 
import numpy as np 
import matplotlib.pyplot as plt 

def WFModel(AF,Pop): #AF = allele frequency 
	AFlist = []
	i = 0
	while 0< AF < 1: 
		i = i + 1 
		num = np.random.binomial(2*Pop, AF)
		AF = num/(2*Pop)
		AFlist.append(AF)
	return [AFlist, i]

gen = WFModel(0.5,200)[1]
print(gen)


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

#Exercise 2 - Part 1 

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



# fig, ax = plt.subplots()
# for i in range(2000):
# 	trajectory = WFModel(0.5,200)
# 	x_positions = trajectory[1]
# 	y_positions = trajectory[0]
# 	ax.set_title( "The Wright-Fisher Model(Repeats = 100)" )
# 	ax.set_xlabel("Generations")
# 	ax.set_ylabel("Allele Frequency")
# 	ax.plot(x_positions,y_positions)
# plt.show()
# fig.savefig( "Exercise2-Histogram" )

#Exercise 2 - Part2 
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
# 	return [AFlist, i]

# # print(WFModel(0.5,200))

# hist_x = []
# for i in range(1500):
# 	trajectory = WFModel(0.5,200)
# 	hist_x.append(trajectory[1])
# print(hist_x)
# print(len(hist_x))
# fig, ax = plt.subplots()
# ax.hist(hist_x)
# plt.show()
# fig.savefig( "Exercise2-Histogram" )

#Execise 3 - Part 1 


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

# pop_size = [100, 500, 1000, 2000, 5000]
# genlist_1= []
# for pop in pop_size:
# 	for i in range(100): 
# 		trajectory = WFModel(0.5,pop) #with fixed allele frequency = 0.5 
# 		genlist_1.append(trajectory[1])
# # print(genlist_1)

# averagelist=[]
# for i in (0, 1, 2, 3, 4):
# 	startPos = i*100
# 	stopPos = i*100 + 99 
# 	averagelist.append(sum(genlist_1[startPos:stopPos])/100)
# print(averagelist)

# fig, ax = plt.subplots()
# ax.scatter(pop_size, averagelist)
# ax.set_xlabel("Population Size")
# ax.set_ylabel("Avaerge Time to Fixation(year)")
# ax.set_title( "Average Time to Fixation across Population Size" )
# fig.savefig( "Average_Time_vs_Population Size" )
# plt.show()

# Exerise 3 - Part 2 

# frequency = [0.01, 0.1, 0.25, 0.5, 0.75]
# genlist_2 = []
# for freq in frequency:
#  	for i in range(10):
#  		trajectory = WFModel(freq,1000) # with fixed population = 1000
#  		genlist_2.append(trajectory[1])
# #print(genlist_2)

# averagelist_2=[]
# for i in (0, 1, 2, 3, 4):
# 	startPos = i
# 	stopPos = i + 9 
# 	averagelist_2.append(sum(genlist_2[startPos:stopPos])/10)
# #print(averagelist_2)

# fig, ax = plt.subplots()
# ax.scatter(frequency, averagelist_2)
# ax.set_xlabel("Allele Frequency")
# ax.set_ylabel("Avaerge Time to Fixation(year)")
# ax.set_title( "Average Time to Fixation across Allele Frequencies" )
# fig.savefig( "Average_Time_vs_Allele_Frequencies" )
# plt.show()


#Basic Exerise 

#1. 
#For the first plot of Question 1, the allele frequency is dropping toward to zero with fluctations.
#We can see the this gene will eventually dispear in the population. 
#What might be contributing could be environmental changes that did not favor the allele. 
#Biologically, it could be the phenotype does not offer any selection advantges for this
#population to survive. 

#2 
#One of the assumptions such as "everyone reproduces once per generation"
#In reality, there might be still a portion of the population can't be able to reproduce due to 
#many reseasons, such as natural disasters, diseases. Therefore, the genetic information from allele might not be able to 
#be passed to the next generation. 

#3
#Another assumpiton like "no mutation", which could be violated by potential errors generated in every possess during 
#protein expression, from transcription to post-translation. Mutations will offer more genetic diversity to the allele. 




