#!/usr/bin/env python 

import sys

fname = sys.argv[1]

data = open(fname).readlines()

num_list = []
for num in data:
	num = num.rstrip()
	num_list.append(int(num))

def mean (num_list): 
	total = sum(num_list)
	average = total/len(num_list)
	return average
	
print (mean(num_list)) 