from expr import Expr

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
		from trunc import Trunc
		return Trunc(Div(self.lhs, self.rhs).conjugate())
	
	#TODO: is the derivative of FloorDiv the floor of the derivative of the div?
	def derivative(self, to = "x"):
		from trunc import Trunc
		from div import Div
		return Trunc(Div(self.lhs, self.rhs).derivative(to))

	#TODO: This can't be right, either. Also, imag is missing.
	@property
	def real(self):
		from add import Add
		return Add(self.lhs, self.rhs)
		
	def value(self):
		from trunc import Trunc
		from div import Div
		return Trunc(Div(self.lhs, self.rhs)).value()
