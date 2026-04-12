class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # create a mapping of numbers to letters '3':['d', 'e', 'f']
        # backtracking
        # current string
        # while my index is not out of bounds form digit string
        # if out of bounds, add the current string to my result
        # I would loop through the mapping for current number
        # add it onto the stirng and run dfs with it
        # remove that character from the string

        if not digits:
            return []

        res = []
        digitMap = {'2': ['a', 'b', 'c'], 
                    '3': ['d', 'e', 'f'],
                    '4': ['g', 'h', 'i'],
                    '5': ['j', 'k', 'l'],
                    '6': ['m', 'n', 'o'],
                    '7': ['p', 'q', 'r', 's'],
                    '8': ['t', 'u', 'v'],
                    '9': ['w', 'x', 'y', 'z']} 

        def dfs(curString, idx):
            if idx >= len(digits):
                res.append(curString)
                return
            
            for letter in digitMap[digits[idx]]:
                curString += letter
                dfs(curString, idx + 1)
                curString = curString[:-1]

        dfs("", 0)
        return res

        