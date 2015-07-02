class Var(Expr):
	def __init__(self, key, *args, **kwargs):
		super(Var, self).__init__(*args, **kwargs)
		
		self.key = key
		
	def value(self, **kwargs):
		if kwargs is not None and self.key in kwargs.keys():
			return kwargs[self.key]
		else:
			raise UnboundLocalError("Tried to find the value of the variable {}, but no value has been set.".format(self.key))
