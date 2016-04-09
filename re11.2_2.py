# -*- coding: utf-8 -*-
# 习题11.2

import re

file_name = raw_input("Enter file: ")
fhand = open(file_name)
text = fhand.read()
sum = 0.0

# 匹配整数或小数
x = re.findall('([0-9]*[.]*[0-9]+)', text)

for num in x:
	sum = sum + float(num)
print sum/len(x)