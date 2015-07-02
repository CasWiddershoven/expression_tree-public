class Mul(Expr):
	def __init__(self, lhs, rhs, *args, **kwargs):
		super(Mul, self).__init__(*args, **kwargs)
		self.lhs = lhs
		self.rhs = rhs
		
	def __neg__(self):
		return Mul(self.lhs.__neg__(), self.rhs)
		
	def __repr__(self):
		return "({})*({})".format(lhs, rhs)
		
	def __str__(self):
		return "({})*({})".format(lhs, rhs)
		
	def __trunc__(self):
		return Trunc(self)
		
	def conjugate(self):
		return Mul(self.lhs.conjugate(), self.rhs.conjugate())
		
	def derivative(self):
		return Add(Mul(self.lhs.derivative(), self.rhs), Mul(self.lhs, self.rhs.derivative()))
		
	@property
	def imag(self):
		return Mul(self.lhs.imag, self.rhs.imag)
		
	@property
	def real(self):
		return Mul(self.lhs.real, self.rhs.real)
		
	def value(self, **kwargs):
		return self.lhs.value(**kwargs) * self.rhs.value(**kwargs)
