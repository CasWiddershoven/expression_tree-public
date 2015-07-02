from expr import Expr
from const import Const

class Root(Expr):
	def __init__(self, lhs, rhs = Const(2), *args, **kwargs):
		super(Root, self).__init__(*args, **kwargs)
		self.lhs = lhs
		self.rhs = rhs
		
	def __repr__(self):
		if(rhs.value() == 2):
			return "sqrt({})".format(lhs)
		else:
			return "root_({})(({}))".format(rhs, lhs)
		
	def __str__(self):
		if(rhs.value() == 2):
			return "sqrt({})".format(lhs)
		else:
			return "root_({})(({}))".format(rhs, lhs)
		
	def conjugate(self):
		from mul import Mul
		return Mul(self.lhs.conjugate(), self.rhs.conjugate())
		
	def derivative(self, to = "x"):
		from pow import Pow
		from div import Div
		from const import Const
		return Pow(self.lhs, Div(Const(1), self.rhs)).derivative()
	
	
	#not yet done
	@property
	def imag(self):
		from mul import Mul
		return Mul(self.lhs.imag, self.rhs.imag)
		
	@property
	def real(self):
		from mul import Mul
		return Mul(self.lhs.real, self.rhs.real)
	#------------------------------
	def value(self, **kwargs):
		return self.lhs.value(**kwargs) ** (1 / self.rhs.value(**kwargs))
