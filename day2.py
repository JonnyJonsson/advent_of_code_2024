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


# TODO: Merge get delta with report safe as theyare always ysed toghrter
def get_delta(r):
	r_copy = copy.deepcopy(r)
	for raport in r_copy:
		for i, level in enumerate(raport):
			if i == len(raport) - 1:
				del raport[-1]
			else:
				raport[i] = raport[i + 1] - raport[i]
	return r_copy


def is_report_safe(r):
	if all(i < 4 and i > -4 for i in r):
		if all(i > 0 for i in r):
			return True
		elif all(i < 0 for i in r):
			return True
	else:
		return False


raports_delta = get_delta(raports)

for raport in raports_delta:
	if is_report_safe(raport):
		raports_safe += 1

print(f"raports_safe: {raports_safe}")


# Damp raports
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
			elif pos > 0 and neg > 0 and zero > 0:
				return False
			elif pos == len(raport) - 1 and all(i < 4 for i in raport):
				return True
			elif neg == len(raport) - 1 and all(i > -4 for i in raport):
				return True
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
	if only_one(raport_delta):
		raports_combos = [
			list(raport) for raport in itertools.combinations(raports[i], len(raports[i]) - 1)
		]
		raports_combos_delta = get_delta(raports_combos)

		for raport in raports_combos_delta:
			if is_report_safe(raport):
				damp += 1
				break


print(f"damp: {damp}")
print(f"total: {raports_safe + damp}")
