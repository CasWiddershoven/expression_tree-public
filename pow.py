from expr import Expr

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
		
	def conjugate(self):
		return Pow(self.lhs.conjugate(), self.rhs.conjugate())
	
	#TODO: Add Expr.isnumber (make it Expr.isconst(to = "x")), add other cases
	def derivative(self, to = "x"):
		if(self.rhs.isnumber()):
			from mul import Mul
			from const import Const
			return Mul(self.lhs.derivative(to), Pow(self.lhs, Sub(self.rhs, Const(1))))
			
	@property
	def imag(self):
		return Pow(self.lhs.imag, self.rhs.imag)
		
	@property
	def real(self):
		return Pow(self.lhs.real, self.rhs.real)
		
	def value(self, **kwargs):
		return self.lhs.value(**kwargs) ** self.rhs.value(**kwargs)
