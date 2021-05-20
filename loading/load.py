class Load:
	"""docstring for Load"""
	load_summary = {'dl':{},'sidl':{},'ll':{}}
	bearing_details = {'bearing_nodes':[], 'bearing_coordinates':[],'bearing_depth':0}
	superstructure_details = {'left':{'effective':0,'overall':0,'clear':0,'depth':0,'width':0},'right':{'effective':0,'overall':0,'clear':0,'depth':0,'width':0}}

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
		pass
	def set_supersturcture_details_left(self,**kwargs):
		pass
	def set_supersturcture_details_right(self,**kwargs):
		pass



	def get_loads(self,name=''):
		''' common output format for all child class '''
		if name =='':
			return self.load_summary[self.load_type]
		else :
			return self.load_summary[self.load_type][self.name]





