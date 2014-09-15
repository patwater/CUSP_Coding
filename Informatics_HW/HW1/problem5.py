import sys
import datetime
import collections 

with open(sys.argv[1]) as raw_file:
	data = []
	for line in raw_file:
		data.append(line.split(","))

#create a list of just the dates created
dates = []

for i in xrange(len(data)-1):
	dates.append(datetime.datetime.strptime(data[i+1][1], "%m/%d/%Y %I:%M:%S %p"))

raw_weekdays = []
for i in xrange(len(dates)):
	raw_weekdays.append(dates[i].weekday())

day_key = {0:"Monday", 1:"Tuesday", 2:"Wednesday", 3:"Thursday", 4:"Friday", 5:"Saturday", 6:"Sunday"}

count = collections.Counter(raw_weekdays)

for i in xrange(7):
	print str(day_key[i])+" == "+str(count[i])