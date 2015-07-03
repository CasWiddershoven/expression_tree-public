from abs import Abs
from add import Add
from cos import Cos
from div import Div
from log import Log
from mod import Mod
from mul import Mul
from pow import Pow
from root import Root
from sin import Sin
from sub import Sub
from const import Const
oplist = ['+', '-', '*', '/', '%']
funclist = ['(', 'sin(', 'cos(', 'tan(', 'abs(', 'derive(']
functiondict = {'abs(' : Abs, '+' : Add, 'cos(' : Cos, '/' : Div,
				'log(' : Log, '%' : Mod, '*' : Mul, '**' : Pow, 'root(' : Root,
				'sin(' : Sin, '-' : Sub}


def fromPolish(queue):
	stack = []
	for t in queue:
		if isinstance(t, str) and t in oplist:
			x = stack.pop()
			y = stack.pop()
			print x, t, y
			stack.append(functiondict[t](x, y))
		elif isinstance(t, str) and t in funclist:
			x = stack.pop()
			stack.append(functiondict[t](x))
		elif isinstance(t, Const):
			stack.append(t)
		else:
			stack.append(Var(t))
	return stack.pop()
		
