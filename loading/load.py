class Load:
	"""docstring for Load"""
	load_summary = {'dl':{},'sidl':{},'ll':{}}
	bearing_details = {'bearing_nodes':[], 'bearing_coordinates':[],'bearing_depth':0}
	superstructure_details = {'left':{'effective':0,'overall':0,'clear':0,'depth':0,'width':2*3.5},'right':{'effective':0,'overall':0,'clear':0,'depth':0,'width':2*3.5},'expension_gap':0.1}

	def __init__(self,load_type,name=""):
		if load_type in list(self.load_summary.keys()):
			self.load_type = load_type
			self.name = name

		else:
			#  raise exception - 
			print ('implementation will be soon')
			# alternate method to add load

	def set_bearing_details(**kwargs):
		""" takes following argument :
		1) bearing nodes number 
		2) bearing coordinates
		3) bearing depth (pedistal + bearing depth)
		"""
		# set bearing details should be made private and should not be used outside the load class, i.e. child classes

		self.bearing_details['bearing_nodes'] = kwargs['bearing_nodes']
		self.bearing_details['bearing_coordinates'] = kwargs['bearing_coordinates']

	def set_superstructure_details(self,**kwargs):
		self.superstructure_details['left'] = kwargs['left']
		self.superstructure_details['right'] = kwargs['right']
		self.superstructure_details['expension_gap'] = kwargs['expension_gap']

	def set_supersturcture_details_left(self,**kwargs):
		self.superstructure_details['left']['effective'] = kwargs['effective'] 
		self.superstructure_details['left']['overall'] = kwargs['overall'] 
		self.superstructure_details['left']['clear'] = kwargs['clear'] 
		self.superstructure_details['left']['depth'] = kwargs['depth'] 
		self.superstructure_details['left']['width'] = kwargs['width'] 

	def set_supersturcture_details_right(self,**kwargs):
		self.superstructure_details['right']['effective'] = kwargs['effective'] 
		self.superstructure_details['right']['overall'] = kwargs['overall'] 
		self.superstructure_details['right']['clear'] = kwargs['clear'] 
		self.superstructure_details['right']['depth'] = kwargs['depth'] 
		self.superstructure_details['right']['width'] = kwargs['width'] 


	def set_load(self,load_on_bearing):
		self.load_summary[self.load_type][self.name] = load_on_bearing

	def get_loads(self,name=''):
		''' common output format for all child class '''
		if name =='':
			return self.load_summary[self.load_type]
		else :
			return self.load_summary[self.load_type][self.name]





