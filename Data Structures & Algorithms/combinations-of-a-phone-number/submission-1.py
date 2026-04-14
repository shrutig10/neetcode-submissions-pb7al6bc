class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # recursive backtracking
        # get all possible combinations given the digits
        # create a map from digit to a list of characters
        # backtracking(curStr, curIndex):
        # base case: index is at the end --> add the string to our output list and return
        # index i that represents where in digits we are
        # for loop that will iterate through the digit's characters
        # for each character, run the backtrack(cur letter appended, index + 1)

        if not digits:
            return []

        res = []
        letterMap = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}

        def backtrack(curStr, curIdx):
            if curIdx >= len(digits):
                res.append(curStr)
                return
            
            for char in letterMap[digits[curIdx]]:
                backtrack(curStr + char, curIdx + 1)

        backtrack("", 0)
        return res
        