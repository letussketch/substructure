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


		if 'load_on_bearings' in kwargs.keys():
			self.load_summary[self.load_type][self.name] = kwargs['load_on_bearings']



	def calculate_LL(self):
		''' tool to calculate superimposed dead load on beaarigns'''

		# self.load_summary[self.load_type][self.name] = 'calcualted dead load'
		pass

d = LL(name = 'tere naam')
print (d.load_type)
print(d.name)
print(d.load_summary)