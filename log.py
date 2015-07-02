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
	
	##what the fiesh?
	def conjugate(self):
		from mul import Mul
		return Mul(self.lhs.conjugate(), self.rhs.conjugate())
	
	
	def derivative(self, to = "x"):
		from div import Div
		if(self.rhs.value() == e):
			from mul import Mul
			return Div(self.lhs.derivative(to), self.lhs)
		return Div(Log(self.lhs), Log(self.rhs)).derivative(to)
	
	
	#not yet done
	@property
	def imag(self):
		from mul import Mul
		return Mul(self.lhs.imag, self.rhs.imag)
		
	@property
	def real(self):
		from mul import Mul
		return Mul(self.lhs.real, self.rhs.real)
	#------------------------------
	def value(self, **kwargs):
		return log(self.lhs.value(**kwargs), self.rhs.value(**kwargs))
