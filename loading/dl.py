from load import Load

class DL(Load):
	"""docstring for DL"""
	''' it takes two default arguments
	name = name of DL
	load_on_bearing = load on each bearings due to dead load'''
	def __init__(self, **kwargs):

		if 'name' in kwargs.keys():
			name  = kwargs['name']
		else :
			### default name = ''
			name = ''

		super(DL, self).__init__('dl',name)


		if 'load_on_bearings' in kwargs.keys():
			self.load_summary[self.load_type][self.name] = kwargs['load_on_bearings']




	def calculate_dl(self):
		''' tool to calculate dead load on beaarigns'''


		# self.load_summary[self.load_type][self.name] = 'calcualted dead load'
		pass

