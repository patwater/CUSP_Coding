import sys
import datetime
import collections

with open(sys.argv[1]) as raw_file:
	data = []
	for line in raw_file:
		data.append(line.split(","))

depts_zips = []
depts = []

for i in xrange(len(data)-1):
	depts_zips.append((data[i+1][3],data[i+1][7]))
	depts.append(data[i+1][3])

depts = sorted(set(depts))


def insertIntoDataStruct(aTuple,aDict):
    if not aTuple[0] in aDict:
        aDict[aTuple[0]] = [aTuple[1]]
    else:
        aDict[aTuple[0]].append(aTuple[1])

def neighborhood(iterable):
    iterator = iter(iterable)
    prev = None
    item = iterator.next()  # throws StopIteration if empty.
    for next in iterator:
        yield (prev,item,next)
        prev = item
        item = next
    yield (prev,item,None)

# go across the depts and count the zip codes

dept_dict = collections.defaultdict(list)

for i in depts:
	for j in depts_zips:
		if i == j[0]:
			insertIntoDataStruct(j,dept_dict)

count = []
for i in depts:
	count.append((i, sorted(collections.Counter(dept_dict[i]).items(), key = lambda t: t[1], reverse = True)))

answer_dict = {}
for i in count:
	for prev,item,next in neighborhood(i[1]):
		if prev == None:
			insertIntoDataStruct((i[0],(item[0], item[1])),answer_dict)
			
		else:
			if item[1] == prev[1]:
				insertIntoDataStruct((i[0],(item[0], item[1])),answer_dict)
			else:
				break

for i in answer_dict:
	answer_dict[i] = sorted(answer_dict[i], key = lambda t: t[0])

for i in answer_dict:
	print " "
	print i
	for j in answer_dict[i]:
		print j[0], j[1]

"""
for i in count:
	print " "
	print i[0]
	for prev,item,next in neighborhood(i[1]):
		if prev == None:
			print item[0], item[1]
			
		else:
			if item[1] == prev[1]:
				print item[0], item[1]
			else:
				break
				
"""