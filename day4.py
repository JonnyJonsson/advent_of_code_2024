import csv
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view

input = []
XMAS = ["X", "M", "A", "S"]
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


def search_matrix(matrix):
	sum = 0
	for line in matrix:
		sum += calc_xmas(line.tolist())
	print(f"found {sum} XMAS in matrix")
	return sum


# Diagonals
for i in range(0, 4):
	matrix = np.rot90(matrix, k=i)
	diags = [matrix[::1, :].diagonal(i) for i in range(-matrix.shape[0] + 1, matrix.shape[1])]
	xmas_sum += search_matrix(diags)
print(f"XMAS diagonals: {xmas_sum}")


xmas_sum += search_matrix(matrix)
xmas_sum += search_matrix(np.fliplr(matrix))
xmas_sum += search_matrix(matrix.T)
xmas_sum += search_matrix(np.flipud(matrix).T)

print(f"xmas sum:  {xmas_sum}")

# Part 2
X_mas = 0
MAS = np.empty((0, 3))
MAS = np.append(MAS, [["M", ".", "S"]], axis=0)
MAS = np.append(MAS, [[".", "A", "."]], axis=0)
MAS = np.append(MAS, [["M", ".", "S"]], axis=0)

views = sliding_window_view(matrix, (3, 3))

for windows in views:
	for i in range(0, 4):
		mas = np.rot90(MAS, k=i)
		for w in windows:
			mas[0][1] = w[0][1]
			mas[1][0] = w[1][0]
			mas[1][2] = w[1][2]
			mas[2][1] = w[2][1]
			if (w == mas).all():
				X_mas += 1

print(f"X-mas sum: {X_mas}")
