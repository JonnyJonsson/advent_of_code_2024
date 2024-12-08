import csv
import numpy as np

input = []
XMAS = ["X", "M", "A", "S"]

with open("day4_input", "r") as f:
	reader = csv.reader(f, delimiter=" ")
	for row in reader:
		input.append(row)

matrix = np.empty((0, 140))
for row in input:
	row_l = []
	for c in row:
		for c2 in c:
			row_l.append(c2)
	# print(row_l)
	# print("next")
	matrix = np.append(matrix, [row_l], axis=0)
diags = [matrix[::-1, :].diagonal(i) for i in range(-139, 140)]
diags.extend(matrix.diagonal(i) for i in range(139, -140, -1))
# print([n.tolist() for n in diags])

xmas_sum = 0

for dia in diags:
	diagonal = dia.tolist()
	indexes = []
	for i in range(len(diagonal)):
		if diagonal[i : i + len(XMAS)] == XMAS:
			indexes.append((i, i + len(XMAS)))
			xmas_sum += 1
	for i in indexes:
		for x in range(i[0], i[1]):
			print(diagonal[x])

print(f"xmas sum:  {xmas_sum}")
