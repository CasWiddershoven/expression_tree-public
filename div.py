from expr import Expr

class Div(Expr):
	def __init__(self, lhs, rhs, *args, **kwargs):
		super(Div, self).__init__(*args, **kwargs)
		self.lhs = lhs
		self.rhs = rhs
		
	def __neg__(self):
		return Div(self.lhs.__neg__(), self.rhs)
		
	def __eq__(self, other, **kwargs):
		return self.lhs.__eq__(Mul(self.rhs, other), kwargs)
		
	def __repr__(self):
		return "({})/({})".format(self.lhs, self.rhs)
		
	def __str__(self):
		return "({})/({})".format(self.lhs, self.rhs)
		
	def conjugate(self):
		return Div(self.lhs.conjugate(), self.rhs.conjugate())
		
	def derivative(self, to = "x"):
		from sub import Sub
		from mul import Mul
		from pow import Pow
		return Div(Sub(Mul(self.lhs.derivative(to), self.rhs), Mul(self.rhs.derivative(to), self.lhs)), Pow(self.rhs, Const(2)))
		
	@property
	def imag(self):
		#(a+bi)/(c+di) = (ac+bd)/(c^2+d^2) + (bc-ad)i/(c^2+d^2)
		from div import Div
		from sub import Sub
		from mul import Mul
		from pow import Pow
		from add import Add
		return Div(Sub(Mul(self.lhs.imag, self.rhs.real), Mul(self.lhs.real, self.rhs.imag)), Add(Pow(self.lhs.real, Const(2)), Pow(self.lhs.imag, Const(2))))
		
	@property
	def real(self):
		#(a+bi)/(c+di) = (ac+bd)/(c^2+d^2) + (bc-ad)i/(c^2+d^2)
		from div import Div
		from mul import Mul
		from pow import Pow
		from add import Add
		return Div(Add(Mul(self.lhs.real, self.rhs.real), Mul(self.lhs.imag, self.rhs.imag)), Add(Pow(self.lhs.real, Const(2)), Pow(self.lhs.imag, Const(2))))
		
	def value(self, **kwargs):
		return self.lhs.value(**kwargs) / self.rhs.value(**kwargs)
