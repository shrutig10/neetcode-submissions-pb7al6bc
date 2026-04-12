class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        valid = {'(': ')', '[': ']', '{': '}'}

        for char in s:
            if char in valid:
                stack.append(char)
            elif len(stack) > 0 and char is valid[stack[-1]]:
                stack.pop()
            else:
                return False

        if len(stack) == 0:
            return True
        return False
        