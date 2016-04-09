# -*- coding: utf-8 -*-
# 习题11.1

import re

x = raw_input("Enter a regular expression: ")
file = open("mbox.txt")
num = 0

for line in file:
	line = line.rstrip()
	if re.search(x, line):
		num = num + 1
		
print "mbox.txt had %d lins that matched %s" % (num, x)