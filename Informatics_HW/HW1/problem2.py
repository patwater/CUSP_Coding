

import sys
import collections

with open(sys.argv[1]) as raw_file:
	data = []
	for line in raw_file:
		data.append(line.split(","))

complaints = []

for i in xrange(len(data)-1):
	complaints.append(data[i+1][5])

counter = collections.Counter(complaints)

key = set(complaints)

for i in key:
	print i, " with ", counter[i], " complaints"