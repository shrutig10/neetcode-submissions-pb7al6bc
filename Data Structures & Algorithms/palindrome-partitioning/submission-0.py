class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # all indiv letters will be palindromes
        # abababab --> aba bab a b, ababa, bab
        # backtracking
        # base case: we reached the end of the string
        # decision to make: make a partition, or keep going
        # make a partition when you have a substring that is a palindrome

        res = []

        def isPal(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1

            return True


        def backtrack(i, j, substrs):
            if i == len(s):
                if j == i:
                    res.append(substrs.copy())
                return 

            if isPal(j, i):
                substrs.append(s[j : i + 1])
                backtrack(i + 1, i + 1, substrs)
                substrs.pop()
            
            backtrack(i + 1, j, substrs)

        backtrack(0, 0, [])
        return res


            


        