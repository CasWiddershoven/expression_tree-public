class Div(Expr):
	def __init__(self, lhs, rhs, *args, **kwargs):
		super(Div, self).__init__(*args, **kwargs)
		self.lhs = lhs
		self.rhs = rhs
		
	def __neg__(self):
		return Div(self.lhs.__neg__(), self.rhs)
		
	def __repr__(self):
		return "({})/({})".format(self.lhs, self.rhs)
		
	def __str__(self):
		return "({})/({})".format(self.lhs, self.rhs)
		
	def __trunc__(self):
		return Trunc(self)
		
	def conjugate(self):
		return Div(self.lhs.conjugate(), self.rhs.conjugate())
		
	def derivative(self):
		return Div(Sub(Mul(self.lhs.derivative(), self.rhs), Mul(self.rhs.derivative(), self.lhs)), Pow(self.rhs, Const(2)))
		
	@property
	def imag(self):
		return Div(self.lhs.imag, self.rhs.imag)
		
	@property
	def real(self):
		return Add(self.lhs.real, self.rhs.real)
		
	def value(self, **kwargs):
		return self.lhs.value(**kwargs) / self.rhs.value(**kwargs)
