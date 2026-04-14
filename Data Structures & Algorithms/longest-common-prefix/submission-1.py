class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # have a prefix that I run through against each string
        # I initialize prefix to the first word in strs
        # loop through strs, loop through the shorter word per iteration 
        # set prefix to this
        # if at any point prefix is empty, return immediately
        # at the end, return prefix

        prefix = strs[0]

        for word in strs:
            length = 0
            for i in range(min(len(prefix), len(word))):
                if prefix[i] != word[i]:
                    break
                length += 1
            if length == 0:
                return ""
            if length < len(prefix):
                prefix = word[:length]
            
        return prefix

                