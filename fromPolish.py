	functiondict = {'abs(' : Abs, '+' : Add, 'cos(' : Cos, '/' : Div,
					'log(' : Log, '%' : Mod, '*' : Mul, '**' : Pow, 'root(' : Root,
					'sin(' : Sin, '-' : Sub}
					
	
	
	def fromPolish(list queue):
		stack = []
		for t in output:
			if t in oplist:
				x = stack.pop()
				y = stack.pop()
				stack.append(functiondict[t](x, y))
			elif t in funclist:
				x = stack.pop()
				stack.append(functiondict[t](x)
			elif isNumber(t):
				stack.append(Const(toNumber(t)))
			else
				stack.append(Var(t))
		return stack.pop()
		