class Solution:
    def isValid(self, s: str) -> bool:
        # iterate through s
        # use a stack
        # if it's open, add to stack
        # if it's closed, check that the closed bracket corresponds to open bracket on top of stack
        # use a hash map to map the corresponding brackets together
        # closed --> open

        parenthesis_map = {')' : '(', '}' : '{', ']': '['}
        stack = []

        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)
            else:
                if len(stack) == 0 or parenthesis_map.get(c) != stack.pop():
                    return False
                
        return len(stack) == 0
        