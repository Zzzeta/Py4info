# -*- coding: utf-8 -*-
# 习题11.2

import re

file_name = raw_input("Enter file: ")
file = open(file_name)
sum = 0.0
count = 0.0

for line in file:
	line = line.rstrip()
	x = re.findall('([0-9]+)', line)
#	if len(x) > 0:
#		print x
	for num in x:
		sum = sum + int(num)
	count = count + 1
	
print "sum: ", sum
print "count: ", count