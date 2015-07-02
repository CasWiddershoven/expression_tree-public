class FloorDiv(Expr):
	def __init__(self, lhs, rhs, *args, **kwargs):
		super(FloorDiv, self).__init__(*args, **kwargs)
		self.lhs = lhs
		self.rhs = rhs
		
	def __neg__(self):
		return FloorDiv(self.lhs.__neg__(), self.rhs)
		
	def __repr__(self):
		return "|_({})/({})_|".format(lhs, rhs)
		
	def __str__(self):
		return "|_({})/({})_|".format(lhs, rhs)
		
	def __trunc__(self):
		return self
		
	def conjugate(self):
		return FloorDiv(self.lhs.conjugate(), self.rhs.conjugate())
		

	@property
	def real(self):
		return Add(self.lhs, self.rhs)
		
	def value(self, **kwargs):
		return Floor(Div(self.lhs, self.rhs)).value(**kwargs)
