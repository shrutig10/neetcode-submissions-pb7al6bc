class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Freq = {}
        s1CharList = list(s1)

        for s in s1CharList:
            s1Freq[s] = s1Freq.get(s, 0) + 1
        
        l = 0
        s2Freq = {}

        for r in range(len(s2)):
            s2Freq[s2[r]] = s2Freq.get(s2[r], 0) + 1
            
            while r - l + 1 > len(s1):
                print(s2Freq)
                s2Freq[s2[l]] -= 1
                if s2Freq[s2[l]] == 0:
                    del s2Freq[s2[l]]
                l += 1
            
            if r - l + 1 == len(s1) and s2Freq == s1Freq:
                return True

        return False
            

        