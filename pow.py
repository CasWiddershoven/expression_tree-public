class Pow(Expr):
	def __init__(self, lhs, rhs, *args, **kwargs):
		super(Pow, self).__init__(*args, **kwargs)
		self.lhs = lhs
		self.rhs = rhs
		
	def __neg__(self):
		return Pow(self.lhs.__neg__(), self.rhs)
		
	def __repr__(self):
		return "({})^({})".format(lhs, rhs)
		
	def __str__(self):
		return "({})^({})".format(lhs, rhs)
		
	def __trunc__(self):
		return Trunc(self)
		
	def conjugate(self):
		return Pow(self.lhs.conjugate(), self.rhs.conjugate())
	
	def derivative(self):
		if(self.lhs.isnumber()):
			if(!self.rhs.isnumber()):
		
		if(self.rhs.isnumber()):
			return Mul(self.lhs.derivative(), Pow(self.lhs, Sub(self.rhs, Const(1))))
				
		
	@property
	def imag(self):
		return Pow(self.lhs.imag, self.rhs.imag)
		
	@property
	def real(self):
		return Pow(self.lhs.real, self.rhs.real)
		
	def value(self, **kwargs):
		return self.lhs.value(**kwargs) ** self.rhs.value(**kwargs)
