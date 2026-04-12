class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # need to keep track of how many open and closing parenthesis there are, current string
        # recursive backtracking question as we are trying every possible combo
        # first thing --> try to add an open parenthesis (if statement)
        # recur
        # if no opening parenthesis is possible, close (outside)
        # recur 
        # set of all strings we've made --> return as a list when done

        res = set()

        def backtrack(openP, closeP, curStr):
            if openP == closeP == n:
                res.add(curStr)
                return
            if openP < n:
                backtrack(openP + 1, closeP, curStr + '(')
            if openP > closeP:
                backtrack(openP, closeP + 1, curStr + ')')

        backtrack(0, 0, '')
        return list(res)

        