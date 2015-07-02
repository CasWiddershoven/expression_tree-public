from expr import Expr

class Add(Expr):
	def __init__(self, lhs, rhs, *args, **kwargs):
		super(Add, self).__init__(*args, **kwargs)
		self.lhs = lhs
		self.rhs = rhs
		
	def __neg__(self):
		from sub import Sub
		return Sub(self.lhs.__neg__(), self.rhs)
		
	def __repr__(self):
		return "({})+({})".format(lhs, rhs)
		
	def __str__(self):
		return "({})+({})".format(lhs, rhs)
		
	def conjugate(self):
		return Add(self.lhs.conjugate(), self.rhs.conjugate())
		
	def derivative(self, to = "x"):
		return Add(self.lhs.derivative(to), self.rhs.derivative(to))
		
	@property
	def imag(self):
		return Add(self.lhs.imag, self.rhs.imag)
		
	@property
	def real(self):
		return Add(self.lhs.real, self.rhs.real)
		
	def value(self, **kwargs):
		return self.lhs.value(**kwargs) + self.rhs.value(**kwargs)
