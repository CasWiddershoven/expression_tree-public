from math import e

class Log(Expr):
	def __init__(self, lhs, rhs = Const(math.e), *args, **kwargs):
		super(Root, self).__init__(*args, **kwargs)
		self.lhs = lhs
		self.rhs = rhs
		
	def __neg__(self):
		return Mul(const(-1), self)
		
	def __repr__(self):
		if(rhs.value() == 2):
			return "lg({})".format(lhs)
		if(rhs.value() == math.e):
			return "ln({})".format(lhs)
		if(rhs.value() == 10):
			return "log({})".format(lhs) 
		return "log_({})(({}))".format(rhs, lhs)
		
	def __str__(self):
		if(rhs.value() == 2):
			return "lg({})".format(lhs)
		if(rhs.value() == math.e):
			return "ln({})".format(lhs)
		if(rhs.value() == 10):
			return "log({})".format(lhs) 
		return "log_({})(({}))".format(rhs, lhs)
		
	def __trunc__(self):
		return Trunc(self)
	
	##what the fiesh?
	def conjugate(self):
		return Mul(self.lhs.conjugate(), self.rhs.conjugate())
	
	
	def derivative(self, to = "x"):
		if(this.rhs.value() == math.e):
			return Mul(this.lhs.derivative(to), Div(Const(1), this.rhs))
		return Div(Log(this.lhs, math.e), Log(this.rhs, math.e)).derivative(to)
	
	
	#not yet done
	@property
	def imag(self):
		return Mul(self.lhs.imag, self.rhs.imag)
		
	@property
	def real(self):
		return Mul(self.lhs.real, self.rhs.real)
	#------------------------------
	def value(self, **kwargs):
		return self.lhs.value(**kwargs) ** (1 / self.rhs.value(**kwargs))
