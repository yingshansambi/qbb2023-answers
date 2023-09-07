#!/usr/bin/env python 

#chmod +x hw1.py

#./hw1.py 

# f = open('inflammation-01.csv', 'r')

# lines = f.readlines()

# newlist=[]

# for line in lines:
# 	line = line.rstrip() # It's still integer
# 	line_list = line.split(',') # Now becomes a list for each patient
# 	newlist.append(line_list) # Now you added splited them and construct a new list using append (create one first)

# patient5 = newlist[4] 

# print(patient5)

# print(patient5[4])

# print(patient5[9])

# print(patient5[-1])

##result: (base) [~/Desktop/swc-python/data $]./hw1.py 
#['0', '1', '1', '3', '3', '1', '3', '5', '2', '4', '4', '7', '6', '5', '3', '10', '8', '10', '6', '17', '9', '14', '9', '7', '13', '9', '12', '6', '7', '7', '9', '6', '3', '2', '2', '4', '2', '0', '1', '1']
#3
#4
#1



# f = open('inflammation-01.csv', 'r')
# lines = f.readlines()

# newlist = []

# for line in lines:
#  	line = line.rstrip() # It's still integer
#  	line_list = line.split(',') # Now becomes a list for each patient
#  	newlist.append(line_list) # Now you added splited them and construct a new list using append (create one first)

# #print(newlist)

# average_list = []

# for eachpatient in newlist: 

# 	sum = 0

# 	for string in eachpatient:
# 		integer = int(string)
# 		sum += integer

# 	average = sum/len(eachpatient)

# 	average_list.append(average)


# print(average_list[0:10])

#reuslt: [5.45, 5.425, 6.1, 5.9, 5.55, 6.225, 5.975, 6.65, 6.625, 6.525]




# f = open('inflammation-01.csv', 'r')
# lines = f.readlines()

# newlist = []

# for line in lines:
#  	line = line.rstrip() # It's still integer
#  	line_list = line.split(',') # Now becomes a list for each patient
#  	newlist.append(line_list) # Now you added splited them and construct a new list using append (create one first)

# #print(newlist)

# average_list = []

# for eachpatient in newlist: 

# 	sum = 0

# 	for string in eachpatient:
# 		integer = int(string)
# 		sum += integer

# 	average = sum/len(eachpatient)

# 	average_list.append(average)


# print(min(average_list))

# print(max(average_list))

#result: 5.225
#7.225



# f = open('inflammation-01.csv', 'r')

# lines = f.readlines()

# newlist=[]

# for line in lines:
# 	line = line.rstrip() # It's still integer
# 	line_list = line.split(',') # Now becomes a list for each patient
# 	newlist.append(line_list) # Now you added splited them and construct a new list using append (create one first)

# patient5 = newlist[4] 
# patient1 = newlist[0]

# patient5_int = [int(i) for i in patient5]
# patient1_int = [int(i) for i in patient1]

# print(patient5_int)
# print(patient1_int)

# difference = []

# for i in range(len(patient5)): 
# 		difference.append (patient1_int[i] - patient5_int[i])

# print(difference)

#[0, 1, 1, 3, 3, 1, 3, 5, 2, 4, 4, 7, 6, 5, 3, 10, 8, 10, 6, 17, 9, 14, 9, 7, 13, 9, 12, 6, 7, 7, 9, 6, 3, 2, 2, 4, 2, 0, 1, 1]
#[0, 0, 1, 3, 1, 2, 4, 7, 8, 3, 3, 3, 10, 5, 7, 4, 7, 7, 12, 18, 6, 13, 11, 11, 7, 7, 4, 6, 8, 8, 4, 4, 5, 7, 3, 4, 2, 3, 0, 0]
#[0, -1, 0, 0, -2, 1, 1, 2, 6, -1, -1, -4, 4, 0, 4, -6, -1, -3, 6, 1, -3, -1, 2, 4, -6, -2, -8, 0, 1, 1, -5, -2, 2, 5, 1, 0, 0, 3, -1, -1]












	