class Solution:
    def decodeString(self, s: str) -> str:
        # stack
        # iterate through string
        # if we see a digit, keep a running number string that we append to, turn into int later
        # if we see a [, number is done, push number as int onto the stack, push the [
        # if we see a character, add to a character string
        # if we see a ], we know that the character string is done, pop the stack to get rid of the [, pop again to get number
        # multiply the character string by the number
        # push it back onto the stack
        # join the stack together, return this

        stack = []
        num = ''

        for char in s:
            if char.isdigit():
                num += char
            elif char == '[':
                stack.append(int(num))
                num = ''
                stack.append(char)
            elif char.isalpha():
                stack.append(char)
            else:
                substr = ''
                while stack[-1] != '[':
                    substr = stack.pop() + substr
                stack.pop() # get rid of '['
                multiplier = stack.pop()
                substr *= multiplier
                stack.append(substr)

        return "".join(stack)
            

        