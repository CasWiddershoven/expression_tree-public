from expr import Expr

from math import sin

class Sin(Expr):
	def __init__(self, *args, **kwargs):
		super(Sin, self).__init__(*args, **kwargs)
		
	def __repr__(self):
		return "Sin({})".format(self.expr)
		
	def __str__(self):
		return "Sin({})".format(self.expr)
		
	@property
	def imag(self, **kwargs):
		# sin(a+bi) = sin(a)cosh(b)-icos(a)sinh(b) where cosh = exp(x)+exp(-x)/2 and sinh = exp(x)-exp(-x)/2
		from cos import Cos
		from sub import Sub
		from mul import Mul
		from pow import Pow
		from const import Const
		
		from math import e
		return Mul(Cos(self.expr.real), Div(Sub(Pow(Const(e), self.expr.imag), Pow(Const(e), -self.expr.imag)), Const(2)))
		
	@property
	def real(self, **kwargs):
		# sin(a+bi) = sin(a)cosh(b)-icos(a)sinh(b) where cosh = exp(x)+exp(-x)/2 and sinh = exp(x)-exp(-x)/2
		from add import Add
		from sin import Sin
		from mul import Mul
		from pow import Pow
		from const import Const
		
		from math import e
		return Mul(Sin(self.expr.real), Div(Add(Pow(Const(e), self.expr.imag), Pow(Const(e), -self.expr.imag)), Const(2)))
		
	@property	
	def value(self, **kwargs):
		return sin(self.expr.value(**kwargs))
	
	def derivative(self, to = "x"):
		from mul import Mul
		from cos import Cos
		return Mul(self.expr.derivative(to), Cos(self.expr))
