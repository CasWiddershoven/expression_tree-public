from expr import Expr

class Mod(Expr):
	def __init__(self, lhs, rhs, *args, **kwargs):
		super(Mod, self).__init__(*args, **kwargs)
		self.lhs = lhs
		self.rhs = rhs
		
	def __neg__(self):
		return Mod(self.lhs.__neg__(), self.rhs)
		
	def __repr__(self):
		return "({})%({})".format(lhs, rhs)
		
	def __str__(self):
		return "({})%({})".format(lhs, rhs)
		
	def __trunc__(self):
		return self
		
	def conjugate(self):
		return Mod(self.lhs.conjugate(), self.rhs.conjugate())
		
	@property
	def imag(self):
		return Mod(self.lhs.imag, self.rhs.imag)
		
	@property
	def real(self):
		return Mod(self.lhs.real, self.rhs.real)
		
	def value(self, **kwargs):
		return self.lhs.value(**kwargs) % self.rhs.value(**kwargs)
