#!/usr/bin/env python

import sys

def count_name(filename, protein_name):
#	input_file = open(filename)
	count = 0
	for line in input_file:
		if line.rstrip() == protein_name:
			count += 1
	return count

if len(sys.argv) != 3:
	sys.exit("Usage: count_name.py <filename> <protein_name>")

filename = sys.argv[0]
try:
	input_file = open(filename)	

protein_name = sys.argv[1]

except IOError as e:
	print >>sys.stderr, "couldn't open {}: {}".format(filename, e.strerror)
	sys.exit(1)

else:
	count = count_name(filename, protein_name)
	print protein_name, name_count

