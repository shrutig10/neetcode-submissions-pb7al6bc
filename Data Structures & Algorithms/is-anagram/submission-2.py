class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # check for lengths to match

        # make a dict for s and get character frequencies (character: int)
        # while we go through all letters in t, check that the character matches in s
        # if the character matches, remove it from s (not the whole letter, just one instance)
        # check that the dict for s is empty --> if so, return True, else return False

        if len(s) != len(t):
            return False

        s_freq = dict()

        for letter in s:
            s_freq[letter] = s_freq.get(letter, 0) + 1

        for letter in t:
            if s_freq.get(letter):
                s_freq[letter] -= 1
                if s_freq[letter] == 0:
                    del s_freq[letter]
            else:
                return False

        return True if not s_freq else False
