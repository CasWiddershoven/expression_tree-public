from math import sin

class Sin(Expr):
	def __init__(self, *args, **kwargs):
		super(Sin, self).__init__(*args, **kwargs)
		
	def __repr__(self):
		return "Sin({})".format(self.expr)
		
	def __str__(self):
		return "Sin({})".format(self.expr)
	
	def __trunc__(self):
		return Trunc(self)
	
	def derivative(self, to = "x"):
		return mul(self.expr.derivative(to), Cos(self.expr))
		
	@property	
	def value(self, **kwargs):
		return sin(self.expr.value(**kwargs))
