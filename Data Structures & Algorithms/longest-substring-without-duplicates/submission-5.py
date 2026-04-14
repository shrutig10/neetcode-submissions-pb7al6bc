class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window approach
        # left and right pointer, increment right as long as no duplicates are seen
        # create a set of seen characters
        # as you move right, check that char is not in seen, and then add it to seen
        # compare length with max and update accordingly max(curMax, curLength)
        # if we have seen, move the left pointer and remove those characters from set until 
        # the character at the right pointer is not seen anymore 

        seen = set()
        l = r = 0
        maxLen = 0
        curLen = 0

        while r < len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
                curLen -= 1
                
            seen.add(s[r])
            curLen += 1
            maxLen = max(maxLen, curLen)
            r += 1
        
        return maxLen

        