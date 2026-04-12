class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # backtracking
        # decision: either open or close
        # constraint: only close when we have at least one open
        # only add a close parenthesis when num of open > num of close
        # base case: when we have n sets of parenthesis --> num of closes and opens equal to n
        # if open ( < n --> add a ( backtrack --> if ) < ( --> add ), then backtrack
        # adjust open and closes accordingly

        res = []

        def backtrack(string, numOpen, numClose):
            if numOpen > n or numClose > n:
                return
            if numOpen == numClose == n:
                res.append(string)
                return
            
            if numClose < numOpen:
                string += ')'
                backtrack(string, numOpen, numClose + 1)
                string = string[:-1]

            string += '('
            backtrack(string, numOpen + 1, numClose)

        backtrack("", 0, 0)
        return res


        