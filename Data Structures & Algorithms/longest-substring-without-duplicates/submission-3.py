class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0

        left = 0
        right = 1
        longest = 1

        while right < len(s):
            while s[right] in s[left : right]:
                left += 1
            if len(s[left : right + 1]) > longest:
                longest = len(s[left : right + 1])
            right += 1

        return longest
        