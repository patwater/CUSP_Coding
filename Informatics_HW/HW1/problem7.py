import sys
import datetime
import collections
import csv 

with open(sys.argv[1]) as raw_file:
	csv = csv.reader(raw_file) 
		#delimiter=' ', quotechar='|', skipinitialspace=False)
	data = []
	for line in csv:
		data.append(line)

with open(sys.argv[2]) as raw_file2:
	zip_borough = []
	for line in raw_file2:
		zip_borough.append(line.split(","))



zipcodes = []

for i in xrange(len(data)-1):
	zipcodes.append(data[i+1][7])

borough_count = {}

def insertIntoDataStruct(aTuple,aDict):
    if not aTuple[0] in aDict:
        aDict[aTuple[0]] = [aTuple[1]]
    else:
        aDict[aTuple[0]].append(aTuple[1])

#put a "1" into a count for every matching zipcode
for i in zipcodes:
	z=-1
	for j in zip_borough:
		if i == j[0]:
			insertIntoDataStruct((j[1],1),borough_count)
		else: 
			z+=1

#change the order of boroughs so it prints correctly
order_they_want = ["BROOKLYN","QUEENS","BRONX","MANHATTAN","STATEN ISLAND"]
dict_order = ["STATEN ISLAND","BRONX","MANHATTAN","BROOKLYN","QUEENS"]

new_borough_count = {}
j=-1
for i in borough_count:
	j+=1
	new_borough_count[dict_order[j]] = borough_count[i]

for i in order_they_want:
	print str(i)+" with "+str(sum(new_borough_count[i]))+" complaints"