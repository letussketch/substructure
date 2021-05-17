import math

class Element:
	"""docstring for Element"""
	"""cross section is Xsection class or any of its subclass"""
	"""node define start and end point of an element"""
	def __init__(self, nodes,x_section,modulus_of_elasticity):
		self.nodes =nodes
		self.node_start = nodes[0]
		self.node_end = nodes[1]
		self.x_section = x_section
		self.modulus_of_elasticity = modulus_of_elasticity



 		


class Xsection:
	"""docstring for Xsection"""
	def __init__(self,radius = 0,length = 0,width=0,area=0 ,coordinate=0 ,moment_of_inertia_major=0, moment_of_inertia_minor = 0 ,material = ""):

		self.radius = radius
		self.length = length
		self.width = width
		self.area = area
		self.coordinate = coordinate
		self.moment_of_inertia_major = moment_of_inertia_major
		self.moment_of_inertia_minor = moment_of_inertia_minor
		self.material = material
		

	def get_area (self, obj):
		return obj.area



class Circle(Xsection):
	"""docstring for Circle"""
	def __init__(self, radius):
		super(Circle, self).__init__(radius = radius, area = math.pi *radius**2, moment_of_inertia_major = math.pi*radius**4/4, moment_of_inertia_minor = math.pi*radius**4/4)

class Rectangle(Xsection):
	"""docstring for Rectangle"""
	def __init__(self, length, width):
		super(Rectangle, self).__init__(length = length, width = width, area= length*width, moment_of_inertia_major = min(length,width) * max(length,width)**3/12, moment_of_inertia_minor = max(length,width) * min(length,width)**3/12)

class DoubleD(Xsection):
	"""docstring for DoubleD"""
	def __init__(self, length, width):
		super(DoubleD, self).__init__(length = length, width = width, area= length*width+math.pi*width**2, moment_of_inertia_major = min(length,width) * max(length,width)**3/12 + math.pi * width**2 *(width**2 + 2*length**2)/8, moment_of_inertia_minor = max(length,width) * min(length,width)**3/12 + math.pi * width**4/4)	

		

class Irregular (Xsection):
	"""docstring for Irregular"""
	def __init__(self, coordinate):
		super(Irregular, self).__init__(coordinate = coordinate)
		self.area = self.calculate_area(coordinate)

	def calculate_area(self, coordinate):
	    a = 0
	    ox,oy = coordinate[0]
	    for x,y in coordinate[1:]:
	        a += (x*oy-y*ox)
	        ox,oy = x,y
	    return abs(a)/2



