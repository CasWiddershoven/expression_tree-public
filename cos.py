from expr import Expr

from cmath import cos # Support complex numbers

class Cos(Expr):
	priority = 3
	associativity = 0
	
	def __init__(self, *args, **kwargs):
		super(Cos, self).__init__(*args, **kwargs)
		
	def __repr__(self):
		return "Cos({})".format(self.expr)
		
	def __str__(self):
		return "Cos({})".format(self.expr)
		
	@property
	def imag(self, **kwargs):
		# cos(a+bi) = cos(a)cosh(b)-isin(a)sinh(b) where cosh = exp(x)+exp(-x)/2 and sinh = exp(x)-exp(-x)/2
		from sin import Sin
		from sub import Sub
		from mul import Mul
		from pow import Pow
		from const import Const
		
		from math import e
		return Mul(Sin(self.expr.real), Div(Sub(Pow(Const(e), self.expr.imag), Pow(Const(e), -self.expr.imag)), Const(2)))
		
	@property
	def real(self, **kwargs):
		# cos(a+bi) = cos(a)cosh(b)-isin(a)sinh(b) where cosh = exp(x)+exp(-x)/2 and sinh = exp(x)-exp(-x)/2
		from add import Add
		from mul import Mul
		from pow import Pow
		from const import Const
		
		from math import e
		return Mul(Cos(self.expr.real), Div(Add(Pow(Const(e), self.expr.imag), Pow(Const(e), -self.expr.imag)), Const(2)))
	
	def value(self, **kwargs):
		return cos(self.expr.value(**kwargs))
	
	def derivative(self, to = "x"):
		from const import Const
		from mul import Mul
		from sin import Sin
		return Mul(Mul(Const(-1), self.expr.derivative(to)), Sin(self.expr).__neg__())
