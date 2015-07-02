class Abs(Expr):
	def __init__(self, *args, **kwargs):
		super(Abs, self).__init__(*args, **kwargs)
		
	@property	
	def value(self):
		return abs(self.expr.value())
