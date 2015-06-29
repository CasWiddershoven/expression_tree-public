class Add(Expr):
	def __init__(self, lhs, rhs, *args, **kwargs):
		super(Add, self).__init__(*args, **kwargs
		self.lhs = lhs
		self.rhs = rhs
		
	def __neg__(self):
		return Sub(lhs.__neg__(), rhs)
		
	def __repr__(self):
		return "({})+({})".format(lhs, rhs)
		
	def __str__(self):
		return "({})+({})".format(lhs, rhs)
		
	def __trunc__(self):
		return Trunc(self)
		
	def conjugate(self):
		return Add(self.lhs.conjugate(), self.rhs.conjugate())
		
	@property
	def imag(self):
		return Add(self.lhs.imag, self.rhs.imag)
		
	@property
	def real(self):
		return Add(self.lhs.real, self.rhs.real)
		
	def value(self):
		return self.lhs.value() + self.rhs.value()
