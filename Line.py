#   Define a Line class which consists of two Points. 
#   Points are defined by x and y coordinate values. Provide a method in the Line class which returns the length of the Line.
import math 

class Line():
	x1 = 0
	y1 = 0
	x2 = 0
	y2 = 0
	def __init__(self, x1, y1, x2, y2):
		self.y1 = y1
		self.x1 = x1
		self.x2 = x2
		self.y2 = y2
		pass
	
	def lineLength(self):
		x = self.x1 + self.x2
		y = self.y1 + self.y2
		return math.sqrt(x^2 + y^2)

line = Line(2,4,2,4)
print(line.lineLength())