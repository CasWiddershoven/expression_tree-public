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
		
	@property	
	def value(self):
		return sin(self.expr.value())
