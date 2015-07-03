from expr import Expr

class Pow(Expr):
	priority = 2
	associativity = 1
	
	def __init__(self, lhs, rhs, *args, **kwargs):
		super(Pow, self).__init__(*args, **kwargs)
		self.lhs = lhs
		self.rhs = rhs
		
	def __neg__(self):
		return Pow(self.lhs.__neg__(), self.rhs)
		
	def __repr__(self):
		if self.lhs.priority < self.priority:
			lhs = "({})".format(self.lhs)
		elif self.lhs.priority == self.priority and self.lhs.associativity == 1:
			lhs = "({})".format(self.lhs)
		elif self.lhs.priority == self.priority and self.associativity == 1:
			lhs = "({})".format(self.lhs)
		elif self.lhs.priority >= self.priority:
			lhs = "{}".format(self.lhs)
		if self.rhs.priority < self.priority:
			rhs = "({})".format(self.rhs)
		elif self.rhs.priority == self.priority and self.rhs.associativity == -1:
			rhs = "({})".format(self.rhs)
		elif self.rhs.priority == self.priority and self.associativity == -1:
			rhs = "({})".format(self.rhs)
		elif self.rhs.priority >= self.priority:
			rhs = "{}".format(self.rhs)
		return "{}^{}".format(lhs, rhs)
		
	def __str__(self):
		return self.__repr__()
	
	#TODO: Add Expr.isnumber (make it Expr.isconst(to = "x")), add other cases
	def derivative(self, to = "x"):
		if(self.rhs.isnumber()):
			from mul import Mul
			from const import Const
			return Mul(self.lhs.derivative(to), Pow(self.lhs, Sub(self.rhs, Const(1))))
			
	def imagPart(self, **kwargs):
		# a^(b+ci) = e^ln(a)^(b+ci) = a^b*e^(ln(a)*c)i = a^b*(cos(ln(a)*c)+isin(ln(a)*c))
		from mul import Mul
		from sin import Sin
		from log import Log
		if self.lhs.imagPart(**kwargs).__eq__(Const(0), **kwargs):
			return Mul(Pow(self.lhs, self.rhs.realPart(**kwargs)), Sin(Mul(Log(self.lhs), self.rhs.imagPart(**kwargs))))
		else:
			raise NotImplementedError("We haven't implemented getting the imaginary part of a power of a complex number yet.")
		
	def realPart(self):
		# a^(b+ci) = e^ln(a)^(b+ci) = a^b*e^(ln(a)*c)i = a^b*(cos(ln(a)*c)+isin(ln(a)*c))
		from mul import Mul
		from cos import Cos
		from log import Log
		if self.lhs.imagPart(**kwargs).__eq__(Const(0), **kwargs):
			return Mul(Pow(self.lhs, self.rhs.realPart(**kwargs)), Cos(Mul(Log(self.lhs), self.rhs.imagPart(**kwargs))))
		else:
			raise NotImplementedError("We haven't implemented getting the real part of a power of a complex number yet.")
		
	def value(self, **kwargs):
		return self.lhs.value(**kwargs) ** self.rhs.value(**kwargs)
