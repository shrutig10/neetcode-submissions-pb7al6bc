from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # care about the frequencies of letters
        # match words (match anagrams) is by the frequencies
        # we can store this in a dictionary or an array
        # dictionary called anagrams: key = frequencies, value=list of valid anagrams
        # when adding to dict, change the array to a tuple
        # iterate through strs, get its frequency match it in the dictionary or create a new entry

        anagrams = defaultdict(list)

        for string in strs:
            frequency = [0] * 26
            for char in string:
                frequency[ord(char) - ord('a')] += 1
            
            anagrams[tuple(frequency)].append(string)

        return list(anagrams.values())
        