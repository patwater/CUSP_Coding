import sys
import collections
from operator import itemgetter

with open(sys.argv[1]) as raw_file:
	data = []
	for line in raw_file:
		data.append(line.split(","))

complaints = []

for i in xrange(len(data)-1):
	complaints.append(data[i+1][5])

counter = collections.Counter(complaints)

key = set(complaints)

counter_tuple = []

for i in key:
	counter_tuple.append((i,counter[i]))

counter_tuple.sort(key = lambda t: t[0])
counter_tuple.sort(key = lambda t: t[1], reverse = True)

for i in xrange(int(sys.argv[2])):
	print counter_tuple[i][0], " with ", counter_tuple[i][1], " complaints"