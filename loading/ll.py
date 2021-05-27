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





	def calculate_LL(self,vehicle = ""):
		''' tool to calculate superimposed dead load on beaarigns'''

		# self.load_summary[self.load_type][self.name] = 'calcualted live load'
		pass











	def define_vehicle(self,name="",axle_load =[],distance=[],longitudenal_clearance=100, transverse_clearance = [100,100],width = 2.3,tyre_width=0.5):

		self.vehicle[name] = {'axle_load':axle_load,'axle_distance':distance,'longitudenal_clearance' : longitudenal_clearance,'transverse_clearance': transverse_clearance,'width': width,'tyre_width' : tyre_width}


	def default_vehicle(self):
		

		''' modify above code based on code'''
		width = min(self.superstructure_details['left']['width'] ,self.superstructure_details['right']['width'])
		self.vehicle['classA'] = {'axle_load':[2.7, 2.7, 11.4, 11.4, 6.8, 6.8, 6.8, 6.8],'axle_distance':[0, 1.1, 3.2, 1.2, 4.3, 3, 3, 3],'longitudenal_clearance':20,'transverse_clearance':[0.15, 0.4  if (width <5.3) else min(0.4 + width-5.3,1.2)],'width':2.3,'tyre_width':0.5}
		self.vehicle['70R'] = {'axle_load':[17, 17, 17, 17, 12, 12, 8],'axle_distance':[0, 1.37, 3.05, 1.37, 2.13, 1.52, 3.96],'longitudenal_clearance':20,'transverse_clearance':[1.2,1.2],'width':2.79,'tyre_width':0.86}


	def reaction_calculator (self,vehicle_type,*args):
		''' calculate reaction Ra and Rb of individual strucutres
			parameters are :
			args[0] = details of 1st span as per required parameters in influence line + expension gap :
			args[1] = details of 2nd span as per required parameters in influence line
		'''
		vehicle = self.vehicle[vehicle_type]
		spans = [x[0] for x in  args]
		exp_gap = [x[-1] for x in args[:-1]]
		x_total = sum(spans) + sum(exp_gap)
		no_of_vehicle = int (2+ x_total /sum(vehicle['axle_distance']))
		axle = vehicle['axle_load']*no_of_vehicle
		distance = vehicle['axle_distance']*no_of_vehicle

		



	def influence_line(self,x,*args,**kwargs):
		''' calculate influence line of structures
			parameters:
			for simply supported :
				args[0]		: overall span 
				args[1]		: effective span 
				args[2]		: left overhang (optional)
			for continuous:
				args[0]		: overall span 
				args[1]		: effective span 
				args[2]		: left overhang (optional)
				args[4]		: span 1
				args[5]		: span 2
				args[6]		: span 3
				...
			for cantelever:
				args[0]		: overall span
				args[1]		: left/right
			bridge_type : continuous, simply_supported, cantelever
			'''
		if kwargs['bridge_type'] in ['ss', 'simply_supported']:
			os = args[0]
			es = args[1]
			if len(args) == 3:
				lo = args[2]
			else:
				lo = 0

			a = lo if lo != 0 else 0.5*(os-es)
			b = os-es-lo
			return ( 1-(x-a)/es, (x-a)/es )

		elif kwargs['bridge_type'] in ['cantelever','cant']:
			if args[1] == 'left':
				return (1,0)
			else :
				return (0,1)
		elif kwargs['bridge_type'] in ['continuous', 'c'] :
			# to be implemented
			pass



