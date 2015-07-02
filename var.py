class Var(Expr):
	def __init__(self, key, *args, **kwargs):
		super(Var, self).__init__(*args, **kwargs)
		
		self.key = key
