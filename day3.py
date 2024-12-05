import csv
import re

input = []

with open("day3_input", "r") as f:
	reader = csv.reader(f, delimiter=" ")
	for row in reader:
		input.append(row)
sum = 0
# mul(xxx,yyy)
for row in input:
	for s in row:
		result = re.findall(r"mul\(\d{1,3},\d{1,3}\)", s)
		if result is not None:
			for mul in result:
				# print(mul)
				x = re.search(r"\(\d{1,3}", mul)
				y = re.search(r",\d{1,3}", mul)
				sum = +int(x.group()[1:]) * int(y.group()[1:])
print(sum)
