from expr import Expr
from math import floor

class Trunc(Expr):
	priority = 3
	associativity = 0
	
	def __init__(self, *args, **kwargs):
		super(Trunc, self).__init__(*args, **kwargs)
		
	def __repr__(self):
		return "|_{}_|".format(self.expr)
		
	def __str__(self):
		return "|_{}_|".format(self.expr)
		
	def __trunc__(self):
		return self
		
	def conjugate(self, **kwargs):
		return Trunc(self.expr.conjugate(**kwargs))

	def imagPart(self, **kwargs):
		return Trunc(self.expr.imagPart(**kwargs))

	def realPart(self, **kwargs):
		return Trunc(self.expr.realPart(**kwargs))
		
	def value(self, **kwargs):
		val = self.expr.value(**kwargs)
		return floor(val.real) + floor(val.imag)*1j
	
	def derivative(self, to = "x"):
		from nserror import NotSupportedError
		raise NotSupportedError("You can't take the derivative of a non-continuous function!")
