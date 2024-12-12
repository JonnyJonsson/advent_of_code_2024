import csv
from graphlib import TopologicalSorter

input = []
rules = []
print_queues = []
middle_page_num = 0

with open("day5_input", "r") as f:
	reader = csv.reader(f, delimiter=" ")
	for row in reader:
		input.append(row)

for row in input:
	if not row:
		break
	rules.append((int(row[0][:2]), int(row[0][3:5])))

found = False
for row in input:
	if found:
		print_queues.append([int(n) for n in row[0].split(",")])
	if not row:
		found = True

# print_queue = [74, 57, 28, 17, 96]
# print(f"print_queue: {print_queue}")
for print_queue in print_queues:
	graph = {}
	for key, value in rules:
		if key in print_queue:
			if key in graph:
				graph[key].append(value)
			else:
				graph[key] = [value]

	for key in graph:
		print(key)
		print(graph[key])

	"""
	graph = {
		47: [53, 13, 61, 29],
		97: [13, 61, 47, 29, 53, 75],
		75: [29, 53, 47, 61, 13],
		61: [13, 53, 29],
		29: [13],
		53: [29, 13],
	}
	"""
	ts = TopologicalSorter(graph)
	order = ts.static_order()
	nodes = list(order)
	printed = []
	print(f"nodes order: {nodes}")

	for paper in print_queue:
		# All nodes that need to be before paper
		temp = [n for n in nodes if nodes.index(n) > nodes.index(paper)]
		print(f"temp: {temp}")
		for p in printed:
			if p in temp:
				temp.remove(p)

		for p in nodes:
			if p not in print_queue:
				if p in temp:
					temp.remove(p)

		# See if print_queue is in the right order
		if print_queue.index(paper) == len(print_queue) - 1:
			print(f"paper {paper} is in right order")
			middle_page_num += print_queue[len(print_queue) // 2]
		elif all(nodes.index(paper) > nodes.index(n) for n in temp):
			print(f"paper: {paper} in rigt order")
		else:
			print(f"paper: {paper} in wrong order")
			break

		printed.append(paper)

print(f"sum of middle page nums: {middle_page_num} ")
