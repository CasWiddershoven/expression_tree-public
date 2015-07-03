 # basic Shunting-yard algorithm
def fromString(string):
	from numbers import Number
	# split into tokens
	tokens = tokenize(string)
	
	# stack used by the Shunting-Yard algorithm
	stack = []
	# output of the algorithm: a list representing the formula in RPN
	# this will contain Constant's and '+'s
	output = []
	
	# list of operators
	oplist = ['+', '-', '*', '/', '%', '**']
	funclist = ['(', 'sin(', 'cos(', 'abs(', 'log(']
	
	def isnumber(s):
		try:
			float(s)
			return True
		except ValueError:
			return False
	
	def isint(s):
		try:
			int(s)
			return True
		except ValueError:
			return False
	from const import Const
	for token in tokens:
		#it can be a numer, which wil go in the output
		if isnumber(token):
			if isint(token):
				output.append(Const(int(token)))
			else:
				output.append(Const(float(token)))
		#it might be an operator
		elif token in oplist:
			operator, precedence = operatorToken(token)
			while(len(stack) != 0 and stack[-1][1] < precedence):
				output.append(stack.pop()[0])
			stack.append([operator, precedence])
		#it might be a function
		elif token in funclist:
			operator, precedence = operatorToken(token)
			stack.append([operator, precedence])
		elif token == ')':
			# right parenthesis: pop everything upto the last left parenthesis to the output
			while not stack[-1][0] in funclist:
				output.append(stack.pop()[0])
			if stack[-1][0] != '(':
				output.append(stack.pop()[0])
			else:
				stack.pop()
		#else it's a variable
		else:
			output.append(token)
		
	# pop any tokens still on the stack to the output
	while len(stack) > 0:
		output.append(stack.pop()[0])
	
	return output
	
	
def operatorToken(operator):
	if(operator == '+' or operator == '-'):
		precedence = 5
	elif(operator == '*' or operator == '/' or operator == '%'):
		precedence = 4
	else:
		precedence = 6
	return operator, precedence
			
def tokenize(string):
	from re import sub
	string = sub("\)(?!(\+|-|$|\*|/|\)))", ")*", string)
	splitchars = ['+', '-', '*', '**', '/', '(', ')', 'sin(', 'cos(', 'abs(', 'log(']
	splitre = "(?P<op>(\+|-|\*\*|\*|/|\(|\)|sin\(|cos\(|abs\(|log\())"
	
	# surround any splitchar by spaces
	tokenstring = sub(splitre, " \g<op> ", string)
	#split on spaces - this gives us our tokens
	tokens = tokenstring.split()
	
	#special casing for **:
	#ans = []
	#for t in tokens:
	#	if len(ans) > 0 and t == ans[-1] == '*':
	#		ans[-1] = '**'
	#	else:
	#		ans.append(t)
	ans = tokens
	return ans
	

		
