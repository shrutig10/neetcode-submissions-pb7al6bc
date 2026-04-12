class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # make a hashmap [List[int], List[str]]
        # return all values

        mapping = {}

        for string in strs:
            freq = [0] * 26
            for char in string:
                freq[ord(char) - ord('a')] += 1
            if not mapping.get(tuple(freq)):
                mapping[tuple(freq)] = [string]
            else:
                mapping[tuple(freq)].append(string)

        return list(mapping.values())
