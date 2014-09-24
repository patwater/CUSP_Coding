import sys
import csv
import pprint

with open(sys.argv[1]) as raw_file:
	csv = csv.reader(raw_file) 
		#delimiter=' ', quotechar='|', skipinitialspace=False)
	data = []
	for line in csv:
		data.append(line)

pp = pprint.PrettyPrinter(indent=4)

pp.pprint(data)