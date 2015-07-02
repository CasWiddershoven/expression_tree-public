class Abs(Expr):
	def __init__(self, *args, **kwargs):
		super(Abs, self).__init__(*args, **kwargs)
		
	def __repr__(self):
		return "|({})|".format(self.expr)
		
	def __str__(self):
		return "|({})|".format(self.expr)
	
	def __trunc__(self):
		return Trunc(self)
	
	def derivative(self):
		return Abs(self.expr.derivative())
		
	@property
	def imag(self):
		return Sqrt(Add(Pow(self.expr.imag(),Const(2)),(Pow(self.expr.real()),Const(2))))
		
	@property
	def real(self):
		return imag(self)
		
	@property	
	def value(self, **kwargs):
		return abs(self.expr.value(**kwargs))
