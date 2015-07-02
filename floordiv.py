from expr import Expr

class FloorDiv(Expr):
	def __init__(self, lhs, rhs, *args, **kwargs):
		super(FloorDiv, self).__init__(*args, **kwargs)
		self.lhs = lhs
		self.rhs = rhs
		
	def __neg__(self):
		return FloorDiv(self.lhs.__neg__(), self.rhs)
		
	def __repr__(self):
		return "|_({})/({})_|".format(self.lhs, self.rhs)
		
	def __str__(self):
		return "|_({})/({})_|".format(self.lhs, self.rhs)
		
	def __trunc__(self):
		return self
		
	def conjugate(self):
		return FloorDiv(self.lhs.conjugate(), self.rhs.conjugate())

	@property
	def imag(self, **kwargs):
		from div import Div
		from trunc import Trunc
		return Trunc(Div(self.lhs, self.rhs).imag(kwargs))

	@property
	def real(self, **kwargs):
		from div import Div
		from trunc import Trunc
		return Trunc(Div(self.lhs, self.rhs).real(kwargs))
		
	def value(self):
		from trunc import Trunc
		from div import Div
		return Trunc(Div(self.lhs, self.rhs)).value()
	
	def derivative(self, to = "x"):
		from nserror import NotSupportedError
		raise NotSupportedError("You can't take the derivative of a non-continuous function!")
