#!/usr/bin/env python 

def mean (anylist): 
	total = sum(anylist)
	average = total/len(anylist)
	return average 

print(mean([3,4,5])) 
