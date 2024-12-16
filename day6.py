import csv
import copy

input = []

with open("day6_input", "r") as f:
	reader = csv.reader(f, delimiter=" ")
	for row in reader:
		input.append(row)


class Guard:
	def __init__(self, pos):
		self.pos = pos
		self.rot = 0

	def move(self):
		match self.rot:
			case 0:
				self.pos[0] -= 1
			case 90:
				self.pos[1] += 1
			case 180:
				self.pos[0] += 1
			case 270:
				self.pos[1] -= 1
			case 360:
				self.pos[0] -= 1

		print(f"new player pos: {self.pos}")

	def get_next_tile(self):
		match self.rot:
			case 0:
				return [self.pos[0] - 1, self.pos[1]]
			case 90:
				return [self.pos[0], self.pos[1] + 1]
			case 180:
				return [self.pos[0] + 1, self.pos[1]]
			case 270:
				return [self.pos[0], self.pos[1] - 1]
			case 360:
				return [self.pos[0] - 1, self.pos[1]]

	def rotate(self):
		self.rot = self.rot + 90
		if self.rot == 360:
			self.rot = 0

		return self.rot

	def get_pos(self):
		return self.pos


class Map:
	def __init__(self, input):
		self.input = input
		self.obstacle = "#"
		self.size = 129
		self.dist = []

	def is_tile_obstacle(self, pos):
		if self.input[pos[0]][0][pos[1]] == self.obstacle:
			return True
		else:
			return False

	def is_tile_outOfBound(self, pos):
		if any(p < 0 for p in pos):
			return True
		elif pos[0] > self.size:
			return True
		elif pos[1] > self.size:
			return True
		else:
			return False

	def get_start_player(self):
		start_pos = []
		for i, row in enumerate(self.input):
			for s in row:
				if "^" in s:
					start_pos.append(i)
					start_pos.append(s.index("^"))
					print(f"found player start: row: {i} col: {s.index("^")}")

		self.add_distinct_pos(start_pos)
		return start_pos

	def get_distinct_pos(self):
		return set(self.dist)

	def add_distinct_pos(self, pos):
		self.dist.append(tuple(pos))

	def get_distinct_pos_len(self):
		distinct_pos = set(self.dist)
		return len(distinct_pos)

	def replace_entity(self, pos, entity):
		input[pos[0]][0] = input[pos[0]][0][: pos[1]] + entity + input[pos[0]][0][pos[1] + 1 :]

	def render_map(self):
		for pos in self.dist:
			self.replace_entity(pos, "X")
		with open("map.txt", "w") as f:
			for row in self.input:
				f.write(row[0])
				f.write("\n")


map = Map(input)
start_pos = map.get_start_player()
guard = Guard(start_pos)


def run(map, guard):
	next_tile = guard.get_next_tile()

	if map.is_tile_outOfBound(next_tile):
		print("out of bounds")
		return False
	elif map.is_tile_obstacle(next_tile):
		print(f"obstacle at {next_tile}")
		guard.rotate()
		return True
	else:
		guard.move()
		map.add_distinct_pos(next_tile)
		return True


calculate = True
while calculate:
	calculate = run(map, guard)


map.render_map()
print(f"distinct positions = {map.get_distinct_pos_len()}")

map_orginal = copy.deepcopy(map)
distinct_pos = map.get_distinct_pos()

while True:
	try:
		# print(type(map.get_distinct_pos()))

		guard = Guard(start_pos)
		map = map_orginal
		map.replace_entity(distinct_pos.pop(), "#")
		calculate = True
		while calculate:
			calculate = run(map, guard)
		# print("replaced 1 entitiy")
	except Exception as ex:
		print(ex)
		break

map.render_map()
