#['__abs__', '__add__', '__div__', '__divmod__', '__eq__', '__float__', '__floordiv__', '__ge__', '__gt__', '__int__', '__le__', '__long__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__nonzero__', '__pow__', '__radd__', '__rdiv__', '__rdivmod__', '__repr__', '__rfloordiv__', '__rmod__', '__rmul__', '__rpow__', '__rsub__', '__rtruediv__', '__str__', '__sub__', '__truediv__', '__trunc__', 'as_integer_ratio', 'conjugate', 'imag', 'is_integer', 'real']

class Expr(object):
	priority = -1
	associativity = 0
	
	def __init__(self, expr="", *args, **kwargs):
		super(Expr, self).__init__(*args, **kwargs)
		from const import Const
		from numbers import Number
		
		if isinstance(expr, Expr):
			self.expr = expr
		elif isinstance(expr, str):
			try:
				self.expr = Const(eval(expr))
			except SyntaxError:
				pass
		elif isinstance(expr, Number):
			self.expr = Const(expr)
		
	def __abs__(self):
		from abs import Abs
		return Abs(self)
		
	def __add__(self, other):
		from const import Const
		from numbers import Number
		if not isinstance(other, Expr):
			if isinstance(other, str):
				other = Const(eval(other))
			elif isinstance(other, Number):
				other = Const(other)
		from add import Add
		return Add(self, other)
		
	def __div__(self, other):
		from const import Const
		from numbers import Number
		if not isinstance(other, Expr):
			if isinstance(other, str):
				other = Const(eval(other))
			elif isinstance(other, Number):
				other = Const(other)
		from div import Div
		return Div(self, other)
		
	def __divmod__(self, other):
		from const import Const
		from numbers import Number
		if not isinstance(other, Expr):
			if isinstance(other, str):
				other = Const(eval(other))
			elif isinstance(other, Number):
				other = Const(other)
		from divmod import Divmod
		return Divmod(self, other)
		
	def __eq__(self, other, **kwargs):
		from const import Const
		from numbers import Number
		if not isinstance(other, Expr):
			if isinstance(other, str):
				other = Const(eval(other))
			elif isinstance(other, Number):
				other = Const(other)
		return (self.value(**kwargs) == other.value(**kwargs))
		
	def __float__(self, **kwargs):
		return float(self.value(**kwargs))
		
	def __floordiv__(self, other):
		from const import Const
		from numbers import Number
		if not isinstance(other, Expr):
			if isinstance(other, str):
				other = Const(eval(other))
			elif isinstance(other, Number):
				other = Const(other)
		from floordiv import FloorDiv
		return FloorDiv(self, other)
		
	def __ge__(self, other, **kwargs):
		from const import Const
		from numbers import Number
		if not isinstance(other, Expr):
			if isinstance(other, str):
				other = Const(eval(other))
			elif isinstance(other, Number):
				other = Const(other)
		return (not self.__lt__(other, **kwargs))
		
	def __gt__(self, other, **kwargs):
		from const import Const
		from numbers import Number
		if not isinstance(other, Expr):
			if isinstance(other, str):
				other = Const(eval(other))
			elif isinstance(other, Number):
				other = Const(other)
		return (not self.__le__(other, **kwargs))
		
	def __int__(self, **kwargs):
		return int(self.value(**kwargs))
		
	def __le__(self, other, **kwargs):
		from const import Const
		from numbers import Number
		if not isinstance(other, Expr):
			if isinstance(other, str):
				other = Const(eval(other))
			elif isinstance(other, Number):
				other = Const(other)
		return (self.__lt__(other, **kwargs) or self.__eq__(other, **kwargs))
		
	def __long__(self, **kwargs):
		return long(self.value(**kwargs))
		
	def __lt__(self, other, **kwargs):
		from const import Const
		from numbers import Number
		if not isinstance(other, Expr):
			if isinstance(other, str):
				other = Const(eval(other))
			elif isinstance(other, Number):
				other = Const(other)
		return (self.value(**kwargs) < other.value(**kwargs))
		
	def __mod__(self, other):
		from const import Const
		from numbers import Number
		if not isinstance(other, Expr):
			if isinstance(other, str):
				other = Const(eval(other))
			elif isinstance(other, Number):
				other = Const(other)
		from mod import mod
		return Mod(self, other)
		
	def __mul__(self, other):
		from const import Const
		from numbers import Number
		if not isinstance(other, Expr):
			if isinstance(other, str):
				other = Const(eval(other))
			elif isinstance(other, Number):
				other = Const(other)
		from mul import Mul
		return Mul(self, other)
		
	def __ne__(self, other, **kwargs):
		from const import Const
		from numbers import Number
		if not isinstance(other, Expr):
			if isinstance(other, str):
				other = Const(eval(other))
			elif isinstance(other, Number):
				other = Const(other)
		return (not self.__eq__(other, **kwargs))
		
	def __neg__(self, **kwargs):
		from mul import Mul
		from const import Const
		return Mul(Const(-1), self)
		
	def __nonzero__(self, **kwargs):
		return self.value(**kwargs) != 0
		
	def __pow__(self, other):
		from const import Const
		from numbers import Number
		if not isinstance(other, Expr):
			if isinstance(other, str):
				other = Const(eval(other))
			elif isinstance(other, Number):
				other = Const(other)
		from pow import Pow
		return Pow(self, other)
		
	def __radd__(self, other):
		from const import Const
		from numbers import Number
		if not isinstance(other, Expr):
			if isinstance(other, str):
				other = Const(eval(other))
			elif isinstance(other, Number):
				other = Const(other)
		from add import Add
		return Add(other, self)
		
	def __rdiv__(self, other):
		from const import Const
		from numbers import Number
		if not isinstance(other, Expr):
			if isinstance(other, str):
				other = Const(eval(other))
			elif isinstance(other, Number):
				other = Const(other)
		from div import Div
		return Div(other, self)
		
	def __rdivmod__(self, other):
		from const import Const
		from numbers import Number
		if not isinstance(other, Expr):
			if isinstance(other, str):
				other = Const(eval(other))
			elif isinstance(other, Number):
				other = Const(other)
		from divmod import Divmod
		return Divmod(other, self)
		
	def __repr__(self, other):
		from const import Const
		from numbers import Number
		if not isinstance(other, Expr):
			if isinstance(other, str):
				other = Const(eval(other))
			elif isinstance(other, Number):
				other = Const(other)
		return self.expr
		
	def __rfloordiv(self, other):
		from const import Const
		from numbers import Number
		if not isinstance(other, Expr):
			if isinstance(other, str):
				other = Const(eval(other))
			elif isinstance(other, Number):
				other = Const(other)
		from floordiv import FloorDiv
		return FloorDiv(other, self)
		
	def __rmod__(self, other):
		from const import Const
		from numbers import Number
		if not isinstance(other, Expr):
			if isinstance(other, str):
				other = Const(eval(other))
			elif isinstance(other, Number):
				other = Const(other)
		from mod import Mod
		return Mod(other, self)
		
	def __rmul__(self, other):
		from const import Const
		from numbers import Number
		if not isinstance(other, Expr):
			if isinstance(other, str):
				other = Const(eval(other))
			elif isinstance(other, Number):
				other = Const(other)
		from mul import Mul
		return Mul(other, self)
		
	def __rpow__(self, other):
		from const import Const
		from numbers import Number
		if not isinstance(other, Expr):
			if isinstance(other, str):
				other = Const(eval(other))
			elif isinstance(other, Number):
				other = Const(other)
		from pow import Pow
		return Pow(other, self)
		
	def __rsub__(self, other):
		from const import Const
		from numbers import Number
		if not isinstance(other, Expr):
			if isinstance(other, str):
				other = Const(eval(other))
			elif isinstance(other, Number):
				other = Const(other)
		from sub import Sub
		return Sub(other, self)
		
	def __rtruediv__(self, other):
		from const import Const
		from numbers import Number
		if not isinstance(other, Expr):
			if isinstance(other, str):
				other = Const(eval(other))
			elif isinstance(other, Number):
				other = Const(other)
		from div import Div
		return Div(other, self)
		
	def __str__(self):
		return self.expr
		
	def __sub__(self, other):
		from const import Const
		from numbers import Number
		if not isinstance(other, Expr):
			if isinstance(other, str):
				other = Const(eval(other))
			elif isinstance(other, Number):
				other = Const(other)
		from sub import Sub
		return Sub(self, other)
		
	def __truediv__(self, other):
		from const import Const
		from numbers import Number
		if not isinstance(other, Expr):
			if isinstance(other, str):
				other = Const(eval(other))
			elif isinstance(other, Number):
				other = Const(other)
		from div import Div
		return Div(self, other)
		
	def __trunc__(self):
		from trunc import Trunc
		return Trunc(self)
		
	def as_integer_ratio(self, **kwargs):
		return self.value(**kwargs).as_integer_ratio()
		
	def conjugate(self, **kwargs):
		from mul import Mul
		return self - Mul(self.imagPart(**kwargs), Const(2))
		
	@property
	def imag(self):
		return self.imagPart()
		
	def imagPart(self, **kwargs):
		return Expr(str(self.value(**kwargs).imag))
		
	def is_integer(self, **kwargs):
		return self.value(**kwargs).is_integer()
	
	@property
	def real(self):
		return self.realPart()
		
	def realPart(self, **kwargs):
		return Expr(str(self.value(**kwargs).real))
	
	def value(self, **kwargs):
		return self.expr.value(**kwargs)
		
	def derivative(self, to = "x"):
		raise NotImplementedError("Deriving black box expressions isn't supported!")
