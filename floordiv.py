from expr import Expr

class FloorDiv(Expr):
	priority = 3
	associativity = 0
	
	def __init__(self, lhs, rhs, *args, **kwargs):
		super(FloorDiv, self).__init__(*args, **kwargs)
		self.lhs = lhs
		self.rhs = rhs
		
	def __repr__(self):
		from div import Div
		if self.lhs.priority < Div.priority:
			lhs = "({})".format(self.lhs)
		elif self.lhs.priority == Div.priority and self.lhs.associativity == 1:
			lhs = "({})".format(self.lhs)
		elif self.lhs.priority == self.priority and self.associativity == 1:
			lhs = "({})".format(self.lhs)
		elif self.lhs.priority >= Div.priority:
			lhs = "{}".format(self.lhs)
		if self.rhs.priority < Div.priority:
			rhs = "({})".format(self.rhs)
		elif self.rhs.priority == Div.priority and self.rhs.associativity == -1:
			rhs = "({})".format(self.rhs)
		elif self.rhs.priority == self.priority and self.associativity == -1:
			rhs = "({})".format(self.rhs)
		elif self.rhs.priority >= self.priority:
			rhs = "{}".format(self.rhs)
		return "|_{}/{}_|".format(self.lhs, self.rhs)
		
	def __str__(self):
		return self.__repr__()
		
	def __trunc__(self):
		return self

	def imagPart(self, **kwargs):
		from div import Div
		from trunc import Trunc
		return Trunc(Div(self.lhs, self.rhs).imagPart(**kwargs))

	def realPart(self, **kwargs):
		from div import Div
		from trunc import Trunc
		return Trunc(Div(self.lhs, self.rhs).realPart(**kwargs))
		
	def value(self):
		from trunc import Trunc
		from div import Div
		return Trunc(Div(self.lhs, self.rhs)).value()
	
	def derivative(self, to = "x"):
		from nserror import NotSupportedError
		raise NotSupportedError("You can't take the derivative of a non-continuous function!")
