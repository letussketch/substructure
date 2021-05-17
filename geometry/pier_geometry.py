import math
from geometry.Element import *

class PierGeometry:
	# self.element_list = []

	def __init__(self, pier_height=5, pier_cap_length=5,ecentricity = 0, bearing_layout=(1.5,1.5), dist_of_first_bearign_from_pier_cap_left=1, bearing_height = 300):
		self.set_dimension (pier_height, pier_cap_length,ecentricity )		
		self.set_bearing_details(bearing_layout, dist_of_first_bearign_from_pier_cap_left, bearing_height )
		self.structure_skeleton()

		# default modulus of elasticity
		self.E = {"pier":30000,"pier_cap": 30000}

	def set_dimension (self, pier_height, pier_cap_length,ecentricity = 0):
		self.pier_height = pier_height
		self.pier_cap_length = pier_cap_length
		self.ecentricity = ecentricity


	def set_bearing_details(self, bearing_layout, dist_of_first_bearign_from_pier_cap_left, bearing_height = 300):
		""" bearing_layout is a tuple containing distance between bearing"""
		self.bearing_layout = bearing_layout
		self.bearing_height = bearing_height
		self.dist_of_first_bearign_from_pier_cap_left = dist_of_first_bearign_from_pier_cap_left


	def set_modulus_of_elasticity (self, **kwargs):
		self.E = {"pier": kwargs["pier"],"pier_cap": kwargs["pier_cap"]}

	def set_x_section_pier(self,*args):
		self.x_section_pier =  self.set_x_section(args)

	def set_x_section_pier_cap(self,*args):
		self.x_section_pier_cap =  self.set_x_section(args)

	def set_x_section(self,*args):
		""" input will be in the form of (x-section, dis, x-section, dis, x-section, dis, .........., x-section)
		x-section = input will be in the form of - (shape, dim1,dim2), dim2 is optional for circular pier
		dis 	  = distance between 2 different cross section, negative distance represent tappering

		""" 

		### correction for *args argument

		if len(args)==1 :
			args = args[0]
			if type(args[0]) == tuple or type(args[0]) == list :
				pass
			else:
				args = [args]

		### correction for *args ends


		x_section_details = {}

		if type(args[-1]) != list and type(args[-1]) != tuple:
			print ("verify input, last item of input must be x-section")

		for x in range (0,len(args),2):

			if args[x][0] == "circle" or args[x][0] == "circular":
				x_section_details [Circle(args[x][1])] = sum(list(x_section_details.values())) + args[x+1] if x+1<len(args) else self.pier_cap_length 
			elif args[x][0] == 'rectangle':
				x_section_details [Rectangle(args[x][1],args[x][2])] = sum(list(x_section_details.values())) + args[x+1] if x+1<len(args) else self.pier_cap_length 
			elif args[x][0] == 'doubleD' or args[x][0] == 'doubled' or args[x][0] == 'double_d':
				x_section_details[DoubleD(args[x][1],args[x][2])] = sum(list(x_section_details.values())) + args[x+1] if x+1<len(args) else self.pier_cap_length 
			else:
				print ('either inputed shape is wrong or will be implemented shortly')

		return x_section_details

	def structure_skeleton(self):

		### pier coordinate
		self.pier_coordinates = [(0,0),(0,self.pier_height)]

		### pier cap coordinate

		## left edge
		pier_cap_x_coordinates = [(-self.pier_cap_length*0.5-self.ecentricity)]
		pier_cap_x_coordinates = pier_cap_x_coordinates + [pier_cap_x_coordinates[-1]+self.dist_of_first_bearign_from_pier_cap_left]
		
		for bearing_dist in self.bearing_layout:
			pier_cap_x_coordinates = pier_cap_x_coordinates + [pier_cap_x_coordinates[-1] + bearing_dist]

		## add end node
		pier_cap_x_coordinates = pier_cap_x_coordinates + [self.pier_cap_length*0.5-self.ecentricity]

		## add junction node 
		pier_cap_x_coordinates = pier_cap_x_coordinates + [0.0] 

		## remove duplicate
		pier_cap_x_coordinates = list(set(pier_cap_x_coordinates))

		## sorting node
		pier_cap_x_coordinates.sort()

		## adding y coordinate
		self.pier_cap_coordinate = [(x,self.pier_height) for x in pier_cap_x_coordinates]

		## adding important coordinates like bearing
		self.important_nodes = {"bearings" : [self.pier_cap_coordinate[x] for x in range(1,len(self.pier_cap_coordinate)-1)],"pier_cap_ends": [self.pier_cap_coordinate[0],self.pier_cap_coordinate[-1]], 'support':self.pier_coordinates[0]}




	def anastruct_element (self):
		self.anastruct_element = {}
		### add extra node to pier cap based on section property

		## only x coordinate of pier cap skeliton
		pier_cap_x_coordinate = [x[0] for x in self.pier_cap_coordinate]


		## implementing node based on change in section of pier cap
		pier_cap_left_end = self.important_nodes["pier_cap_ends"][0][0]
		pier_cap_section_coordinates = [pier_cap_left_end + x for x in  self.x_section_pier_cap.values()]

		## clubbing all nodes of pier cap
		pier_cap_x_coordinate_all = list(set(pier_cap_x_coordinate+pier_cap_section_coordinates))
		pier_cap_x_coordinate_all.sort()


		## generating anastruct elements for pier cap , i.e. element = (nodi1,node2,EA,EI)
		anastruct_ele=[]

		x_coordinates = pier_cap_x_coordinate_all
		for keys, values in self.x_section_pier_cap.items() :
			temp_list = []
			for index in range(len(x_coordinates)-1):
				
				if x_coordinates[index] <values+pier_cap_left_end:
					anastruct_ele = anastruct_ele + [(((x_coordinates[index],self.pier_height),(x_coordinates[index+1],self.pier_height)),self.E["pier_cap"]*keys.area,self.E["pier_cap"]*keys.moment_of_inertia_major)]
					temp_list = temp_list + [x_coordinates[index]]

			x_coordinates = list(set(x_coordinates)-set(temp_list))


		self.anastruct_element['pier_cap'] = anastruct_ele


		#____________________________________________________________________________________#

		### adding extra node to pier based on section property

		## only y coordinate of pier cap skeliton
		pier_y_coordinate = [x[1] for x in self.pier_coordinates]
		
		## implementing node based on change in section of pier cap
		pier_bottom_end = self.important_nodes["support"][1]
		pier_section_coordinates = [pier_bottom_end + x for x in  self.x_section_pier.values()]

		## clubbing all nodes of pier cap
		pier_y_coordinate_all = list(set(pier_y_coordinate+pier_section_coordinates))
		pier_y_coordinate_all.sort()

		## generating anastruct elements for pier, i.e. element = (nodi1,node2,EA,EI)
		anastruct_ele=[]

		y_coordinates = pier_y_coordinate_all
		for keys, values in self.x_section_pier.items() :
			temp_list = []
			for index in range(len(y_coordinates)-1):
				
				if y_coordinates[index] <values+pier_bottom_end:
					anastruct_ele = anastruct_ele + [(((0,y_coordinates[index]),(0,y_coordinates[index+1])),self.E["pier"]*keys.area,self.E["pier"]*keys.moment_of_inertia_major)]
					temp_list = temp_list + [y_coordinates[index]]

			y_coordinates = list(set(y_coordinates)-set(temp_list))


		self.anastruct_element['pier'] = anastruct_ele
		print (self.anastruct_element)



# a = PierGeometry()
# print (a.pier_coordinates)

# print(a.set_x_section (('circle',2)))


# a.set_x_section_pier_cap(('circle',2),2,('doubled',2,3),1,('rectangle',1,2))
# # a.set_x_section_pier_cap(('circle',2))
# print (a.x_section_pier_cap)

# a.set_x_section_pier(('circle',2),2,('doubled',2,3),1,('rectangle',1,2))
# print (a.x_section_pier)

# sections = list(a.x_section_pier_cap.keys())
# print (sections[0].moment_of_inertia_major)

# a.anastruct_element()


# print(a.pier_cap_coordinate)