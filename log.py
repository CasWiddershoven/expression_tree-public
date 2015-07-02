from expr import Expr
from const import Const

from math import e
from math import log

class Log(Expr):
	def __init__(self, lhs, rhs = Const(e), *args, **kwargs):
		super(Log, self).__init__(*args, **kwargs)
		self.lhs = lhs
		self.rhs = rhs
		
	def __repr__(self):
		if(self.rhs.value() == 2):
			return "lg({})".format(self.lhs)
		if(self.rhs.value() == e):
			return "ln({})".format(self.lhs)
		if(self.rhs.value() == 10):
			return "log({})".format(self.lhs) 
		return "log_({})(({}))".format(self.rhs, self.lhs)
		
	def __str__(self):
		if(self.rhs.value() == 2):
			return "lg({})".format(self.lhs)
		if(self.rhs.value() == e):
			return "ln({})".format(self.lhs)
		if(self.rhs.value() == 10):
			return "log({})".format(self.lhs) 
		return "log_({})(({}))".format(self.rhs, self.lhs)
		
	def __trunc__(self):
		from trunc import Trunc
		return Trunc(self)
	
	def derivative(self, to = "x"):
		from div import Div
		if(self.rhs.value() == e):
			from mul import Mul
			return Div(self.lhs.derivative(to), self.lhs)
		return Div(Log(self.lhs), Log(self.rhs)).derivative(to)
	
	@property
	def imag(self, **kwargs):
		# WolframAlpha tells us Im(log(a+bi)) = Re(-ilog(a+bi))
		from mul import Mul
		return Mul(Const(-1j), self).real(kwargs)
		
	@property
	def real(self, **kwargs):
		# WolframAlpha tells us Re(log(a+bi)) = log(a^2+b^2)/2
		from pow import Pow
		from add import Add
		from div import Div
		if (self.rhs.imag.__eq__(Const(0), kwargs)):
			return Div(Log(Add(Pow(self.lhs.real(kwargs), Const(2)), Pow(self.lhs.imag(kwargs), Const(2)))), Const(2))
		else:
			return Div(Log(self.lhs), Log(self.rhs))
			
	def value(self, **kwargs):
		return log(self.lhs.value(**kwargs), self.rhs.value(**kwargs))
