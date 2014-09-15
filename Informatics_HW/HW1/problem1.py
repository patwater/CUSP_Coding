import sys
import datetime

with open(sys.argv[1]) as raw_file:
	data = []
	for line in raw_file:
		data.append(line.split(","))

#create a list of just the dates created
dates = []

for i in xrange(len(data)-1):
	dates.append(data[i+1][1])

print str(len(data) - 1)+" complaints between "+str(datetime.datetime.strptime(str(min(dates)), "%m/%d/%Y %I:%M:%S %p"))+" and "+str(datetime.datetime.strptime(str(max(dates)), "%m/%d/%Y %I:%M:%S %p"))