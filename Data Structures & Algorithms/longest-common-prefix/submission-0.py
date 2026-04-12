class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # we know the prefix cannot be longer than the shortest word
        # lower bound for prefix is ""
        # we get the shortest word <-- loop through the rest of strs
        # whatever the maximum common prefix is between those two words will be the result (update every iteration)
        # minimum of the common prefix and the current result

        res = strs[0]

        for i in range(1, len(strs)):
            common_prefix = ""
            for k in range(min(len(res), len(strs[i]))):
                if res[k] == strs[i][k]:
                    common_prefix += strs[i][k]
                else:
                    break
            
            if len(res) > len(common_prefix):
                res = common_prefix

        return res



        