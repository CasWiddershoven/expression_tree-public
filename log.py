from expr import Expr
from const import Const

from math import e
from cmath import log

class Log(Expr):
	priority = 3
	associativity = 0
	
	def __init__(self, lhs, rhs = Const(e), *args, **kwargs):
		super(Log, self).__init__(*args, **kwargs)
		self.lhs = lhs
		self.rhs = rhs
		
	def __repr__(self):
		try:
			if(self.rhs.value() == 2):
				return "lg({})".format(self.lhs)
			if(self.rhs.value() == e):
				return "ln({})".format(self.lhs)
			if(self.rhs.value() == 10):
				return "log({})".format(self.lhs) 
		except UnboundLocalError:
			pass
		return "log_({})({})".format(self.rhs, self.lhs)
		
	def __str__(self):
		return self.__repr__()
		
	def __trunc__(self):
		from trunc import Trunc
		return Trunc(self)
	
	def derivative(self, to = "x"):
		from div import Div
		try:
			if(self.rhs.value() == e):
				from mul import Mul
				return Div(self.lhs.derivative(to), self.lhs)
		except UnboundLocalError:
			pass
		return Div(Log(self.lhs), Log(self.rhs)).derivative(to)
	
	def imagPart(self, **kwargs):
		from div import Div
		from sub import Sub
		return Div(Sub(self, self.realPart(**kwargs)), Const(1j))
		
	def realPart(self, **kwargs):
		# WolframAlpha tells us Re(log(a+bi)) = log(a^2+b^2)/2
		from pow import Pow
		from add import Add
		from div import Div
		if (self.rhs.imagPart(**kwargs).__eq__(Const(0), **kwargs)):
			return Div(Log(Add(Pow(self.lhs.realPart(**kwargs), Const(2)), Pow(self.lhs.imagPart(**kwargs), Const(2)))), Const(2))
		else:
			return Div(Log(self.lhs), Log(self.rhs)).realPart(**kwargs)
			
	def value(self, **kwargs):
		return log(self.lhs.value(**kwargs), self.rhs.value(**kwargs))
