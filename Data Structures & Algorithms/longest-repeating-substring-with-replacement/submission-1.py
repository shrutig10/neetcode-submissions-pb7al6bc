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
            while r - l + 1 - mostFrequent > k:
                frequencies[s[l]] -=  1
                l += 1
            maxLength = max(maxLength, r - l + 1)

        return maxLength

        