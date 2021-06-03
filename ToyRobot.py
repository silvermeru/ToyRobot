class ToyRobot():
	#Move north one square. If at the edge of the table, do nothing
	def North(self):
		if self.Y < 4:
			self.Y += 1

	#Move east one square. If at the edge of the table, do nothing
	def East(self):
		if self.X < 4:
			self.X +=1

	#Move South one square. If at the edge of the table, do nothing
	def South(self):
		if self.Y > 0:
			self.Y -= 1

	#Move West one square. If at the edge of the table, do nothing
	def West(self):
		if self.X > 0:
			self.X -= 1

	def __init__(self):
		# X coordinate on the table. Initialized to 0 to prevent runtime errors 
		self.X = 0
		# Y coordinate on the table. Initialized to 0 to prevent runtime errors 
		self.Y = 0
		# Number coresponding to a direction. Initialized to 0 to prevent runtime errors 
		self.Direction = 0
		# Boolean value to tell if the robot is on the table or not. Initially not on the table. 
		#No functions should run if the robot has not been placed
		self.Placed = False

		#Dictionary to get the appropriate move function for a given direction number
		self.Mover = {
			0: self.North,
			1: self.East,
			2: self.South,
			3: self.West
		}

		#Dictionary to get the direction that coresponds to a number
		self.NumberToDirection = {
			0: "NORTH",
			1: "EAST",
			2: "SOUTH",
			3: "WEST"
		}

		#Dictionary to get the number that corresponds to a direction
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
		return ""

	# Move robot one in unit in the direction it is facing
	def Move(self):
		if self.Placed:
			func = self.Mover.get(self.Direction, "Argument not found")
			func()
		return ""

	# Move Direction Left
	def Left(self):
		if self.Placed:
			if self.Direction ==  0:
				self.Direction = 3
			else:
				self.Direction -= 1
		return ""

	# Move Direction Right
	def Right(self):
		if self.Placed:
			if self.Direction ==  3:
				self.Direction = 0
			else:
				self.Direction += 1
		return ""

	# Report the coordinates of the robot and the direction it is facing
	def Report(self):
		if self.Placed:
			return "Output: " + str(self.X) + "," + str(self.Y) + "," + self.NumberToDirection.get(self.Direction, "Argument not found")
		return	""
