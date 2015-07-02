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
		
	@property	
	def value(self):
		return  cos(self.expr.value())
