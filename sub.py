from expr import Expr

class Sub(Expr):
	priority = 0
	associativity = -1
	
	def __init__(self, lhs, rhs, *args, **kwargs):
		super(Sub, self).__init__(*args, **kwargs)
		self.lhs = lhs
		self.rhs = rhs
		
	def __neg__(self):
		return Sub(self.rhs, self.lhs)
		
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
		return "{}-{}".format(lhs, rhs)
		
	def __str__(self):
		return self.__repr__()
		
	def conjugate(self):
		return Sub(self.lhs.conjugate(), self.rhs.conjugate())
	
	def derivative(self, to = "x"):
		return Sub(self.lhs.derivative(to), self.rhs.derivative(to))
		
	def imagPart(self, **kwargs):
		return Sub(self.lhs.imagPart(**kwargs), self.rhs.imagPart(**kwargs))
		
	def realPart(self, **kwargs):
		return Sub(self.lhs.realPart(**kwargs), self.rhs.realPart(**kwargs))
		
	def value(self, **kwargs):
		return self.lhs.value(**kwargs) - self.rhs.value(**kwargs)
