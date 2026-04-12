class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # running longest length
        # set of all characters in substring
        # sliding window
        # l and r pointer
        # while the next character is different, increment right pointer 
        # once I hit a character I've seen before --> keep incrementing left pointer until all my characters are unique again
        # either set does not contain the letter at r or l = r
        # add character at r, and then update longest = max(longest, cur_length)
        # cur length = r - l + 1


        longest = 0
        substring = set()
        l = r = 0

        while r < len(s):
            while l < r and s[r] in substring:
                substring.remove(s[l])
                l += 1
            substring.add(s[r])
            r += 1
            longest = max(longest, r - l)
        
        return longest


        