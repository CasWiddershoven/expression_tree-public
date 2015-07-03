from expr import Expr
from const import Const

class Root(Expr):
	priority = 2
	associativity = 0
	
	def __init__(self, lhs, rhs = Const(2), *args, **kwargs):
		super(Root, self).__init__(*args, **kwargs)
		self.lhs = lhs
		self.rhs = rhs
		
	def __repr__(self):
		if(self.rhs.value() == 2):
			return "sqrt({})".format(self.lhs)
		else:
			return "root_({})({})".format(self.rhs, self.lhs)
		
	def __str__(self):
		return self.__repr__()
		
	def derivative(self, to = "x"):
		from pow import Pow
		from div import Div
		from const import Const
		return Pow(self.lhs, Div(Const(1), self.rhs)).derivative()
	
	# Done simply, but ugly (and probably terribly slow)
	def imagPart(self, **kwargs):
		from pow import Pow
		from const import Const
		from div import Div
		return Pow(self.lhs, Div(Const(1), self.rhs)).imagPart(**kwargs)
		
	def realPart(self):
		from pow import Pow
		from const import Const
		from div import Div
		return Pow(self.lhs, Div(Const(1), self.rhs)).realPart(**kwargs)
		
	def value(self, **kwargs):
		return self.lhs.value(**kwargs) ** (1 / self.rhs.value(**kwargs))
