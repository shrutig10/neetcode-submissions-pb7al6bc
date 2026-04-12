class Solution:
    def isPalindrome(self, s: str) -> bool:
        s.replace(" ", "")
        s = s.lower()

        start = 0
        end = len(s) - 1

        while start < end:
            while(start < end and (not s[start].isalpha() and not s[start].isdigit())):
                start += 1
            while(end > start and (not s[end].isalpha() and not s[end].isdigit())):
                end -= 1
            if(s[start] != s[end]):
                return False
            start += 1
            end -= 1

        return True