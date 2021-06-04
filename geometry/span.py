class Span :






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



