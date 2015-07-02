class Abs(Expr):
	def __init__(self, *args, **kwargs):
		super(Abs, self).__init__(*args, **kwargs)
		
	def __repr__(self):
		return "|({})|".format(self.expr)
		
	def __str__(self):
		return "|({})|".format(self.expr)
	
	def __trunc__(self):
		return Trunc(self)
		
	@property	
	def value(self):
		return abs(self.expr.value())
