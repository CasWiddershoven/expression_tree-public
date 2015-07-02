from math import cos

class Cos(Expr):
	def __init__(self, *args, **kwargs):
		super(Cos, self).__init__(*args, **kwargs)
		
	def __repr__(self):
		return "Cos({})".format(self.expr)
		
	def __str__(self):
		return "Cos({})".format(self.expr)
	
	def __trunc__(self):
		return Trunc(self)
		
	def derivative(self, to = "x"):
		return Mul(Mul(Const(-1), self.expr.derivative(to)), Sin(self.expr)__neg__())
		
	@property	
	def value(self):
		return  cos(self.expr.value())
