import csv
from graphlib import TopologicalSorter

tree = []
# 74,57,28,17,96
# 74|11
# 74|57

with open("day5_input", "r") as f:
	reader = csv.reader(f, delimiter=" ")
	for row in reader:
		tree.append(row)
print_queue = ["75", "47", "61", "53", "29"]
print(f"print_queue: {print_queue}")
graph = {
	"47": {"53", "13", "61", "29"},
	"97": {"13", "61", "47", "29", "53", "75"},
	"75": {"29", "53", "47", "61", "13"},
	"61": {"13", "53", "29"},
	"29": {"13"},
	"53": {"29", "13"},
}
ts = TopologicalSorter(graph)
order = ts.static_order()
nodes = list(order)
printed = []
print(f"nodes order: {nodes}")
middle_page_num = 0

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
