from expr import Expr

class Abs(Expr):
	""" The Absolute function: Abs: C -> R, |a+bi| = sqrt(a^2+b^2) """
	def __init__(self, *args, **kwargs):
		super(Abs, self).__init__(*args, **kwargs)
		
	def __eq__(self, other, **kwargs):
		return self.expr == other.expr or -self.expr == other.expr
		
	def __lt__(self, other, **kwargs):
		return (self.expr.__gt__(Const(0), kwargs) and self.expr.__lt__(other, kwargs))
				or (self.expr.__lt__(Const(0), kwargs) and -self.expr.__lt__(other, kwargs))
				
	def __nonzero__(self, **kwargs):
		return self.expr.__nonzero__(kwargs)
		
	def __repr__(self):
		return "|({})|".format(self.expr)
		
	def __str__(self):
		return "|({})|".format(self.expr)
		
	def conjugate(self):
		return self
		
	@property
	def imag(self, **kwargs):
		# |a+b*i| = sqrt(a^2+b^2), so imag(sqrt(a^2+b^2)) = 0
		from const import Const
		return Const(0)
		
	@property
	def real(self, **kwargs):
		return self.value(**kwargs)
			
	def value(self, **kwargs):
		return abs(self.expr.value(**kwargs))
	
	def derivative(self, to = "x"):
		# |f(x)|' = f(x)f'(x)/|f(x)|
		from mul import Mul
		from div import Div
		return Div(Mul(self.expr, self.expr.derivative(to)), self)
