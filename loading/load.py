class Load:
	"""docstring for Load"""
	load_summary = {'dl':{},'sidl':{},'ll':{}}
	bearing_details = {'left':{'bearing_nodes':3, 'bearing_coordinates':[1.5],'bearing_depth':0.3,'carriageway_ecentricity':0},'right':{'bearing_nodes':2, 'bearing_coordinates':[1],'bearing_depth':0.3,'carriageway_ecentricity':0}}
	superstructure_details = {'left':{'effective':99,'overall':100,'clear':0,'depth':0,'width':3*3.5,'left_overhang':0},'right':{'effective':49.5,'overall':50,'clear':0,'depth':0,'width':3.5*3,'left_overhang':0},'expension_gap':0.01}
	carriageway_details = {'left':{'no_of_lane':1,'crash_barrier_left':0.45, 'foothpath_left':0,'median':0,'foothpath_right':0,'crash_barrier_right':0},'right':{'no_of_lane':1,'crash_barrier_left':0, 'foothpath_left':0,'median':0,'foothpath_right':0,'crash_barrier_right':0}}
	def __init__(self,load_type,name=""):
		if load_type in list(self.load_summary.keys()):
			self.load_type = load_type
			self.name = name

			### setting default bearing ecentricity (in longitudenal direction)
			bearing_ecentricity_left = 0.5*(self.superstructure_details['left']['overall'] - self.superstructure_details['left']['effective'] ) + 0.5*self.superstructure_details['expension_gap']
			bearing_ecentricity_right = 0.5*(self.superstructure_details['right']['overall'] - self.superstructure_details['right']['effective'] ) + 0.5*self.superstructure_details['expension_gap']
			self.superstructure_details['bearing_ecentricity'] = [bearing_ecentricity_left,bearing_ecentricity_right]

			### correction of bearing coordinates for equal spaced bearings  
			for span in self.bearing_details.keys():
				if self.bearing_details[span]['bearing_nodes']-1 != len(self.bearing_details[span]['bearing_coordinates']):
					self.bearing_details[span]['bearing_coordinates'] = [self.bearing_details[span]['bearing_coordinates'][0]]*(self.bearing_details[span]['bearing_nodes']-1)

		else:
			#  raise exception - 
			print ('implementation will be soon')
			# alternate method to add load

	def set_carriageway_details(self,**kwargs):
		# this class should be made private and should not be used outside the load class, i.e. child classes
		self.carriageway_details['left'] = kwargs['left']
		self.carriageway_details['right'] = kwargs['right']

	def set_carriageway_details_left(self,**kwargs):
		# this class should be made private and should not be used outside the load class, i.e. child classes
		self.carriageway_details['left']['no_of_lane'] = kwargs['no_of_lane']
		self.carriageway_details['left']['crash_barrier_left'] = kwargs['crash_barrier_left']
		self.carriageway_details['left']['foothpath_left'] = kwargs['foothpath_left']
		self.carriageway_details['left']['median'] = kwargs['median']
		self.carriageway_details['left']['foothpath_right'] = kwargs['foothpath_right']
		self.carriageway_details['left']['crash_barrier_right'] = kwargs['crash_barrier_right']

	def set_carriageway_details_right(self,**kwargs):
		# this class should be made private and should not be used outside the load class, i.e. child classes
		self.carriageway_details['right']['no_of_lane'] = kwargs['no_of_lane']
		self.carriageway_details['right']['crash_barrier_left'] = kwargs['crash_barrier_left']
		self.carriageway_details['right']['foothpath_left'] = kwargs['foothpath_left']
		self.carriageway_details['right']['median'] = kwargs['median']
		self.carriageway_details['right']['foothpath_right'] = kwargs['foothpath_right']
		self.carriageway_details['right']['crash_barrier_right'] = kwargs['crash_barrier_right']

	def set_bearing_details(self,**kwargs):
		# this class should be made private and should not be used outside the load class, i.e. child classes

		self.bearing_details['left'] = kwargs['left']
		self.bearing_details['right'] = kwargs['right']


		### equal spaced bearings 
		for span, details in kwargs.items():
			if details['bearing_nodes']-1 != len(details['bearing_coordinates']):
				details['bearing_coordinates'] = [details['bearing_coordinates'][0]]*(details['bearing_nodes']-1)

				### waring message for mismatch of bearing nodes and bearing coordinates
				if len(details['bearing_coordinates']) != 1 and details['bearing_nodes']>2 :
					print ('warning \n', 'please verify bearing distances')
					print('beaings are assumned as equal spaced with their c/c distance :',details['bearing_coordinates'][0])

	def set_bearing_details_left(self,**kwargs):
		""" takes following argument :
		1) bearing nodes number 
		2) bearing coordinates
		3) bearing depth (pedistal + bearing depth)
		"""
		# this class should be made private and should not be used outside the load class, i.e. child classes

		self.bearing_details['left']['bearing_nodes'] = kwargs['bearing_nodes']
		self.bearing_details['left']['bearing_coordinates'] = kwargs['bearing_coordinates']
		self.bearing_details['left']['bearing_depth'] = self.kwargs['bearing_depth']
		self.bearing_details['left']['carriageway_ecentricity'] = self.kwargs['carriageway_ecentricity']

		if self.bearing_details['left']['bearing_nodes']-1 != len(self.bearing_details['left']['bearing_coordinates']):
			self.bearing_details['left']['bearing_coordinates'] = [self.bearing_details['left']['bearing_coordinates'][0]]*(self.bearing_details['left']['bearing_nodes']-1)

			### waring message for mismatch of bearing nodes and bearing coordinates
			if len(self.bearing_details['left']['bearing_coordinates']) != 1 and self.bearing_details['left']['bearing_nodes']>2 :
				print ('warning \n', 'please verify bearing distances')
				print('beaings are assumned as equal spaced with their c/c distance :',self.bearing_details['left']['bearing_coordinates'][0])

	def set_bearing_details_right(self,**kwargs):
		""" takes following argument :
		1) bearing nodes number 
		2) bearing coordinates
		3) bearing depth (pedistal + bearing depth)
		"""
		# this class should be made private and should not be used outside the load class, i.e. child classes

		self.bearing_details['right']['bearing_nodes'] = kwargs['bearing_nodes']
		self.bearing_details['right']['bearing_coordinates'] = kwargs['bearing_coordinates']
		self.bearing_details['right']['bearing_depth'] = self.kwargs['bearing_depth']
		self.bearing_details['right']['carriageway_ecentricity'] = self.kwargs['carriageway_ecentricity']

		if self.bearing_details['right']['bearing_nodes']-1 != len(self.bearing_details['right']['bearing_coordinates']):
			self.bearing_details['right']['bearing_coordinates'] = [self.bearing_details['right']['bearing_coordinates'][0]]*(self.bearing_details['right']['bearing_nodes']-1)

			### waring message for mismatch of bearing nodes and bearing coordinates
			if len(self.bearing_details['right']['bearing_coordinates']) != 1 and self.bearing_details['right']['bearing_nodes']>2 :
				print ('warning \n', 'please verify bearing distances')
				print('beaings are assumned as equal spaced with their c/c distance :',self.bearing_details['right']['bearing_coordinates'][0])

	def set_superstructure_details(self,**kwargs):

		# this class should be made private and should not be used outside the load class, i.e. child classes

		self.superstructure_details['left'] = kwargs['left']
		self.superstructure_details['right'] = kwargs['right']
		self.superstructure_details['expension_gap'] = kwargs['expension_gap']
		if 'bearing_ecentricity' in kwargs.keys():
			self.superstructure_details['bearing_ecentricity'] = kwargs['bearing_ecentricity']
		else:
			bearing_ecentricity_left = 0.5*(self.superstructure_details['left']['overall'] - self.superstructure_details['left']['effective'] ) + 0.5*self.superstructure_details['expension_gap']
			bearing_ecentricity_right = 0.5*(self.superstructure_details['right']['overall'] - self.superstructure_details['right']['effective'] ) + 0.5*self.superstructure_details['expension_gap']
			self.superstructure_details['bearing_ecentricity'] = [bearing_ecentricity_left,bearing_ecentricity_right]

	def set_supersturcture_details_left(self,**kwargs):

		# this class should be made private and should not be used outside the load class, i.e. child classes

		self.superstructure_details['left']['effective'] = kwargs['effective'] 
		self.superstructure_details['left']['overall'] = kwargs['overall'] 
		self.superstructure_details['left']['clear'] = kwargs['clear'] 
		self.superstructure_details['left']['depth'] = kwargs['depth'] 
		self.superstructure_details['left']['width'] = kwargs['width'] 
		self.superstructure_details['left']['left_overhang'] = kwargs['left_overhang']

	def set_supersturcture_details_right(self,**kwargs):

		# this class should be made private and should not be used outside the load class, i.e. child classes

		self.superstructure_details['right']['effective'] = kwargs['effective'] 
		self.superstructure_details['right']['overall'] = kwargs['overall'] 
		self.superstructure_details['right']['clear'] = kwargs['clear'] 
		self.superstructure_details['right']['depth'] = kwargs['depth'] 
		self.superstructure_details['right']['width'] = kwargs['width'] 
		self.superstructure_details['right']['left_overhang'] = kwargs['left_overhang'] 
		

	def set_load(self,load_on_bearing):
		self.load_summary[self.load_type][self.name] = load_on_bearing

	def get_loads(self,name=''):
		''' common output format for all child class '''
		if name =='':
			return self.load_summary[self.load_type]
		else :
			return self.load_summary[self.load_type][self.name]




# l = Load('dl')
# l.set_bearing_details(left={'bearing_nodes':8, 'bearing_coordinates':[1,9,7],'bearing_depth':0.3,'carriageway_ecentricity':0},right={'bearing_nodes':2, 'bearing_coordinates':[1],'bearing_depth':0.3,'carriageway_ecentricity':0})
# print(l.bearing_details)
