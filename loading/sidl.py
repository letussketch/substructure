from load import Load

class SIDL(Load):
	"""docstring for SIDL"""
	''' it takes two default arguments
		name = name of SIDL
		load_on_bearing = load on each bearings due to superimposed dead load'''
	def __init__(self, **kwargs):

		if 'name' in kwargs.keys():
			name  = kwargs['name']
		else :
			### default name = ''
			name = ''

		super(SIDL, self).__init__('sidl',name)


		if 'load_on_bearings' in kwargs.keys():
			self.load_summary[self.load_type][self.name] = kwargs['load_on_bearings']



	def calculate_sidl(self):
		''' tool to calculate superimposed dead load on beaarigns'''



		# self.load_summary[self.load_type][self.name] = 'calcualted dead load'
		pass

		