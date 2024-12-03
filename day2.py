import csv

raports = []

with open("day2_input", "r") as f:
	reader = csv.reader(f, delimiter=" ")
	for row in reader:
		raports.append(row)

for i, raport in enumerate(raports):
	raports[i] = list(map(int, raports[i]))
# asc desc abs(i - i+1) = 1,2,3

# Safe
raports_safe = 0
descanding = 0
ascending = 0

for raport in raports:
	if raport[0] > raport[1]:
		for i, level in enumerate(raport):
			if i == len(raport) - 1:
				if ascending == len(raport) - 1:
					raports_safe += 1
				ascending = 0
				break
			if raport[i] - raport[i + 1] in (1, 2, 3):
				ascending += 1
			else:
				damp = raport[i]
				# print(f"level: {raport[i]} level next: {raport[i+1]}")
	elif raport[0] < raport[1]:
		for i, level in enumerate(raport):
			if i == len(raport) - 1:
				if descanding == len(raport) - 1:
					raports_safe += 1
				descanding = 0
				break
			if raport[i] - raport[i + 1] in (-1, -2, -3):
				descanding += 1
				# print(f"level: {raport[i]} level next: {raport[i+1]}")

print(f"safe raports: {raports_safe}")

# Damp
dampener = 0
list_damp = []
descanding = 0
ascending = 0

for raport in raports:
	if raport[0] > raport[1]:
		for i, level in enumerate(raport):
			if i == len(raport) - 1:
				if ascending == len(raport) - 2:
					raports_safe += 1
				ascending = 0
				break
			if raport[i] - raport[i + 1] in (1, 2, 3):
				ascending += 1
			else:
				damp = raport[i]
				# print(f"level: {raport[i]} level next: {raport[i+1]}")
	elif raport[0] < raport[1]:
		for i, level in enumerate(raport):
			if i == len(raport) - 1:
				if descanding == len(raport) - 2:
					raports_safe += 1
				descanding = 0
				break
			if raport[i] - raport[i + 1] in (-1, -2, -3):
				descanding += 1
				# print(f"level: {raport[i]} level next: {raport[i+1]}")

print(f"safe raports plus damp raports: {raports_safe + dampener}")
