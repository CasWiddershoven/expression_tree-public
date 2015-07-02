from expr import Expr

from math import sin

class Sin(Expr):
	def __init__(self, *args, **kwargs):
		super(Sin, self).__init__(*args, **kwargs)
		
	def __repr__(self):
		return "Sin({})".format(self.expr)
		
	def __str__(self):
		return "Sin({})".format(self.expr)
	
	def derivative(self, to = "x"):
		from mul import Mul
		from cos import Cos
		return Mul(self.expr.derivative(to), Cos(self.expr))
		
	@property	
	def value(self, **kwargs):
		return sin(self.expr.value(**kwargs))
