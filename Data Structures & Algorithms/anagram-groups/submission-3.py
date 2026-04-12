class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # keep track of character frequencies
        # dict --> character frequency mapping (array) pointing to a list of strings with that character frequency mapping
        
        # go through each word and get character mapping
        # if that mapping exists, then append to the list 
        # otherwise make a new entry in the dictionary
        # return list of values

        anagrams = defaultdict(list)

        for word in strs:
            char_freq = [0] * 26
            for letter in word:
                char_freq[ord(letter) - ord('a')] += 1
            
            anagrams[tuple(char_freq)].append(word)

        return list(anagrams.values())

        