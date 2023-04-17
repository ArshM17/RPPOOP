import math

class regularPolygon:
	def __init__(self,sides,sideLength):
		self.sides = sides
		self.sideLength = sideLength
	
	def perimeter(self):
		self.p = self.sides * self.sideLength
		print(self.p)

	def area(self):
		self.a = (((self.sideLength)**2)*self.sides)/(4*(math.tan(math.pi/self.sides)))
		print(self.a)
	
class square(regularPolygon):
	def __init__(self,sideLength):
		self.sides = 4
		self.sideLength = sideLength

class triangle(regularPolygon):
	def __init__(self,sideLength):
		self.sides = 3
		self.sideLength = sideLength
		
class pentagon(regularPolygon):
	def __init__(self,sideLength):
		self.sides = 5
		self.sideLength = sideLength
		
class hexagon(regularPolygon):
	def __init__(self,sideLength):
		self.sides = 6
		self.sideLength = sideLength
		
sq = square(4)
sq.perimeter()
sq.area()
tr = triangle(4)
tr.perimeter()
tr.area()
pe = pentagon(4)
pe.perimeter()
pe.area()
he = hexagon(4)
he.perimeter()
he.area()



