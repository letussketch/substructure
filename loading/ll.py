from load import Load

class LL(Load):
	"""docstring for LL"""
	''' it takes two default arguments
		name = name of LL
		load_on_bearing = load on each bearings due to live load'''
	def __init__(self, **kwargs):

		if 'name' in kwargs.keys():
			name  = kwargs['name']
		else :
			### default name = ''
			name = ''

		super(LL, self).__init__('ll',name)


		### set default vehicle ###
		self.vehicle = {}
		self.default_vehicle()
		self.results ={'vehicle_run':[]}





	def calculate_LL(self,vehicle = ""):
		''' tool to calculate live load on beaarigns'''

		# self.load_summary[self.load_type][self.name] = 'calcualted live load'
		



	def define_vehicle(self,name="",axle_load =[],distance=[],longitudenal_clearance=100, transverse_clearance = [100,100],width = 2.3,tyre_width=0.5):

		self.vehicle[name] = {'axle_load':axle_load,'axle_distance':distance,'longitudenal_clearance' : longitudenal_clearance,'transverse_clearance': transverse_clearance,'width': width,'tyre_width' : tyre_width}

	def default_vehicle(self):
		
		''' modify above block of code based on design reference codes'''
		width = min(self.superstructure_details['left']['width'] ,self.superstructure_details['right']['width'])

		self.vehicle['classA'] = {'axle_load':[2.7, 2.7, 11.4, 11.4, 6.8, 6.8, 6.8, 6.8],'axle_distance':[0, 1.1, 3.2, 1.2, 4.3, 3, 3, 3],'longitudenal_clearance':20,'transverse_clearance':[0.15, 0.4  if (width <5.3) else min(0.4 + width-5.3,1.2)],'width':2.3,'tyre_width':0.5}
		self.vehicle['70R'] = {'axle_load':[17, 17, 17, 17, 12, 12, 8],'axle_distance':[0, 1.37, 3.05, 1.37, 2.13, 1.52, 3.96],'longitudenal_clearance':20,'transverse_clearance':[1.2,1.2],'width':2.79,'tyre_width':0.86}

	def transverse_ecentricity (self,carriageway_width,vehicle_type =''):
		''' calculates transverse ecentricity for a given carriageway '''
		pass

	def transverse_clearance_classA(self,width):
		''' a helper function for calculating transver clearance of class A vehicle '''
		return [0.15, 0.4  if (width <5.3) else min(0.4 + width-5.3,1.2)]

	def vehicle_arrangements(self,carriageway):
		''' As per IRC 6 -2016'''
		vehicle_arrangements = []
		if carriageway <2.6:
			pass
		elif carriageway>=2.6 and carriageway <4.25:
			vehicle_arrangements = [['classA']]

		elif carriageway>=4.25 and carriageway <5.35:
			### q need to be implemented 
			vehicle_arrangements = [['classA']]	
		elif carriageway>=5.3 and carriageway <9.6:

			vehicle_arrangements = [['classA','classA'],['70R']]	

		elif carriageway>=9.6 and carriageway <13.1:

			if carriageway <9.7:
				vehicle_arrangements = [['classA','classA','classA']]	
			else :
				vehicle_arrangements = [['classA','classA','classA'],['classA','70R']]	

		elif carriageway>=13.1 and carriageway <16.6:

			if carriageway <13.2:
				vehicle_arrangements = [['classA','classA','classA','classA']]	
			elif carriageway >=13.2 and carriageway <14.5 :
				vehicle_arrangements = [['classA','classA','classA','classA'],['classA','classA','70R']]	
			else:
				vehicle_arrangements = [['classA','classA','classA','classA'],['classA','classA','70R'],['70R','70R']]	

		elif carriageway>=16.6 and carriageway <20.1:

			if carriageway <16.7:
				vehicle_arrangements = [['classA','classA','classA','classA','classA']]	
			elif carriageway >=16.7 and carriageway <16.8 :
				vehicle_arrangements = [['classA','classA','classA','classA','classA'],['classA','classA','classA','70R'],['classA','70R','70R']]	
			else:
				vehicle_arrangements = [['classA','classA','classA','classA','classA'],['classA','classA','classA','70R'],['classA','70R','70R'],['70R','classA','70R']]	

		elif carriageway>=20.1 and carriageway <23.6:

			if carriageway <20.2:
				vehicle_arrangements = [['classA','classA','classA','classA','classA','classA']]	
			elif carriageway >=20.2 and carriageway <20.3 :
				vehicle_arrangements = [['classA','classA','classA','classA','classA','classA'],['classA','classA','classA','classA','70R'],['classA','classA','70R','70R']]	
			else:
				vehicle_arrangements = [['classA','classA','classA','classA','classA','classA'],['classA','classA','classA','classA','70R'],['classA','classA','70R','70R'],['70R','classA','classA','70R']]	
		
		return vehicle_arrangements

	def vehicle_ecentricity(self,list_of_vehicles,load_details={},left_span = True):
		''' only for one vehicular combination'''
		### implemented for carriageway without medians (i.e. undivided carriageway)



		carriageway_margin =0
		centerline_carriageway= 0
		bearing_carriageway_ecentricity = 0

		if left_span:
			carriageway_margin = self.carriageway_details['left']['crash_barrier_left']+self.carriageway_details['left']['foothpath_left']
			centerline_carriageway= self.superstructure_details['left']['width']*0.5
			bearing_carriageway_ecentricity = self.bearing_details['left']['carriageway_ecentricity']
			### calculating superstructure width
			for key, value in self.carriageway_details['left'].items():
				if key == 'no_of_lane':       #### not cohessive 
					pass
				else :
					centerline_carriageway = centerline_carriageway + value*0.5
		else :
			carriageway_margin = self.carriageway_details['right']['crash_barrier_left']+self.carriageway_details['right']['foothpath_left']
			centerline_carriageway= self.superstructure_details['right']['width']*0.5
			bearing_carriageway_ecentricity = self.bearing_details['right']['carriageway_ecentricity']

			### calculating superstructure width
			for key, value in self.carriageway_details['left'].items():
				if key == 'no_of_lane':       #### not cohessive 
					pass
				else :
					centerline_carriageway = centerline_carriageway + value*0.5


		ecentricity = 0
		load_sum = {'mlm':0,'mvf':0}          #### not cohessive
		lever_arm_sum = {'mlm':0,'mvf':0}	  #### not cohessive
		result_dict = {}

		
		for index in range(len(list_of_vehicles)):

			### calculating and updating load_details of each vehicle 
			if list_of_vehicles[index] in load_details.keys():
				### to avoid recalculation of reactions
				pass
			else:
				### if no result for vehicle in load_details then reaction calculator will calculate the reactions on bearing
				reaction_container = self.reaction_calculator(list_of_vehicles[index])

				### saving important results
				self.results['vehicle_run'] += [{list_of_vehicles[index] : reaction_container}]
				###

				load_details[list_of_vehicles[index]]= {'mvf' :reaction_container['max_vertical_force']['reactions'][1:3],'mlm' :reaction_container['max_longitudenal_moment']['reactions'][1:3]}

			### calculating ecentricity from leftmost end of carriageway
			if index ==0:
				### ecentricity = (crashbarrier and footpath) + f + 0.5 x width of vehicle 
				ecentricity = carriageway_margin+ self.vehicle[list_of_vehicles[index]]['transverse_clearance'][0] + self.vehicle[list_of_vehicles[index]]['width']*0.5

			else:
				### ecentricity = privious ecentricity + last vehicle width x 0.5 + transverse clearance from last vehicle (g_last) + current vehicle width x 0.5
				ecentricity = ecentricity + self.vehicle[list_of_vehicles[index-1]]['width']*0.5 + self.vehicle[list_of_vehicles[index-1]]['transverse_clearance'][1] + self.vehicle[list_of_vehicles[index]]['width']*0.5



			for key, value in load_details[list_of_vehicles[index]].items():

				
				lever_arm_sum[key] = lever_arm_sum[key]  + ecentricity * value[0 if left_span else 1]
				load_sum[key] = load_sum[key]  + value[0 if left_span else 1]

				result_dict[key] = (load_sum[key] ,centerline_carriageway -  (lever_arm_sum[key]/load_sum[key] if load_sum[key] != 0 else 0) +bearing_carriageway_ecentricity)
				###														to avoid divisible by zero in calculating lever arm 

		return result_dict

	def bearing_load(self,left_span = True):

		no_of_bearings = 0
		bearing_distances = []

		if left_span:
			no_of_bearings =  self.bearing_details['left']['bearing_nodes']
			bearing_distances = self.bearing_details['left']['bearing_coordinates']
			superstructure_width = self.superstructure_details['left']['width']
		else:
			no_of_bearings =  self.bearing_details['right']['bearing_nodes']
			bearing_distances = self.bearing_details['right']['bearing_coordinates']
			superstructure_width = self.superstructure_details['right']['width']

		### adding 1st bearing coordinate = 0 

		bearing_distances = [0]+ bearing_distances

		cum_bearing_distance = [sum(bearing_distances[:x+1]) for x in range(len ( bearing_distances))]
		bearing_center = sum(bearing_distances)/2
		r = [dis-bearing_center for dis in cum_bearing_distance]
		r_square = [dis**2 for dis in r ]
		sum_r_square = sum(r_square)
		### getting arrangement of vehicle for a given carriageway width 
		possible_arrangements = self.vehicle_arrangements(superstructure_width)
		### saving important results
		self.results['transverse_vehicle_arrangements'] = possible_arrangements
		###

		load_cases = [self.vehicle_ecentricity(arrangement,left_span = left_span) for arrangement in possible_arrangements]
		### saving important results 
		self.results['transverse_vehicle_ecentricity'] = load_cases
		load_on_bearing = {}
		result=[]
		for x in range(len(load_cases)):
			for keys, values in load_cases[x].items():

				p = values[0]
				M = values[0]*values[1]

				bearing_loads = [p + M * radial_distance /sum_r_square for radial_distance in r ]
				
				load_on_bearing[ keys] = [p + M * radial_distance /sum_r_square for radial_distance in r ]
				# load_on_bearing['load case '+ str(x+1)+ ':' + keys] = [p + M * radial_distance /sum_r_square for radial_distance in r ]
			result += [load_on_bearing]
			
		self.results['bearing_reaction'] = result
		return result





	# def no_of_vehicle(self,carriageway,existing_vehicles):

	# 	# if vehicle in self.vehicle.keys():
	# 	# 	clearance = self.vehicle['transverse_clearance'] 

	# 	# else:
	# 	# 	print ('unknown vehicle \n', 'please define vehicle\n')
	# 	# 	print ('available vehicles are : \n' ,self.vehicle.keys())
	# 	# 	return 0
	# 	pass



	# def no_of_vehicle_on_carriageway(self,carriageway_width=0):
	# 	### needs correction

	# 	### for calculation of class A vehicle 
	# 	no_of_vehicles = {}
	# 	if carriageway_width ==0:
	# 		carriageway_width = min(self.superstructure_details['left']['width'] ,self.superstructure_details['right']['width'])


	# 	clearance = self.transverse_clearance_classA(carriageway_width)

	# 	### formula applicable for upto 10 lanes can be increased if required
		
	# 	for x in range(0,10):
	# 		for vehicle in self.vehicle.keys():

	# 			if vehicle == 'classA':
					
	# 				if carriageway_width >= 2 * clearance[0] + x * self.vehicle[vehicle]['width'] + (x-1) * clearance[1]:
	# 					no_of_vehicles[vehicle] = x
						
	# 			else:
	# 				if carriageway_width >= 2 * self.vehicle[vehicle]['transverse_clearance'][0] + x * self.vehicle[vehicle]['width'] + (x-1) * self.vehicle[vehicle]['transverse_clearance'][1]:
	# 					print(2 * self.vehicle[vehicle]['transverse_clearance'][0], x * self.vehicle[vehicle]['width'] , (x-1) * self.vehicle[vehicle]['transverse_clearance'][1])
	# 					no_of_vehicles[vehicle] = x
				
	# 			# if no_of_vehicles.keys() == self.vehicle.keys():
	# 	return no_of_vehicles


	def reaction_calculator (self,vehicle_type,*args):
		''' calculate reaction Ra and Rb of individual strucutres
			parameters are :
			vehicle from relevent code
		'''
		increment = 0.1
		### getting details of beidge from Load class
		left = self.superstructure_details['left']
		right = self.superstructure_details['right']
		exp = self.superstructure_details['expension_gap']
		bearing_ecentricity = self.superstructure_details['bearing_ecentricity']
		### check if vehicle exist in vehicle database
		if vehicle_type in self.vehicle.keys():
			vehicle = self.vehicle[vehicle_type]
		else:
			print('please select vehicle form existing database:')
			[print (key +'\n') for key in self.vehicle.keys()]  

			print ('Or define custom vehicle and then run the function')
			return -1

		### calculate total vehicle length
		vehicle_length = sum(vehicle['axle_distance']) + vehicle['longitudenal_clearance']
		### calculate total bridge length
		x_total = left['overall'] + exp + right['overall'] 
		### calculate number of vehicle to run on span 
		no_of_vehicle = int (2+ x_total /vehicle_length)
		### generate arrays of axle loads
		axle = vehicle['axle_load']*no_of_vehicle
		### generate arrays of axle distance
		dis = vehicle['axle_distance'] + ([vehicle['longitudenal_clearance']] + vehicle['axle_distance'][1:])*(no_of_vehicle-1)
		### generate cumulative distance with first axle placed at 0 with origin at start of left span.
		distance = [-sum(dis[:x+1]) for x in range(len(dis))]

		reactions = {}
		pier_load = 0
		pier_moment = 0

		# temp_dict = {}
		for x in range(0,int((vehicle_length*(no_of_vehicle+1))/increment) ):

			inc = x * increment
			### activate distances (+ve) of all the axle loads lie on left span 
			left_span_active_dist = [x + inc if  x + inc <= left['overall'] else -1 for x in distance]
			### activate distances (+ve) of all the axle loads lie on right span 
			right_span_active_dist = [x + inc-exp-left['overall'] if x + inc-exp-left['overall'] <= right['overall'] else -1 for x in distance]
			### get influence line values of all loads for left span (values are in the form of tuples of both reactions of span )
			left_il = [self.influence_line_ss(x,left['overall'],left['effective'],left['left_overhang']) for x in left_span_active_dist ]
			### get influence line values of all loads for right span (values are in the form of tuples of both reactions of span )
			right_il = [self.influence_line_ss(x,right['overall'],right['effective'],right['left_overhang']) for x in right_span_active_dist ]

			temp_reaction = [0,0,0,0]
			for index in range(len(axle)):
				### multiplying each influence line values to axle loads to get reactions
				left_1,left_2,right_1,right_2 = temp_reaction
				### getting reactions of left span 
				left_1 = left_1 + left_il[index][0]*axle[index]
				left_2 = left_2 + left_il[index][1]*axle[index]
				### getting reactions of right span 
				right_1 = right_1 + right_il[index][0] *axle[index]
				right_2 = right_2 + right_il[index][1] *axle[index]

				temp_reaction = [round(left_1,2),round(left_2,2),round(right_1,2),round(right_2,2)]


			if temp_reaction[1] + temp_reaction[2] > pier_load:
				### updating maximum vertical force
				pier_load = temp_reaction[1] + temp_reaction[2] 
				### getting reaction corresponding to maximum vertical force
				reactions['max_vertical_force'] = {'x': inc, 'reactions':temp_reaction}

			if abs(temp_reaction[1]*bearing_ecentricity[0] - temp_reaction[2]*bearing_ecentricity[1]) > pier_moment:
				### updating maximum longitudenal moment
				pier_moment = temp_reaction[1]*bearing_ecentricity[0] - temp_reaction[2]*bearing_ecentricity[1]
				### getting reaction corresponding to maximum longitudenal moment
				reactions['max_longitudenal_moment'] = {'x': inc, 'reactions':temp_reaction}
		return reactions

	def influence_line_ss(self,x,overall_span,effective_span, left_overhang=0):
		''' calculate influence line of span
			parameters:
			for simply supported :
				x : axle distance from left end
				overall span 
				effective span 
				left overhang (optional)
			'''

		os = overall_span
		es = effective_span
		lo = left_overhang

		a = lo if lo != 0 else 0.5*(os-es)
		b = os-es-lo
		return ( 1-(x-a)/es if x >=0 else 0, (x-a)/es if x>=0 else 0 )

a = LL()
# print (a.reaction_calculator('70R'))
print(a.bearing_load())
print ('_'*15)
print(a.results)

# print (a.no_of_vehicle_on_carriageway(9.6))
# a.no_of_vehicle('classA',3.5,'')