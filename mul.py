from expr import Expr

class Mul(Expr):
	def __init__(self, lhs, rhs, *args, **kwargs):
		super(Mul, self).__init__(*args, **kwargs)
		self.lhs = lhs
		self.rhs = rhs
		
	def __neg__(self):
		return Mul(self.lhs.__neg__(), self.rhs)
		
	def __repr__(self):
		return "({})*({})".format(self.lhs, self.rhs)
		
	def __str__(self):
		return "({})*({})".format(self.lhs, self.rhs)
		
	def conjugate(self):
		return Mul(self.lhs.conjugate(), self.rhs.conjugate())
		
	def derivative(self, to = "x"):
		from add import Add
		return Add(Mul(self.lhs.derivative(to), self.rhs), Mul(self.lhs, self.rhs.derivative(to)))
		
	@property
	def imag(self, **kwargs):
		from add import Add
		return Add(Mul(self.lhs.imag(kwargs), self.rhs.real(kwargs)), Mul(self.lhs.real(kwargs), self.rhs.imag(kwargs)))
		
	@property
	def real(self, **kwargs):
		from sub import Sub
		return Sub(Mul(self.lhs.real(kwargs), self.rhs.real(kwargs)), Mul(self.lhs.imag(kwargs), self.rhs.imag(kwargs)))
		
	def value(self, **kwargs):
		return self.lhs.value(**kwargs) * self.rhs.value(**kwargs)
