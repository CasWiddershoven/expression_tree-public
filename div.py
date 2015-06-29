class Div(Expr):
	def __init__(self, lhs, rhs, *args, **kwargs):
		super(Div, self).__init__(*args, **kwargs)
		self.lhs = lhs
		self.rhs = rhs
		
	def __neg__(self):
		return Div(lhs.__neg__(), rhs)
		
	def __repr__(self):
		return "({})/({})".format(lhs, rhs)
		
	def __str__(self):
		return "({})/({})".format(lhs, rhs)
		
	def __trunc__(self):
		return Trunc(self)
		
	def conjugate(self):
		return Div(self.lhs.__neg__(), self.rhs)
		
	@property
	def imag(self):
		return Div(self.lhs.imag, self.rhs.imag)
		
	@property
	def real(self):
		return Add(self.lhs.real, self.rhs.real)
		
	def value(self):
		return self.lhs.value() + self.rhs.value()
