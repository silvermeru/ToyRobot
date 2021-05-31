class ToyRobot():
	def North(self):
		if self.X < 4:
			self.X += 1

	def East(self):
		if self.Y < 4:
			self.Y +=1

	def South(self):
		if self.X > 0:
			self.X = self.X - 1

	def West(self):
		if self.Y > 0:
			self.Y -= 1

	def __init__(self):
		self.X = 0
		self.Y = 0
		self.Direction = 0
		self.Placed = False

		self.Mover = {
			0: self.North,
			1: self.East,
			2: self.South,
			3: self.West
		}

		self.NumberToDirection = {
			0: "NORTH",
			1: "EAST",
			2: "SOUTH",
			3: "WEST"
		}

		self.DirectionToNumber = {
			"NORTH": 0,
			"EAST": 1,
			"SOUTH": 2,
			"WEST": 3 
		}

	# Place robot at given point and facing the given direction
	def Place(self, X, Y, Direction):
		if X >= 0 and X <= 4 and Y >= 0 and Y <= 5 :
			self.X = X
			self.Y = Y
			self.Direction = self.DirectionToNumber.get(Direction, "Argument not found")
			self.Placed = True

	# Move robot one in unit in the direction it is facing
	def Move(self):
		if self.Placed:
			func = self.Mover.get(self.Direction, "Argument not found")
			func()

	# Move Direction Left
	def Left(self):
		if self.Placed:
			if self.Direction ==  0:
				self.Direction = 3
			else:
				self.Direction -= 1

	# Move Direction Right
	def Right(self):
		if self.Placed:
			if self.Direction ==  3:
				self.Direction = 0
			else:
				self.Direction += 1

	def Report(self):
		if self.Placed:
			print("Output: " + str(self.X) + "," + str(self.Y) + "," + self.NumberToDirection.get(self.Direction, "Argument not found"))
