import csv
import copy
import itertools

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
raports_delta = copy.deepcopy(raports)
for raport in raports_delta:
	# print(len(raport))
	for i, level in enumerate(raport):
		if i == len(raport) - 1:
			del raport[-1]
		else:
			raport[i] = raport[i + 1] - raport[i]
	# print(raport)

for raport in raports_delta:
	if all(i < 4 and i > -4 for i in raport):
		if all(i > 0 for i in raport):
			# print(raport)
			raports_safe += 1
		elif all(i < 0 for i in raport):
			raports_safe += 1

print(raports_safe)

qq = [1, -1, 3, 4]
qqq = [1, 2, 4, 5]

for q in itertools.combinations(qq, len(qq) - 1):
	print(q)

for raport in raports:
	for level in raport:
		pass


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
			if pos == len(raport) - 1 and all(i < 4 for i in raport):
				return True
			if neg == len(raport) - 1 and all(i > -4 for i in raport):
				return True
			# if any(i > 3 for i in raport) and neg > 0:
			# return False
			# elif any(i < -3 for i in raport) and pos > 0:
			# return False
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

	return found


damp = 0

for i, raport_delta in enumerate(raports_delta):
	print(f"raport_delta: {raport_delta}")
	if only_one(raport_delta):
		print(f"found only one: {raport_delta}")
		print(f"creating combos of {raports[i]}")
		raports_combos = [
			list(raport) for raport in itertools.combinations(raports[i], len(raports[i]) - 1)
		]
		# print(f"raport combo: {type(raports_combos[0])}")
		for raport_combo in raports_combos:
			for n, level in enumerate(raport_combo):
				if n == len(raport_combo) - 1:
					del raport_combo[-1]
				else:
					raport_combo[n] = raport_combo[n + 1] - raport_combo[n]

		for raport in raports_combos:
			print(f"check if combo is safe: {raport}")
			if all(level < 4 and level > -4 for level in raport):
				if all(level > 0 for level in raport):
					# print(f"found damp raport {raport}")
					damp += 1
					break
				elif all(level < 0 for level in raport):
					# print(f"found damp raport {raport}")
					damp += 1
					break


print(f"damp: {damp}")
print(f"total: {raports_safe + damp}")
