from expr import Expr

class Const(Expr):
	""" A constant value """
	priority = 3
	associativity = 0
	
	def __init__(self, val, *args, **kwargs):
		super(Const, self).__init__(*args, **kwargs)
		
		self.val = val
		
	def __neg__(self):
		return Const(-self.val)
		
	def __repr__(self):
		return str(self.val)
		
	def __str__(self):
		return str(self.val)
		
	@property
	def imag(self):
		return Const(self.val.imag)
		
	@property
	def real(self):
		return Const(self.val.real)
		
	def value(self, **kwargs):
		return self.val
		
	def derivative(self, to = "x"):
		return Const(0)
