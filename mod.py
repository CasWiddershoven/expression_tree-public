from expr import Expr

class Mod(Expr):
	priority = 3
	associativity = 1
	
	def __init__(self, lhs, rhs, *args, **kwargs):
		super(Mod, self).__init__(*args, **kwargs)
		self.lhs = lhs
		self.rhs = rhs
		
	def __neg__(self):
		return Mod(self.lhs.__neg__(), self.rhs)
		
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
		return "{}%{}".format(lhs, rhs)
		
	def __str__(self):
		return self.__repr__()
		
	def __trunc__(self):
		return self
		
	def conjugate(self):
		# Complex numbers don't support modulo, so we'll just assume both lhs and rhs are real.
		return self
		
	def imagPart(self, **kwargs):
		from nserror import NotSupportedError
		raise NotSupportedError("Complex numbers don't support modulo")
		
	def realPart(self, **kwargs):
		return Mod(self.lhs.realPart(**kwargs), self.rhs.realPart(**kwargs))
		
	def value(self, **kwargs):
		return self.lhs.value(**kwargs) % self.rhs.value(**kwargs)
