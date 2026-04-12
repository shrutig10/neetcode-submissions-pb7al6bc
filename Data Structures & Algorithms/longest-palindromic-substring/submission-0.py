class Solution:
    def longestPalindrome(self, s: str) -> str:
        # have a left and a right pointer
        # upper bound on lgest palindrome is the word itself
        # lower bound is one character of the word
        # go through s, and consider this as the center of the palindrome
        # for odd, iterate both sides at the same time
        # for even, first check that either neighbor is the same character, and then iterate both sides at the same time
        # result will be the longest string, update result based on the length of the string we build

        longest = ""
        
        for i in range(len(s)):
            cur_str = s[i]
            l, r = i - 1, i + 1

            # odd length
            while l >= 0 and r < len(s) and s[l] == s[r]:
                cur_str = s[l : r + 1]
                l -= 1
                r +=1 
            if len(cur_str) > len(longest):
                longest = cur_str

            # even length
            l, r = i - 1, i + 1
            if l >= 0 and s[l] == s[i]:
                cur_str = s[l : i + 1]
                l -= 1
            elif r < len(s) and s[i] == s[r]:
                cur_str = s[i : r + 1]
                r += 1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                cur_str = s[l : r + 1]
                l -= 1
                r +=1 
            if len(cur_str) > len(longest):
                longest = cur_str

        return longest
            


        
                
        