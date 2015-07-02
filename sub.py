class Sub(Expr):
	def __init__(self, lhs, rhs, *args, **kwargs):
		super(Sub, self).__init__(*args, **kwargs)
		self.lhs = lhs
		self.rhs = rhs
		
	def __neg__(self):
		return Add(self.lhs.__neg__(), self.rhs)
		
	def __repr__(self):
		return "({})-({})".format(self.lhs, self.rhs)
		
	def __str__(self):
		return "({})-({})".format(self.lhs, self.rhs)
		
	def __trunc__(self):
		return Trunc(self)
		
	def conjugate(self):
		return Sub(self.lhs.conjugate(), self.rhs.conjugate())
	
	def derivative(self, to = "x"):
		return Sub(self.lhs.derivative(to), self.rhs.derivative(to))
		
	@property
	def imag(self):
		return Sub(self.lhs.imag, self.rhs.imag)
		
	@property
	def real(self):
		return Sub(self.lhs.real, self.rhs.real)
		
	def value(self, **kwargs):
		return self.lhs.value(**kwargs) - self.rhs.value(**kwargs)
