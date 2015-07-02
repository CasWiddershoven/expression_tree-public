from expr import Expr

class Abs(Expr):
	def __init__(self, *args, **kwargs):
		super(Abs, self).__init__(*args, **kwargs)
		
	def __repr__(self):
		return "|({})|".format(self.expr)
		
	def __str__(self):
		return "|({})|".format(self.expr)
	
	def derivative(self, to = "x"):
		return Abs(self.expr.derivative(to))
		
	@property
	def imag(self):
		from root import Root
		from pow import Pow
		from add import Add
		from const import Const
		return Root(Add(Pow(self.expr.imag(),Const(2)),(Pow(self.expr.real()),Const(2))))
		
	@property
	def real(self):
		return imag(self)
		
	@property	
	def value(self, **kwargs):
		return abs(self.expr.value(**kwargs))
