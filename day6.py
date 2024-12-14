import csv

input = []
pos = (0, 0)
rot = 0

with open("day6_input", "r") as f:
	reader = csv.reader(f, delimiter=" ")
	for row in reader:
		input.append(row)

# speed * rot : 1 * 90


class Guard:
	def __init__(self):
		self.pos = [0, 0]
		self.rot = 0
		self.dist = []

	def move(self):
		# 1 * rot
		match self.rot:
			case 0:
				self.pos[0] = self.pos[0] + 1
			case 90:
				self.pos[1] += 1
			case 180:
				self.pos[0] -= 1
			case 270:
				self.pos[1] -= 1
			case 360:
				self.pos[0] += 1

		self.dist.append(self.pos)

	def rotate(self):
		self.rot = self.rot + 90
		if self.rot == 360:
			self.rot = 0

		return self.rot
	def get_distinct_pos(self):
		distinct_pos = set(self.dist)
		return len(distinct_pos)

class Map:
	def __init__(self, input):
		self.input = input
		self.obstacle = "#"
		self.size = 130

	def check_move(self, pos):
		pass
		# Move to main?

	def is_tile_obstacle(self, pos):
		if self.input[pos[0]][pos[1]] == self.obstacle:
			return True
		else:
			return False

	def is_tile_outOfBound(self, pos):
		if any(p < 0 for p in pos):
			return True
		elif pos[0] > self.size:
			# Not sure this is correct
			return True
		elif pos[1] > self.size:
			return True
		else:
			return False

	def get_start_player(self):



map = Map(input)
print(f"similarity_score = {len(map.input)}")
