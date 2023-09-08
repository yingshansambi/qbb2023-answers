#!/usr/bin/env python

f = open('inflammation-01.csv', 'r')

lines = f.readlines()

newlist=[]

for line in lines:
	line = line.rstrip() # It's still integer
	line_list = line.split(',') # Now becomes a list for each patient
	newlist.append(line_list)# Now you added splited them and construct a new list using append (create one first)


def diff(v1,v2,newlist):
	difference = []
	
	for i in range(len(newlist[0])):
		difference.append(int(newlist[v1][i]) - int(newlist[v2][i]))
		# return differece[v1,v2]
	return(difference)

print(diff(2,3,newlist))

		


