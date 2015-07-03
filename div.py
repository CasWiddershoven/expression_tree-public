from expr import Expr

class Div(Expr):
	priority = 1
	associativity = -1
	
	def __init__(self, lhs, rhs, *args, **kwargs):
		super(Div, self).__init__(*args, **kwargs)
		self.lhs = lhs
		self.rhs = rhs
		
	def __neg__(self):
		return Div(self.lhs.__neg__(), self.rhs)
		
	def __eq__(self, other, **kwargs):
		from const import Const
		from numbers import Number
		if not isinstance(other, Expr):
			if isinstance(other, str):
				other = Const(eval(other))
			elif isinstance(other, Number):
				other = Const(other)
				
		return self.lhs.__eq__(Mul(self.rhs, other), **kwargs)
		
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
		return "{}/{}".format(lhs, rhs)
		
	def __str__(self):
		return self.__repr__()
		
	def conjugate(self):
		return Div(self.lhs.conjugate(), self.rhs.conjugate())
		
	def derivative(self, to = "x"):
		from sub import Sub
		from mul import Mul
		from pow import Pow
		from const import Const
		return Div(Sub(Mul(self.lhs.derivative(to), self.rhs), Mul(self.rhs.derivative(to), self.lhs)), Pow(self.rhs, Const(2)))
		
	def imagPart(self, **kwargs):
		#(a+bi)/(c+di) = (ac+bd)/(c^2+d^2) + (bc-ad)i/(c^2+d^2)
		from div import Div
		from sub import Sub
		from mul import Mul
		from pow import Pow
		from add import Add
		from const import Const
		return Div(
					Sub(
							Mul(self.lhs.imagPart(**kwargs), self.rhs.realPart(**kwargs)), 
							Mul(self.lhs.realPart(**kwargs), self.rhs.imagPart(**kwargs))), 
					Add(
							Pow(self.rhs.realPart(**kwargs), Const(2)), 
							Pow(self.rhs.imagPart(**kwargs), Const(2))))
		
	def realPart(self, **kwargs):
		#(a+bi)/(c+di) = (ac+bd)/(c^2+d^2) + (bc-ad)i/(c^2+d^2)
		from div import Div
		from mul import Mul
		from pow import Pow
		from add import Add
		from const import Const
		return Div(
					Add(
							Mul(self.lhs.realPart(**kwargs), self.rhs.realPart(**kwargs)), 
							Mul(self.lhs.imagPart(**kwargs), self.rhs.imagPart(**kwargs))), 
					Add(
							Pow(self.rhs.realPart(**kwargs), Const(2)), 
							Pow(self.rhs.imagPart(**kwargs), Const(2))))
		
	def value(self, **kwargs):
		return self.lhs.value(**kwargs) / self.rhs.value(**kwargs)
