from expr import Expr

class Const(Expr):
	def __init__(self, val, *args, **kwargs):
		super(Const, self).__init__(*args, **kwargs)
		
		self.val = val
		
	def __neg__(self):
		return Const(-self.val)
		
	@property
	def imag(self):
		return self.val.imag
		
	def derivative(self, to = "x"):
		return Const(0)
		
	@property
	def real(self):
		return self.val.real
		
	def value(self, **kwargs):
		return self.val
