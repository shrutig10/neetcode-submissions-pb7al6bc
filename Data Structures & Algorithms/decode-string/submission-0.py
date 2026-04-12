class Solution:
    def decodeString(self, s: str) -> str:
        # stack
        # running output
        # if you encounter a letter and stack is empty --> add it directly to output
        # push letter onto the stack
        # if you encounter a number, have a number string -> add it there
        # once you encounter a [, then push the number onto the stack before the [
        # once you encounter a ], pop characters until you get to [
        # when popping characters, build a string such that string = stack.pop() + string
        # after open bracket, pop the top of stack (number), multiply and push the whole string back onto the stack
        # if the stack exists <- push onto the stack, else, add directly to output

        stack = []
        output = ''
        number = ''

        for char in s:
            if char.isalpha():
                if not stack:
                    output += char
                else:
                    stack.append(char)

            elif char.isdigit():
                number += char

            elif char == '[':
                stack.append(number)
                number = ''
                stack.append(char)

            else:
                string = ''
                while stack[-1] != '[':
                    string = stack.pop() + string
                stack.pop() # to get rid of '['
                num = int(stack.pop())
                
                string *= num

                if stack:
                    stack.append(string)
                else:
                    output += string

        return output
            




        

        


                


