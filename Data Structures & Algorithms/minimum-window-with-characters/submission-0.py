class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #create frequency table for t
        #go through s and keep incrememnting right until you see all 
        #letters that are in t (frequencies match)
        #increment left until you change something in t (Stop there and set min from one back)
        #keep incrementing right until you hit all of t again

        # check that character is in t --> go through changing left pointer

        tFreq = {}

        for char in t:
            tFreq[char] = tFreq.get(char, 0) + 1

        res = s * 2
        sFreq = {}
        l = 0

        for r in range(len(s)):
            if s[r] in tFreq:
                sFreq[s[r]] = sFreq.get(s[r], 0) + 1
                while self.checkMaps(tFreq, sFreq):
                    if len(s[l : r + 1]) < len(res):
                        res = s[l : r + 1]
                    if sFreq.get(s[l]):
                        sFreq[s[l]] -= 1
                    l += 1
        
        if len(res) > len(s):
            return ""
        return res

    def checkMaps(self, map1, map2):
        if map1.keys() != map2.keys():
            return False
        
        for key in map1.keys():
            if map2[key] < map1[key]:
                return False

        return True
                


        