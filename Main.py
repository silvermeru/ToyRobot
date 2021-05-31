import sys
import ToyRobot

tr = ToyRobot.ToyRobot()

CMDReader = {
	"PLACE": tr.Place,
	"LEFT": tr.Left,
	"RIGHT": tr.Right,
	"MOVE": tr.Move,
	"REPORT": tr.Report
}

if __name__ == "__main__":
	text = input()

	while text != "CLOSE":
		text = text.replace(",", " ")
		toks = text.split()
		if toks[0] == "PLACE" and len(toks) == 4:
			tr.Place(int(toks[1]),int(toks[2]),toks[3])
		elif len(toks) == 1:
			func = CMDReader.get(toks[0], "Command not found")
			func()
		else:
			print("Command Not Found")
		text = input()
		


