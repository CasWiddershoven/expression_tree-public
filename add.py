from expr import Expr

class Add(Expr):
	""" Addition: Add: CxC -> C, (a + bi) + (a' + b'i) = a + a' + (b + b')i """
	priority = 0
	associativity = 0
	
	def __init__(self, lhs, rhs, *args, **kwargs):
		super(Add, self).__init__(*args, **kwargs)
		self.lhs = lhs
		self.rhs = rhs
		
	def __neg__(self):
		from sub import Sub
		return Sub(self.lhs.__neg__(), self.rhs)
		
	def __nonzero__(self, **kwargs):
		from mul import Mul
		from const import Const
		return (Mul(self.lhs, self.rhs).__gt__(Const(0), **kwargs) or
					self.lhs.__ne__(-self.rhs, **kwargs) or 
					(self.lhs.__nonzero__(**kwargs) != self.rhs.__nonzero__(**kwargs)))
		
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
		return "{}+{}".format(lhs, rhs)
		
	def __str__(self):
		return self.__repr__()
		
	def conjugate(self):
		return Add(self.lhs.conjugate(), self.rhs.conjugate())
		
	def imagPart(self, **kwargs):
		return Add(self.lhs.imagPart(**kwargs), self.rhs.imagPart(**kwargs))
		
	def realPart(self, **kwargs):
		return Add(self.lhs.realPart(**kwargs), self.rhs.realPart(**kwargs))
		
	def value(self, **kwargs):
		return self.lhs.value(**kwargs) + self.rhs.value(**kwargs)
		
	def derivative(self, to = "x"):
		return Add(self.lhs.derivative(to), self.rhs.derivative(to))
