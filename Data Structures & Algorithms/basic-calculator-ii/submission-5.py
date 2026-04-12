class Solution:
    def calculate(self, s: str) -> int:
        # use a stack --> push operators onto it
        # need to keep track of prioirty of operator
        # if cur operator is higher, push onto stack
        # lower or equal, pop the stack until stack is empty or we reach a lower priority operator

        # evaluate the string with another stack
        # push numbers onto the stack
        # if we encounter an operator, pop the top two numbers in the stack and then evaluate and push back onto the stack

        expr = []
        stack = []

        idx = 0
        while idx < len(s):
            cur_num = ''
            while idx < len(s) and s[idx].isdigit():
                cur_num += s[idx]
                idx += 1
            
            if cur_num:
                expr.append(cur_num)

            if idx < len(s) and s[idx] in ['+', '-', '*', '/']:
                operator = s[idx]
                while stack and ((stack[-1] == '*' or stack[-1] == '/') or (operator in ['+', '-'] and stack[-1] in ['+', '-'])):
                    expr.append(stack.pop())
                stack.append(operator)
            
            idx += 1
        
        while stack:
            expr += stack.pop()

        for item in expr:
            if item in ['+', '-', '*', '/']:
                num2 = stack.pop()
                num1 = stack.pop()

                if item == '+':
                    stack.append(num1 + num2)
                elif item == '-':
                    stack.append(num1 - num2)
                elif item == '*':
                    stack.append(num1 * num2)
                else:
                    stack.append(num1 // num2)
            else:
                stack.append(int(item))
            
        return stack[0]


        





        