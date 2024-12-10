import csv

list_l = []
list_r = []
distance = 0

with open("day1_input", "r") as f:
	reader = csv.reader(f, delimiter=" ")
	for row in reader:
		list_l.append(row[0])
		list_r.append(row[3])

list_l.sort()
list_l = list(map(int, list_l))
list_r.sort()
list_r = list(map(int, list_r))

for i, id in enumerate(list_l):
	distance += abs(list_l[i] - list_r[i])

print(f"distance = {distance}")

similarity_score = 0

for id in list_l:
	if id in list_r:
		count = sum(1 for i in list_r if i == id)
		similarity_score += count * id

print(f"similarity_score = {similarity_score}")
