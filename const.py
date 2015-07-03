from expr import Expr

class Const(Expr):
	""" A constant value """
	priority = 4
	associativity = 0
	
	def __init__(self, val, *args, **kwargs):
		super(Const, self).__init__(*args, **kwargs)
		
		self.val = val
		
	def __neg__(self):
		return Const(-self.val)
		
	def __repr__(self):
		if self.val.imag == 0 and self.val >= 0:
			return str(self.val)
		else:
			return "({})".format(self.val)
		
	def __str__(self):
		if self.val.imag == 0 and self.val >= 0 or self.val.imag != 0:
			return str(self.val)
		else:
			return "({})".format(self.val)
			
	def conjugate(self, **kwargs):
		return Const(self.val.conjugate())
		
	def imagPart(self, **kwargs):
		return Const(self.val.imag)
		
	def realPart(self, **kwargs):
		return Const(self.val.real)
		
	def value(self, **kwargs):
		return self.val
		
	def derivative(self, to = "x"):
		return Const(0)
