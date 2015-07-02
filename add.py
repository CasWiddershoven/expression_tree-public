from expr import Expr

class Add(Expr):
	""" Addition: Add: CxC -> C, (a + bi) + (a' + b'i) = a + a' + (b + b')i """
	def __init__(self, lhs, rhs, *args, **kwargs):
		super(Add, self).__init__(*args, **kwargs)
		self.lhs = lhs
		self.rhs = rhs
		
	def __neg__(self):
		from sub import Sub
		return Sub(self.lhs.__neg__(), self.rhs)
		
	def __nonzero__(self, **kwargs):
		from mul import Mul
		return Mul(self.lhs, self.rhs).__gt__(Const(0), kwargs) or # Both of the same sign and not zero
				self.lhs.__ne__(-self.rhs, **kwargs) or # Both of different signs but also of different absolute value
				(self.lhs.__nonzero__(kwargs) != self.rhs.__nonzero__(kwargs)) # Exactly one of them is zero
		
	def __repr__(self):
		return "({})+({})".format(self.lhs, self.rhs)
		
	def __str__(self):
		return "({})+({})".format(self.lhs, self.rhs)
		
	def conjugate(self):
		return Add(self.lhs.conjugate(), self.rhs.conjugate())
		
	@property
	def imag(self, **kwargs):
		return Add(self.lhs.imag(kwargs), self.rhs.imag(kwargs))
		
	@property
	def real(self, **kwargs):
		return Add(self.lhs.real(kwargs), self.rhs.real(kwargs))
		
	def value(self, **kwargs):
		return self.lhs.value(**kwargs) + self.rhs.value(**kwargs)
		
	def derivative(self, to = "x"):
		return Add(self.lhs.derivative(to), self.rhs.derivative(to))
