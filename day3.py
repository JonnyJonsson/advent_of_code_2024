import csv
import re
import copy

input = []
input2 = ""
muls = 0

s = "hellodo()asd £ asd /)( don't()) 1234 asd !# don't()"
r = re.findall(r"do\(\).+?don't\(\)", s)


with open("day3_input", "r") as f:
	input2 = f.read()
	f.seek(0)
	reader = csv.reader(f, delimiter=" ")
	for row in reader:
		input.append(row)
multiplication = 0


def get_sum_of_mul(s):
	result = re.findall(r"mul\(\d{1,3},\d{1,3}\)", s, flags=re.DOTALL)
	sum = 0
	if result:
		for mul in result:
			global muls
			muls += 1

			print(mul)
			x = re.search(r"\(\d{1,3}", mul, flags=re.DOTALL)
			y = re.search(r",\d{1,3}", mul, flags=re.DOTALL)
			sum += int(x.group()[1:]) * int(y.group()[1:])
			print(f"sum: {sum}")
	return sum


for row in input:
	for s in row:
		# multiplication += get_sum_of_mul(s)
		pass
print(multiplication)


def find_first_segment(s):
	result = re.search(r".+?don't\(\)", s, flags=re.DOTALL)
	print(f"first segment: {result.group()}")
	dos = get_sum_of_mul(result.group())
	print(f"dos === {dos}")
	return dos


def find_do_segments(s):
	dos = 0
	# print(f"seaching segments in: {s}")
	# result = re.findall(r"do\(\)(.*)don't\(\)", s)
	result = re.findall(r"do\(\).+?don't\(\)", s, flags=re.DOTALL)
	# print(f"result {result}")
	if result:
		for seg in result:
			print(seg)
			print("\n")
			dos += get_sum_of_mul(seg)
	return dos


def find_last_segment(s):
	# result = re.search(r"do\(\).*", s)
	result = s[s.rfind("do()") :]
	print(f"last segment: {result}")
	dos = get_sum_of_mul(result)
	return dos


print(input2)
dos = find_first_segment(copy.deepcopy(input2))
dos += find_do_segments(input2)
dos += find_last_segment(input2)
print(f"dos: {dos}")
print(muls)
