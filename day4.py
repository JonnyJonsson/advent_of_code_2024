import csv
import numpy as np

input = []
XMAS = ["X", "M", "A", "S"]
# test = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
xmas_sum = 0

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
	matrix = np.append(matrix, [row_l], axis=0)


def calc_xmas(line=["X", "X", "M", "A", "S", "X", "M", "A", "S"]):
	occurence = 0
	indexes = []
	for i in range(len(line)):
		if line[i : i + len(XMAS)] == XMAS:
			indexes.append((i, i + len(XMAS)))
			occurence += 1

	return occurence


for i in range(0, 4):
	matrix = np.rot90(matrix, k=i)
	diags = [matrix[::1, :].diagonal(i) for i in range(-matrix.shape[0] + 1, matrix.shape[1])]

	for dia in diags:
		# print(dia.tolist())
		xmas_sum += calc_xmas(dia.tolist())
print(f"xmas_sum after diagonals: {xmas_sum}")

for line in matrix:
	xmas_sum += calc_xmas(line.tolist())
print(f"xmas_sum after left-right {xmas_sum}")

for line in np.fliplr(matrix):
	xmas_sum += calc_xmas(line.tolist())
print(f"xmas_sum after right-left {xmas_sum}")

for line in matrix.T:
	xmas_sum += calc_xmas(line.tolist())
print(f"xmas_sum after top-down {xmas_sum}")

for line in np.flipud(matrix).T:
	xmas_sum += calc_xmas(line.tolist())
print(f"xmas_sum after down-top {xmas_sum}")

print(f"xmas sum:  {xmas_sum}")
