#!/usr/bin/env python 

f = open('inflammation-01.csv', 'r')

lines = f.readlines()

newlist=[]

for line in lines:
	line = line.rstrip() # It's still integer
	line_list = line.split(',') # Now becomes a list for each patient
	newlist.append(line_list)# Now you added splited them and construct a new list using append (create one first)

 #need to be assigned first
def mean_in(patient, newlist):
	average_list=[]
	total = 0
	patient = 0
	patient in range(len(newlist))
	print(type(patient))
	for eachpatient in newlist: 
		for string in eachpatient:
			integer = int(string)
			total += integer
		average = total/len(eachpatient)
		average_list.append(average) # so far here you are looping within the patient level 
	return average_list[patient] #indasation matters, you need to go back to calculate for every patient

print(mean_in(1, newlist))