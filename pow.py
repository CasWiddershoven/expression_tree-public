from expr import Expr

class Pow(Expr):
	def __init__(self, lhs, rhs, *args, **kwargs):
		super(Pow, self).__init__(*args, **kwargs)
		self.lhs = lhs
		self.rhs = rhs
		
	def __neg__(self):
		return Pow(self.lhs.__neg__(), self.rhs)
		
	def __repr__(self):
		return "({})^({})".format(self.lhs, self.rhs)
		
	def __str__(self):
		return "({})^({})".format(self.lhs, self.rhs)
	
	#TODO: Add Expr.isnumber (make it Expr.isconst(to = "x")), add other cases
	def derivative(self, to = "x"):
		if(self.rhs.isnumber()):
			from mul import Mul
			from const import Const
			return Mul(self.lhs.derivative(to), Pow(self.lhs, Sub(self.rhs, Const(1))))
			
	@property
	def imag(self, **kwargs):
		# a^(b+ci) = e^ln(a)^(b+ci) = a^b*e^(ln(a)*c)i = a^b*(cos(ln(a)*c)+isin(ln(a)*c))
		from mul import Mul
		from sin import Sin
		from log import Log
		if self.lhs.imag(kwargs).__eq__(Const(0), kwargs):
			return Mul(Pow(self.lhs, self.rhs.real(kwargs)), Sin(Mul(Log(self.lhs), self.rhs.imag(kwargs))))
		else:
			raise NotImplementedError("We haven't implemented getting the imaginary part of a power of a complex number yet.")
		
	@property
	def real(self):
		# a^(b+ci) = e^ln(a)^(b+ci) = a^b*e^(ln(a)*c)i = a^b*(cos(ln(a)*c)+isin(ln(a)*c))
		from mul import Mul
		from cos import Cos
		from log import Log
		if self.lhs.imag(kwargs).__eq__(Const(0), kwargs):
			return Mul(Pow(self.lhs, self.rhs.real(kwargs)), Cos(Mul(Log(self.lhs), self.rhs.imag(kwargs))))
		else:
			raise NotImplementedError("We haven't implemented getting the real part of a power of a complex number yet.")
		
	def value(self, **kwargs):
		return self.lhs.value(**kwargs) ** self.rhs.value(**kwargs)
