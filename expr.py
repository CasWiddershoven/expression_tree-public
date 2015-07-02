class Expr(object):
	def __init__(self, expr, *args, **kwargs):
		super(Expr, self).__init__(*args, **kwargs)
		
		self.expr = expr
		
	def __abs__(self):
		return Abs(self)
		
	def __add__(self, other):
		return Add(self, other)
		
	def __div__(self, other):
		return Div(self, other)
		
	def __divmod__(self, other):
		return Divmod(self, other)
		
	def __eq__(self, other, **kwargs):
		return self.value(**kwargs) == other.value(**kwargs)
		
	def __float__(self, **kwargs):
		return float(self.value(**kwargs))
		
	def __floordiv__(self, other):
		return Floordiv(self, other)
		
	def __ge__(self, other, **kwargs):
		return self.value(**kwargs) >= other.value(**kwargs)
		
	def __gt__(self, other, **kwargs):
		return self.value(**kwargs) > other.value(**kwargs)
		
	def __int__(self, **kwargs):
		return int(self.value(**kwargs))
		
	def __le__(self, other, **kwargs):
		return self.value(**kwargs) <= other.value(**kwargs)
		
	def __long__(self):
		return long(self.value())
		
	def __lt__(self, other):
		return self.value() < other.value()
		
	def __mod__(self, other):
		return Mod(self, other)
		
	def __mul__(self, other):
		return Mul(self, other)
		
	def __ne__(self, other, **kwargs):
		return self.value(**kwargs) != other.value(**kwargs)
		
	def __neg__(self, **kwargs):
		return Expr(str(-self.value(**kwargs)))
		
	def __nonzero__(self, **kwargs):
		return self.value(**kwargs) != 0
		
	def __pow__(self, other):
		return Pow(self, other)
		
	def __radd__(self, other):
		return Add(other, self)
		
	def __rdiv__(self, other):
		return Div(other, self)
		
	def __rdivmod__(self, other):
		return Divmod(other, self)
		
	def __repr__(self, other):
		return self.expr
		
	def __rfloordiv(self, other):
		return Floordiv(other, self)
		
	def __rmod__(self, other):
		return Mod(other, self)
		
	def __rmul__(self, other):
		return Mul(other, self)
		
	def __rpow__(self, other):
		return Pow(other, self)
		
	def __rsub__(self, other):
		return Sub(other, self)
		
	def __rtruediv__(self, other):
		return Div(other, self)
		
	def __str__(self):
		return self.expr
		
	def __sub__(self, other):
		return Sub(self, other)
		
	def __truediv__(self, other):
		return Div(self, other)
		
	def __trunc__(self):
		return Trunc(self)
		
	def as_integer_ratio(self, **kwargs):
		return self.value(**kwargs).as_integer_ratio()
		
	def conjugate(self, **kwargs):
		return Expr(str(self.value(**kwargs).conjugate()))
		
	@property
	def imag(self, **kwargs):
		return Expr(str(self.value(**kwargs).imag))
		
	def is_integer(self, **kwargs):
		return self.value(**kwargs).is_integer()
	
	@property
	def real(self, **kwargs):
		return Expr(str(self.value(**kwargs).real))
	
	def value(self, **kwargs):
		return eval(self.expr)
