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
		funclist = ['(', 'sin(', 'cos(', 'tan(', 'abs(', 'derive(', '==', '>=', '=<', '<', '>']
        
        for token in tokens:
			#it can be a numer, which wil go in the output
            if isnumber(token):
                if isint(token):
                    output.append(Const(int(token)))
                else:
                    output.append(Const(float(token)))
			#it might be an operator
            elif token in oplist:
				operator = operatorToken(token)
				while(len(stack) != 0 and stack[-1].precedence() < operator.precedence()):
					output.append(stack.pop().operator)
				stack.append(operator)
			#it might be a function
            elif token in funclist:
                stack.append(operatorToken(token))
            elif token == ')':
                # right parenthesis: pop everything up to the last left parenthesis to the output
                while not stack[-1] in funclist:
                    output.append(stack.pop().operator)
                if stack[-1] != '(':
					output.append(stack.pop())
				else:
					stack.pop()
			#else it's a variable
            else:
                output.append(t)
            
        # pop any tokens still on the stack to the output
        while len(stack) > 0:
            output.append(stack.pop())
		
		return output
        
		
	def operatorToken(string operator):
		self.operator = operator
		if(operator == '+' or operator == '-'):
			self.precedence = 5
		elif(operator == '*' or operator == '/' or operator == '%'):
			self.precedence = 4
		else:
			self.precedence = 6
			
def tokenize(string):
    splitchars = ['+', '-', '*', '/', '(', ')', 'sin(', 'cos(', 'tan(', 'abs(', 'derive(', '==', '>=', '=<', '<', '>']
    
    # surround any splitchar by spaces
    tokenstring = []
    for c in string:
        if c in splitchars:
            tokenstring.append(' %s ' % c)
        else:
            tokenstring.append(c)
    tokenstring = ''.join(tokenstring)
    #split on spaces - this gives us our tokens
    tokens = tokenstring.split()
    
    #special casing for **:
    ans = []
    for t in tokens:
        if len(ans) > 0 and t == ans[-1] == '*':
            ans[-1] = '**'
        else:
            ans.append(t)
    return ans
    
		