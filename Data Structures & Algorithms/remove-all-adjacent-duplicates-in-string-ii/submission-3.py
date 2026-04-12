class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # stack
        # keep track of last seen letter (substr)
        # if substr is len of k, then remove (set substr to top of the stack)
        # if cur letter does not match letters in substr, push substr onto stack and set substr to this letter
        # return "" if stack is empty otherwise top of the stack

        stack = []
        substr = ""

        for char in s:
            if len(substr) == k:
                if stack:
                    substr = stack.pop()
                else:
                    substr = ""

            if not substr or char == substr[0]:
                substr += char
            else:
                stack.append(substr)
                substr = char
        
        if len(substr) == k:
            substr = ""

        return substr if not stack else "".join(stack) + substr



