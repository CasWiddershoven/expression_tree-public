from expr import Expr

class Mod(Expr):
	def __init__(self, lhs, rhs, *args, **kwargs):
		super(Mod, self).__init__(*args, **kwargs)
		self.lhs = lhs
		self.rhs = rhs
		
	def __neg__(self):
		return Mod(self.lhs.__neg__(), self.rhs)
		
	def __repr__(self):
		return "({})%({})".format(self.lhs, self.rhs)
		
	def __str__(self):
		return "({})%({})".format(self.lhs, self.rhs)
		
	def __trunc__(self):
		return self
		
	def conjugate(self):
		# Complex numbers don't support modulo, so we'll just assume both lhs and rhs are real.
		return self
		
	@property
	def imag(self):
		from nserror import NotSupportedError
		raise NotSupportedError("Complex numbers don't support modulo")
		
	@property
	def real(self):
		return Mod(self.lhs.real, self.rhs.real)
		
	def value(self, **kwargs):
		return self.lhs.value(**kwargs) % self.rhs.value(**kwargs)
