class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        occurences = {}
        for c in s:
            if c in occurences:
                occurences[c] = occurences[c] + 1
            else:
                occurences[c] = 1
        
        for c in t:
            if c in occurences:
                occurences[c] = occurences[c] - 1
                if occurences[c] == 0:
                    occurences.pop(c)
            else:
                return False

        return len(occurences.keys()) == 0

