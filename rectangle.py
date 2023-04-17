class rectangle:
	def __init__(self,length,breadth):
		self.length=length 
		self.breadth=breadth
	
	def perimeter(self):
		self.p =2* (self.length+self.breadth)
		print(self.p)
		
	def area(self):
		self.a = (self.length*self.breadth)
		print(self.a)
	
	def changeDim(self ,newlength,newbreadth):
		b=int(input("What do you want to change: 1)Length 2)Breadth 3)Both:"))
		if(b==1):
			c = int(input("Enter new length:"))
			self.length = c
		elif(b==2):
			c = int(input("Enter new breadth:"))
			self.breadth = c
		elif(b==3):	
			l = int(input("Enter new length:"))
			b = int(input("Enter new breadth:"))
			self.length = l
			self.breadth = b
		else:
			print("Invalid option")

	def getLength(self):
		print(self.length)
		
	def getBreadth(self):
		print(self.breadth)
try:
	l=float(input("Enter length of rectangle:"))
	b=float(input("Enter breadth of rectangle:"))


rect=rectangle(l,b)
while(True):
	a=int(input("Which operation you want to perform:\n1)Find perimeter of rectangle\n2)Find area\n3)Change Dimension\n4)View Dimensions \n5)Quit\nChoose Option:"))
	if(a==1):
		rect.perimeter()
	elif(a==2):
		rect.area()
	elif(a==3):
		rect.changeDim()
	elif(a==4):
		rect.getLength()
		rect.getBreadth()
	elif(a==5):
		break;
	else:
		print("Invalid Input")
