from expr import Expr

class Var(Expr):
	priority = 3
	associativity = 0
	
	def __init__(self, key, *args, **kwargs):
		super(Var, self).__init__(*args, **kwargs)
		
		self.key = key
		
	def __repr__(self):
		return self.key
		
	def __str__(self):
		return self.key
		
	def value(self, **kwargs):
		if kwargs is not None and self.key in kwargs.keys():
			return kwargs[self.key]
		else:
			raise UnboundLocalError("Tried to find the value of the variable {}, but no value has been set.".format(self.key))

	def derivative(self, to = "x"):
		from const import Const
		if to == self.key:
			return Const(1)
		else:
			return Const(0)
