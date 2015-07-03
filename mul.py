from expr import Expr

class Mul(Expr):
	priority = 1
	associativity = 0
	
	def __init__(self, lhs, rhs, *args, **kwargs):
		super(Mul, self).__init__(*args, **kwargs)
		self.lhs = lhs
		self.rhs = rhs
		
	def __neg__(self):
		return Mul(self.lhs.__neg__(), self.rhs)
		
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
		return "{}*{}".format(lhs, rhs)
		
	def __str__(self):
		return self.__repr__()
		
	def conjugate(self):
		return Mul(self.lhs.conjugate(), self.rhs.conjugate())
		
	def derivative(self, to = "x"):
		from add import Add
		return Add(Mul(self.lhs.derivative(to), self.rhs), Mul(self.lhs, self.rhs.derivative(to)))
		
	def imagPart(self, **kwargs):
		from add import Add
		return Add(Mul(self.lhs.imagPart(**kwargs), self.rhs.realPart(**kwargs)), Mul(self.lhs.realPart(**kwargs), self.rhs.imagPart(**kwargs)))
		
	def realPart(self, **kwargs):
		from sub import Sub
		return Sub(Mul(self.lhs.realPart(**kwargs), self.rhs.realPart(**kwargs)), Mul(self.lhs.imagPart(**kwargs), self.rhs.imagPart(**kwargs)))
		
	def value(self, **kwargs):
		return self.lhs.value(**kwargs) * self.rhs.value(**kwargs)
