class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # iterate through string
        # check that each substring exists
        # continue and see if a longer stirng exists, try a new word for the next character
        # stored whether or not future words can be made
        # dp bottom up solution


        dp = [False] * (len(s) + 1)
        dp[-1] = True

        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if i + len(word) <= len(s) and s[i : i + len(word)] == word:
                    dp[i] = dp[i + len(word)]
                if dp[i]:
                    break
        
        return dp[0]


        
        