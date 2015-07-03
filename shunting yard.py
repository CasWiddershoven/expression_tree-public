 # basic Shunting-yard algorithm
    def fromString(string):
        # split into tokens
        tokens = tokenize(string)
        
        # stack used by the Shunting-Yard algorithm
        stack = []
        # output of the algorithm: a list representing the formula in RPN
        # this will contain Constant's and '+'s
        output = []
        
        # list of operators
        oplist = ['+', '-', '*', '/', '%']
		funclist = ['(', 'sin(', 'cos(', 'tan(']
        
        for token in tokens:
            if isnumber(token):
                # numbers go directly to the output
                if isint(token):
                    output.append(Const(int(token)))
                else:
                    output.append(Const(float(token)))
            elif token in oplist:
				operator = operatorToken(token)
				while(len(stack) != 0 and stack[-1].precedence() < operator.precedence()):
					output.append(stack.pop().operator)
				stack.append(operator)
            elif token in funclist:
                # left parentheses go to the stack
                stack.append(token)
            elif token == ')':
                # right parenthesis: pop everything upto the last left parenthesis to the output
                while not stack[-1] in funclist:
                    output.append(stack.pop().operator)
                if stack[-1] != '(':
					output.append(stack.pop())
				else:
					stack.pop()
            else:
                raise ValueError('Unknown token: %s' % token)
            
        # pop any tokens still on the stack to the output
        while len(stack) > 0:
            output.append(stack.pop())
		
		return output
        
		
	def operatorToken(string operator):
		self.operator = operator
		if(operator == '+' or operator == '-'):
			self.precedence = 5
		if(operator == '*' or operator == '/' or operator == '%')
			self.precedence = 4
		