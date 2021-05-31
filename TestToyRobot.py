import unittest
import ToyRobot


class TestToyRobotMethods(unittest.TestCase):
	def test_beforeplace(self):
		tr = ToyRobot.ToyRobot()
		tr.Left()
		self.assertEqual(tr.X, 0)
		self.assertEqual(tr.Y, 0)
		self.assertEqual(tr.Direction, 0)
		tr.Right()
		self.assertEqual(tr.X, 0)
		self.assertEqual(tr.Y, 0)
		self.assertEqual(tr.Direction, 0)
		tr.Move()
		self.assertEqual(tr.X, 0)
		self.assertEqual(tr.Y, 0)
		self.assertEqual(tr.Direction, 0)

	def test_Place(self):
		tr = ToyRobot.ToyRobot()
		tr.Place(3,3,"SOUTH")
		self.assertEqual(tr.X, 3)
		self.assertEqual(tr.Y, 3)
		self.assertEqual(tr.Direction, 2)
		#Test placed off board 
		tr.Place(5,1,"NORTH")
		self.assertEqual(tr.X, 3)
		self.assertEqual(tr.Y, 3)
		self.assertEqual(tr.Direction, 2)

	def test_Move(self):
		tr = ToyRobot.ToyRobot()
		tr.Place(3,3,"SOUTH")
		tr.Move()
		self.assertEqual(tr.X, 2)
		self.assertEqual(tr.Y, 3)
		self.assertEqual(tr.Direction, 2)
		tr.Move()
		self.assertEqual(tr.X, 1)
		self.assertEqual(tr.Y, 3)
		self.assertEqual(tr.Direction, 2)
		tr.Move()
		self.assertEqual(tr.X, 0)
		self.assertEqual(tr.Y, 3)
		self.assertEqual(tr.Direction, 2)
		#Dont move off the board
		tr.Move()
		self.assertEqual(tr.X, 0)
		self.assertEqual(tr.Y, 3)
		self.assertEqual(tr.Direction, 2)

	def test_Right(self):
		tr = ToyRobot.ToyRobot()
		tr.Place(2,3,"SOUTH")
		tr.Right()
		self.assertEqual(tr.X, 2)
		self.assertEqual(tr.Y, 3)
		self.assertEqual(tr.Direction, 3)
		#Turn to North (roll over value)
		tr.Right()
		self.assertEqual(tr.X, 2)
		self.assertEqual(tr.Y, 3)
		self.assertEqual(tr.Direction, 0)

	def test_Left(self):
		tr = ToyRobot.ToyRobot()
		tr.Place(2,3,"NORTH")
		tr.Left()
		self.assertEqual(tr.X, 2)
		self.assertEqual(tr.Y, 3)
		self.assertEqual(tr.Direction, 3)
		tr.Left()
		self.assertEqual(tr.X, 2)
		self.assertEqual(tr.Y, 3)
		self.assertEqual(tr.Direction, 2)
		#Test Place after already placed
		tr.Place(4,4,"EAST")
		tr.Left()
		self.assertEqual(tr.X, 4)
		self.assertEqual(tr.Y, 4)
		self.assertEqual(tr.Direction, 0)

if __name__ == '__main__':
    unittest.main()

