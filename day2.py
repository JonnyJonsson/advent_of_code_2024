import csv

raports = []

with open("day2_input", "r") as f:
	reader = csv.reader(f, delimiter=" ")
	for row in reader:
		raports.append(row)

for i, raport in enumerate(raports):
	raports[i] = list(map(int, raports[i]))

# Safe
raports_safe = 0
descanding = 0
ascending = 0
unsorted_raports = raports

for raport in raports:
	# print(len(raport))
	for i, level in enumerate(raport):
		if i == len(raport) - 1:
			del raport[-1]
		else:
			raport[i] = raport[i + 1] - raport[i]
	# print(raport)

for raport in raports:
	if all(i < 4 and i > -4 for i in raport):
		if all(i > 0 for i in raport):
			# print(raport)
			raports_safe += 1
		elif all(i < 0 for i in raport):
			raports_safe += 1
		else:
			unsafe_raports.append(raport)
	else:
		unsafe_raports.append(raport)


print(raports_safe)


def only_one(raport):
	if not all(i > 0 for i in raport):
		if not all(i < 0 for i in raport):
			pos = 0
			neg = 0
			zero = 0
			for level in raport:
				if level > 0:
					pos += 1
				elif level < 0:
					neg += 1
				elif level == 0:
					zero += 1

			if pos > 1 and neg > 1:
				return False
			if pos > 0 and neg > 0 and zero > 0:
				return False
			if any(i > 3 for i in raport) and neg > 0:
				return False
			elif any(i < -3 for i in raport) and pos > 0:
				return False
			elif any(i > 3 for i in raport) and zero > 0:
				return False
			elif any(i < -3 for i in raport) and zero > 0:
				return False

	found = False
	for level in raport:
		if level > 3 or level < -3 or level == 0:
			if found:
				return False
			else:
				found = True

	return True


damp = 0

for raport in unsafe_raports:
	if only_one(raport):
		damp += 1
		print(raport)

print(f"damp: {damp}")
print(f"total: {raports_safe + damp}")
