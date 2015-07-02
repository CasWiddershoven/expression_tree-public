from expr import Expr

from math import cos

class Cos(Expr):
	def __init__(self, *args, **kwargs):
		super(Cos, self).__init__(*args, **kwargs)
		
	def __repr__(self):
		return "Cos({})".format(self.expr)
		
	def __str__(self):
		return "Cos({})".format(self.expr)
	
	def derivative(self, to = "x"):
		from const import Const
		from mul import Mul
		from sin import Sin
		return Mul(Mul(Const(-1), self.expr.derivative(to)), Sin(self.expr).__neg__())
		
	@property	
	def value(self, **kwargs):
		return cos(self.expr.value(**kwargs))
