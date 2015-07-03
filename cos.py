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
		
	def imagPart(self, **kwargs):
		# cos(a+bi) = cos(a)cosh(b)-isin(a)sinh(b) where cosh = exp(x)+exp(-x)/2 and sinh = exp(x)-exp(-x)/2
		from sin import Sin
		from sub import Sub
		from mul import Mul
		from pow import Pow
		from div import Div
		from const import Const
		
		from math import e
		return Mul(Sin(self.expr.realPart(**kwargs)), Div(Sub(Pow(Const(e), self.expr.imagPart(**kwargs)), Pow(Const(e), -self.expr.imagPart(**kwargs))), Const(2)))
		
	def realPart(self, **kwargs):
		# cos(a+bi) = cos(a)cosh(b)-isin(a)sinh(b) where cosh = exp(x)+exp(-x)/2 and sinh = exp(x)-exp(-x)/2
		from add import Add
		from div import Div
		from mul import Mul
		from pow import Pow
		from const import Const
		
		from math import e
		return Mul(Cos(self.expr.realPart(**kwargs)), Div(Add(Pow(Const(e), self.expr.imagPart(**kwargs)), Pow(Const(e), -self.expr.imagPart(**kwargs))), Const(2)))
	
	def value(self, **kwargs):
		return cos(self.expr.value(**kwargs))
	
	def derivative(self, to = "x"):
		from const import Const
		from mul import Mul
		from sin import Sin
		return Mul(self.expr.derivative(to), -Sin(self.expr))
