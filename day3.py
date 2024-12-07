import csv
import re

input = []

with open("day3_input", "r") as f:
	reader = csv.reader(f, delimiter=" ")
	for row in reader:
		input.append(row)
multiplication = 0


def get_sum_of_mul(s):
	result = re.findall(r"mul\(\d{1,3},\d{1,3}\)", s)
	sum = 0
	if result:
		for mul in result:
			# print(mul)
			x = re.search(r"\(\d{1,3}", mul)
			y = re.search(r",\d{1,3}", mul)
			sum += int(x.group()[1:]) * int(y.group()[1:])
			# print(f"sum: {sum}")
	return sum


for row in input:
	for s in row:
		multiplication += get_sum_of_mul(s)

print(multiplication)


def find_do_segments(s):
	result = re.findall(r"do\(\).*don't\(\)", s)
	if result:
		for seg in result:
			print(seg)
			print("\n")


for row in input:
	for s in row:
		find_do_segments(s)
