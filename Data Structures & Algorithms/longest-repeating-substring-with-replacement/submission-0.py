class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLength = 0
        # go through string, however many chars that are not the same, keep counting until k
        frequencies = {}
        l = 0
        mostFrequent = 0

        for r in range(len(s)):
            frequencies[s[r]] = frequencies.get(s[r], 0) + 1
            mostFrequent = max(mostFrequent, frequencies[s[r]])
            curLength = r - l + 1
            if curLength - mostFrequent <= k:
                if curLength > maxLength:
                    maxLength = curLength
            else:
                while curLength - mostFrequent > k:
                    frequencies[s[l]] -=  1
                    l += 1
                    curLength = r - l + 1
            

        return maxLength

        