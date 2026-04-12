class Solution:
    def validPalindrome(self, s: str) -> bool:
        # go from the two ends and meet in the center
        # check that either l : r - 1 is palindrome OR l + 1 : r is a palindrome
        # separate method to check for palindrome
        # iterate through s

        def isP(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            
            return True

        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return isP(l + 1, r) or isP(l, r - 1)

            l += 1
            r -=1

        return True
            



        