class Const(Expr):
	def __init__(self, val, *args, **kwargs):
		super(Const, self).__init__(*args, **kwargs)
		
		self.val = val
		
	@property
	def imag(self):
		return self.val.imag
		
	@property
	def real(self):
		return self.val.real
		
	def value(self):
		return self.val
