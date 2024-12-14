import csv
from graphlib import TopologicalSorter

input = []
rules = []
print_queues = []
middle_page_num = 0
middle_reorder_num = 0

with open("day5_input", "r") as f:
	reader = csv.reader(f, delimiter=" ")
	for row in reader:
		input.append(row)

for row in input:
	if not row:
		break
	rules.append((int(row[0][:2]), int(row[0][3:5])))

found_start_queues = False
for row in input:
	if found_start_queues:
		print_queues.append([int(n) for n in row[0].split(",")])
	if not row:
		found_start_queues = True


def create_graph(print_queue):
	graph = {}

	for key, value in rules:
		if key in print_queue:
			if key in graph:
				graph[key].append(value)
			else:
				graph[key] = [value]

	return graph


for print_queue in print_queues:
	graph = create_graph(print_queue)

	ts = TopologicalSorter(graph)
	order = ts.static_order()
	nodes = list(order)

	reorder = [n for n in nodes if n in print_queue]
	reorder = list(reversed(reorder))

	if reorder == print_queue:
		middle_page_num += print_queue[len(print_queue) // 2]
	else:
		middle_reorder_num += reorder[len(reorder) // 2]

print(f"sum of middle page nums: {middle_page_num} ")
print(f"sum of midle reorderd page nums: {middle_reorder_num} ")
