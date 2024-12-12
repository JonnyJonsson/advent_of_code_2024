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
print_queue = ["75", "97", "47", "61", "53"]
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
# print(nodes)
printed = []

for paper in print_queue:
	# All nodes that need to be before paper
	temp = [n for n in nodes if nodes.index(n) > nodes.index(paper)]
	# print(f"paper: {paper}")
	print(temp)
	# print(printed)
	for p in printed:
		if p in temp:
			temp.remove(p)
			# print(f"removed {p} from temp: {temp}")
	# See if print_queue is in the right order
	print("y")
	print(temp)
	print([nodes.index(n) for n in nodes if n in temp])
	if (
		nodes.index(paper) > all([nodes.index(n) for n in nodes if n in temp])
		or print_queue.index(paper) == len(print_queue) - 1
	):
		print(f"paper {paper} is in right order")
	else:
		print("wrong order")
		break

	printed.append(paper)
